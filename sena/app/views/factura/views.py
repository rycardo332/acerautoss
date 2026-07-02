import threading

from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from decimal import Decimal

from app.models import Factura, OrdenServicio, Producto, Caja, Notificacion
from app.forms import FacturaForm
from app.views.Notificacion.views import _enviar_correo_orden_terminada


# ── Mixin 1: Solo ADMIN ──────────────────────────────────────────
class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para realizar esta acción.")
        return redirect('app:dashboard')


# ── Mixin 2: ADMIN o MECANICO ────────────────────────────────────
class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


# ── LISTAR ────────────────────────────────────────────────────────
class FacturaListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Factura
    template_name = 'factura/listar.html'
    context_object_name = 'factura'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Facturas'
        return context


# ── CREAR ─────────────────────────────────────────────────────────
class FacturaCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/crear.html'
    success_url = reverse_lazy('app:listar_factura')

    def form_valid(self, form):
        factura = form.save(commit=False)
        tipo    = factura.tipo

        if tipo == 'SERVICIO':
            orden    = factura.orden_servicio
            subtotal = Decimal('0')
            for servicio in orden.servicios.all():
                subtotal += servicio.precio_mano_obra
            for detalle in orden.productos_usados.select_related('producto').all():
                subtotal += detalle.producto.precio * detalle.cantidad
            factura.total = subtotal

        elif tipo == 'PRODUCTO':
            producto = form.cleaned_data.get('producto')
            cantidad = form.cleaned_data.get('cantidad')
            if producto and cantidad:
                factura.total = producto.precio * cantidad
                Producto.objects.filter(pk=producto.pk).update(
                    stock=producto.stock - cantidad
                )

        factura.estado_pago = 'Pendiente'
        factura.save()
        messages.success(self.request, f"Factura {factura.numero_factura} creada correctamente.")
        return redirect(self.success_url)


# ── DETALLE ───────────────────────────────────────────────────────
class FacturaDetailView(LoginRequiredMixin, AdminOMecanicoMixin, DetailView):
    model = Factura
    template_name = 'factura/detalle.html'
    context_object_name = 'factura'


# ── ELIMINAR ──────────────────────────────────────────────────────
class FacturaDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Factura
    template_name = 'factura/eliminar.html'
    success_url = reverse_lazy('app:listar_factura')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Factura'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Factura eliminada correctamente.')
        return super().form_valid(form)


# ── PAGAR ─────────────────────────────────────────────────────────
class PagarFacturaView(LoginRequiredMixin, SoloAdminMixin, View):
    EXTENSIONES_VALIDAS = ('.pdf', '.jpg', '.jpeg', '.png', '.gif')
    TAMANO_MAX_MB = 5
    METODOS_CON_COMPROBANTE = ('Nequi', 'Transferencia', 'Daviplata')

    def post(self, request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        metodo  = request.POST.get('metodo_pago', '').strip()
        metodos_validos = [m[0] for m in Factura.METODOS_PAGO]

        if not metodo or metodo not in metodos_validos:
            messages.error(request, "Seleccione un método de pago válido.")
            return redirect('app:listar_factura')

        if factura.estado_pago == 'Pagada':
            messages.warning(request, "Esta factura ya fue pagada.")
            return redirect('app:listar_factura')

        # ── Validación de comprobante ──────────────────────────
        comprobante = request.FILES.get('comprobante_pago')

        if metodo in self.METODOS_CON_COMPROBANTE:
            if not comprobante:
                messages.error(request, f"Debe adjuntar el comprobante de pago para {metodo}.")
                return redirect('app:listar_factura')

            nombre = comprobante.name.lower()
            if not nombre.endswith(self.EXTENSIONES_VALIDAS):
                messages.error(request, "El comprobante debe ser PDF, JPG, PNG o GIF.")
                return redirect('app:listar_factura')

            if comprobante.size > self.TAMANO_MAX_MB * 1024 * 1024:
                messages.error(request, f"El comprobante no puede superar {self.TAMANO_MAX_MB}MB.")
                return redirect('app:listar_factura')

            factura.comprobante_pago = comprobante

        factura.metodo_pago = metodo
        factura.estado_pago = 'Pagada'
        factura.fecha_pago  = timezone.now()
        factura.save()

        # ── Registro en caja ───────────────────────────────────
        ya_existe = Caja.objects.filter(
            descripcion__icontains=factura.numero_factura,
            tipo='INGRESO'
        ).exists()

        if not ya_existe:
            Caja.objects.create(
                descripcion = f"Factura {factura.numero_factura} — {factura.get_tipo_display()}",
                monto       = factura.total,
                tipo        = 'INGRESO',
                categoria   = 'Ventas' if factura.tipo == 'PRODUCTO' else 'Servicios',
                metodo_pago = metodo,
            )

        # ── Orden de servicio: pasar a Terminado + notificar ──
        if factura.tipo == 'SERVICIO' and factura.orden_servicio:
            orden = factura.orden_servicio
            if orden.estado != 'Terminado':
                orden.estado = 'Terminado'
                orden.save()

                vehiculo = orden.vehiculo
                cliente  = vehiculo.cliente

                # Notificación interna en el sistema
                Notificacion.objects.create(
                    tipo='Mantenimiento',
                    origen='SISTEMA',
                    titulo=f'Servicio completado — {vehiculo.placa}',
                    vehiculo=vehiculo,
                    mensaje=(
                        f'El servicio de la orden #{orden.pk} ha sido completado '
                        f'y el pago registrado. El vehículo {vehiculo.placa} '
                        f'({vehiculo.marca.nombre} {vehiculo.modelo}) ya puede ser retirado.'
                    ),
                    leido=False,
                )

                # Correo al cliente en background para no bloquear la respuesta
                def _enviar():
                    _enviar_correo_orden_terminada(cliente, vehiculo, orden)

                t = threading.Thread(target=_enviar)
                t.daemon = True
                t.start()

        messages.success(request, "Pago registrado correctamente.")
        return redirect('app:listar_factura')