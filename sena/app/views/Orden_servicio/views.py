from urllib import request

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import timedelta, date

from app.forms import OrdenServicioForm
from app.models import (
    OrdenServicio,
    OrdenServicioDetalle,
    DetalleOrdenProducto,
    Vehiculo,
    Producto,
    CompatibilidadProducto,
    SeguimientoMantenimiento,
)


# ══════════════════════════════════════════════════════════
#  CONFIGURACIÓN DE MANTENIMIENTO POR TIPO DE USO
# ══════════════════════════════════════════════════════════
CONFIG_MANTENIMIENTO = {
    'BAJO':   (30,  5000),
    'NORMAL': (50,  5000),
    'ALTO':   (200, 8000),
    'CARGA':  (400, 15000),
}


MAX_DIAS_SIN_REVISION = 365


def _calcular_fecha_sugerida(vehiculo, km_actual=None):
    config = CONFIG_MANTENIMIENTO.get(vehiculo.tipo_uso, (50, 5000))
    km_diarios, km_por_cambio = config
    km_base = km_actual if km_actual else 0
    if km_base > 0:
        km_proximo = ((km_base // km_por_cambio) + 1) * km_por_cambio
        km_faltan  = km_proximo - km_base
    else:
        km_faltan  = km_por_cambio
        km_proximo = km_por_cambio
    dias = max(1, km_faltan // km_diarios)
    dias = min(dias, MAX_DIAS_SIN_REVISION)
    return date.today() + timedelta(days=dias), km_proximo, dias


def _info_mantenimiento(vehiculo, km_actual=None):
    config = CONFIG_MANTENIMIENTO.get(vehiculo.tipo_uso, (50, 5000))
    km_diarios, km_por_cambio = config
    fecha, km_proximo, dias = _calcular_fecha_sugerida(vehiculo, km_actual)
    km_base = km_actual if km_actual else 0
    km_faltan = max(0, km_proximo - km_base)
    return {
        'fecha_sugerida':  fecha.isoformat(),
        'km_proximo':      km_proximo,
        'km_faltan':       km_faltan,
        'km_diarios':      km_diarios,
        'km_por_cambio':   km_por_cambio,
        'dias':            dias,
        'tipo_uso_label':  vehiculo.get_tipo_uso_display(),
    }


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


def _verificar_compat(producto, marca_id, servicio_id=None):
    total = CompatibilidadProducto.objects.filter(producto=producto).count()
    if total == 0:
        return 'neutral', ''
    qs = CompatibilidadProducto.objects.filter(producto=producto, marca_vehiculo_id=marca_id)
    if servicio_id and qs.filter(tipo_servicio_id=servicio_id).exists():
        return 'ok', f'{producto.nombre} es compatible con esta marca y servicio.'
    if qs.filter(tipo_servicio__isnull=True).exists():
        return 'ok', f'{producto.nombre} es compatible con esta marca.'
    marcas_ok = list(
        CompatibilidadProducto.objects
        .filter(producto=producto)
        .values_list('marca_vehiculo__nombre', flat=True)
        .distinct()
    )
    return 'warn', f'{producto.nombre} no aplica para esta marca. Aplica para: {", ".join(marcas_ok)}.'


def _get_productos_disponibles():
    return Producto.objects.filter(estado=True, stock__gt=0).order_by('nombre')


def _guardar_productos(request, orden):
    producto_ids = request.POST.getlist('producto_ids[]')
    cantidades   = request.POST.getlist('producto_cantidades[]')
    errores = []
    for pid, cant in zip(producto_ids, cantidades):
        try:
            prod = Producto.objects.get(pk=pid, estado=True)
            DetalleOrdenProducto.objects.create(
                orden=orden, producto=prod, cantidad=max(1, int(cant))
            )
        except (Producto.DoesNotExist, ValueError):
            continue
        except ValidationError as e:
            errores.append(e.message)
    return errores


def _guardar_servicios_detalle(form, orden):
    orden.servicios_detalle.all().delete()
    servicios = form.cleaned_data.get('servicios', [])
    for tipo in servicios:
        OrdenServicioDetalle.objects.create(
            orden=orden,
            tipo_servicio=tipo,
            precio_mano_obra=tipo.precio_mano_obra,
        )


def _hay_incompatibles(request, marca_id, servicio_ids):
    for pid in request.POST.getlist('producto_ids[]'):
        try:
            prod = Producto.objects.get(pk=pid, estado=True)
            total_reglas = CompatibilidadProducto.objects.filter(producto=prod).count()
            if total_reglas == 0:
                continue
            es_compatible = False
            for sid in servicio_ids:
                status, _ = _verificar_compat(prod, marca_id, sid)
                if status in ('ok', 'neutral'):
                    es_compatible = True
                    break
            if not es_compatible:
                return True
        except Producto.DoesNotExist:
            continue
    return False


def _crear_seguimientos(request, orden):
    servicios_con_seguimiento = orden.servicios.filter(requiere_seguimiento=True)
    if not servicios_con_seguimiento.exists():
        return

    # Una sola fuente de verdad: fecha, km_proximo y dias salen juntos y
    # consistentes entre sí (incluyendo el tope por tiempo ya aplicado).
    fecha_calculada, km_proximo, dias = _calcular_fecha_sugerida(orden.vehiculo, orden.km_actual)

    fecha_form = request.POST.get('fecha_proximo_mantenimiento') or None
    if fecha_form:
        try:
            fecha_proximo = date.fromisoformat(fecha_form)
        except ValueError:
            fecha_proximo = fecha_calculada
    else:
        fecha_proximo = fecha_calculada

    config = CONFIG_MANTENIMIENTO.get(orden.vehiculo.tipo_uso, (50, 5000))
    km_diarios, km_por_cambio = config
    km_faltan = max(0, km_proximo - orden.km_actual)

    SeguimientoMantenimiento.objects.filter(
        vehiculo=orden.vehiculo,
        activo=True
    ).update(activo=False)

    tipo_uso_label = orden.vehiculo.get_tipo_uso_display()

    for servicio in servicios_con_seguimiento:
        SeguimientoMantenimiento.objects.create(
            vehiculo=orden.vehiculo,
            orden_servicio=orden,
            tipo_servicio=servicio,
            km_al_momento=orden.km_actual,
            km_proximo_mantenimiento=km_proximo,
            fecha_proximo_mantenimiento=fecha_proximo,
            estado='Pendiente',
            activo=True,
            observaciones=(
                f'Creado automáticamente desde Orden #{orden.pk}. '
                f'Km al momento: {orden.km_actual:,}. '
                f'Próximo cambio a los {km_proximo:,} km '
                f'({km_faltan:,} km restantes). '
                f'Uso del vehículo: {tipo_uso_label} '
                f'(~{km_diarios} km/día, cambio cada {km_por_cambio:,} km). '
                f'Estimado: {dias} días.'
            ),
        )


# ══════════════════════════════════════════════════════════
#  LISTAR
# ══════════════════════════════════════════════════════════
class OrdenServicioListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = OrdenServicio
    template_name = 'OrdenServicio/listar.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related(
            'servicios_detalle__tipo_servicio',
            'productos_usados__producto',
        )
        for orden in qs:
            marca_id     = orden.vehiculo.marca_id
            servicio_ids = list(orden.servicios.values_list('id', flat=True))
            tiene_warn   = False
            for detalle in orden.productos_usados.all():
                es_compat = False
                for sid in servicio_ids:
                    status, _ = _verificar_compat(detalle.producto, marca_id, sid)
                    if status in ('ok', 'neutral'):
                        es_compat = True
                        break
                if not es_compat:
                    tiene_warn = True
                    break
            orden.tiene_incompatibles = tiene_warn
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Órdenes de Servicio'
        return context


# ══════════════════════════════════════════════════════════
#  CAMBIAR ESTADO
# ══════════════════════════════════════════════════════════
class CambiarEstadoOrdenView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def post(self, request, pk):
        orden = get_object_or_404(OrdenServicio, pk=pk)
        if orden.estado == 'Terminado':
            messages.error(request, f'La orden #{orden.pk} ya está terminada y no puede modificarse.')
            return redirect('app:orden_servicio_list')
        nuevo_estado = request.POST.get('estado')
        flujo = ['Pendiente', 'En Proceso', 'Terminado']
        if nuevo_estado in flujo:
            idx_actual = flujo.index(orden.estado)
            idx_nuevo  = flujo.index(nuevo_estado)
            if idx_nuevo == idx_actual + 1:
                orden.estado = nuevo_estado
                orden.save(update_fields=['estado'])
                messages.success(request, f'Orden #{orden.pk} → {nuevo_estado}')
            else:
                messages.error(request, 'Cambio de estado no permitido.')
        else:
            messages.error(request, 'Estado inválido.')
        return redirect('app:orden_servicio_list')


# ══════════════════════════════════════════════════════════
#  DETALLE
# ══════════════════════════════════════════════════════════
class OrdenServicioDetailView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request, pk):
        orden    = get_object_or_404(OrdenServicio, pk=pk)
        detalles = DetalleOrdenProducto.objects.filter(orden=orden).select_related('producto')
        marca_id     = orden.vehiculo.marca_id
        servicio_ids = list(orden.servicios.values_list('id', flat=True))
        for d in detalles:
            best_status = 'warn'
            best_msg    = ''
            for sid in servicio_ids:
                s, m = _verificar_compat(d.producto, marca_id, sid)
                if s in ('ok', 'neutral'):
                    best_status = s
                    best_msg    = m
                    break
            d.compat_status, d.compat_mensaje = best_status, best_msg
        mano_obra = sum(d.precio_mano_obra for d in orden.servicios_detalle.all())
        subtotal_productos = sum(d.precio_unitario * d.cantidad for d in detalles)
        total = subtotal_productos + mano_obra
        return render(request, 'OrdenServicio/detalle.html', {
            'orden':               orden,
            'detalles':            detalles,
            'subtotal_productos':  subtotal_productos,
            'mano_obra':           mano_obra,
            'total':               total,
            'titulo':              f'Detalle Orden #{orden.pk}',
            'listar_url':          reverse_lazy('app:orden_servicio_list'),
        })


# ══════════════════════════════════════════════════════════
#  AJAX
# ══════════════════════════════════════════════════════════
class VehiculoKmView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request, pk):
        try:
            v = Vehiculo.objects.select_related('marca').get(pk=pk)
            km_actual = int(request.GET.get('km', 0)) or 0
            info = _info_mantenimiento(v, km_actual if km_actual else None)
            return JsonResponse({
                'km':              0,
                'placa':           v.placa,
                'marca_id':        v.marca_id,
                'marca_nombre':    v.marca.nombre,
                'tipo_uso':        v.tipo_uso,
                'tipo_uso_label':  v.get_tipo_uso_display(),
                'fecha_sugerida':  info['fecha_sugerida'],
                'km_proximo':      info['km_proximo'],
                'km_faltan':       info['km_faltan'],
                'km_diarios':      info['km_diarios'],
                'km_por_cambio':   info['km_por_cambio'],
                'dias':            info['dias'],
            })
        except Vehiculo.DoesNotExist:
            return JsonResponse({'km': 0}, status=404)


class VerificarCompatibilidadView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request):
        producto_id = request.GET.get('producto')
        marca_id    = request.GET.get('marca')
        servicio_id = request.GET.get('servicio')
        if not producto_id or not marca_id:
            return JsonResponse({'compatible': None, 'tiene_reglas': False, 'mensaje': ''})
        try:
            producto = Producto.objects.get(pk=producto_id)
        except Producto.DoesNotExist:
            return JsonResponse({'compatible': None, 'tiene_reglas': False, 'mensaje': ''})
        status, mensaje = _verificar_compat(producto, marca_id, servicio_id)
        if status == 'neutral':
            return JsonResponse({'compatible': False, 'tiene_reglas': False, 'mensaje': ''})
        elif status == 'ok':
            return JsonResponse({'compatible': True,  'tiene_reglas': True,  'mensaje': mensaje})
        else:
            return JsonResponse({'compatible': False, 'tiene_reglas': True,  'mensaje': mensaje})


class ProductosCompatiblesView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request):
        marca_id    = request.GET.get('marca')
        servicio_id = request.GET.get('servicio')
        if not marca_id:
            return JsonResponse({'productos': []})
        qs_base = CompatibilidadProducto.objects.filter(marca_vehiculo_id=marca_id).select_related('producto')
        qs = (
            qs_base.filter(tipo_servicio_id=servicio_id) |
            qs_base.filter(tipo_servicio__isnull=True)
        ) if servicio_id else qs_base
        productos, vistos = [], set()
        for comp in qs:
            if comp.producto_id not in vistos and comp.producto.estado:
                vistos.add(comp.producto_id)
                productos.append({
                    'id':     comp.producto.pk,
                    'nombre': comp.producto.nombre,
                    'stock':  comp.producto.stock,
                    'precio': float(comp.producto.precio),
                })
        return JsonResponse({'productos': productos})


# ══════════════════════════════════════════════════════════
#  CREAR
# ══════════════════════════════════════════════════════════
class OrdenServicioCreateView(LoginRequiredMixin, AdminOMecanicoMixin, CreateView):
    model         = OrdenServicio
    form_class    = OrdenServicioForm
    template_name = 'OrdenServicio/crear.html'
    success_url   = reverse_lazy('app:orden_servicio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']                = 'Nueva Orden de Servicio'
        context['listar_url']            = reverse_lazy('app:orden_servicio_list')
        context['es_editar']             = False
        context['productos_disponibles'] = _get_productos_disponibles()
        return context

    def form_valid(self, form):
        orden = form.save(commit=False)
        orden.fecha = timezone.now()
        orden.save()
        _guardar_servicios_detalle(form, orden)

        servicio_ids = list(orden.servicios.values_list('id', flat=True))
        if _hay_incompatibles(self.request, orden.vehiculo.marca_id, servicio_ids):
            messages.error(self.request, '⚠ No se puede guardar: hay productos incompatibles con la marca.')
            orden.delete()
            return self.form_invalid(form)

        errores = _guardar_productos(self.request, orden)
        if errores:
            for e in errores:
                messages.error(self.request, f'⚠ {e}')
            orden.delete()
            return self.form_invalid(form)

        _crear_seguimientos(self.request, orden)
        messages.success(self.request, 'Orden de servicio creada correctamente.')
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


# ══════════════════════════════════════════════════════════
#  EDITAR
# ══════════════════════════════════════════════════════════
class OrdenServicioUpdateView(LoginRequiredMixin, AdminOMecanicoMixin, UpdateView):
    model         = OrdenServicio
    form_class    = OrdenServicioForm
    template_name = 'OrdenServicio/crear.html'
    success_url   = reverse_lazy('app:orden_servicio_list')

    def dispatch(self, request, *args, **kwargs):
        orden = get_object_or_404(OrdenServicio, pk=kwargs['pk'])
        if orden.estado == 'Terminado':
            messages.error(request, f'La orden #{orden.pk} ya está terminada y no puede editarse.')
            return redirect('app:orden_servicio_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']                = 'Editar Orden de Servicio'
        context['listar_url']            = reverse_lazy('app:orden_servicio_list')
        context['es_editar']             = True
        context['productos_disponibles'] = _get_productos_disponibles()
        return context

    def form_valid(self, form):
        orden = form.save(commit=False)
        orden.fecha = self.get_object().fecha
        orden.save()
        _guardar_servicios_detalle(form, orden)

        servicio_ids = list(orden.servicios.values_list('id', flat=True))
        if _hay_incompatibles(self.request, orden.vehiculo.marca_id, servicio_ids):
            messages.error(self.request, '⚠ No se puede guardar: hay productos incompatibles con la marca.')
            return self.form_invalid(form)

        orden.productos_usados.all().delete()
        errores = _guardar_productos(self.request, orden)
        if errores:
            for e in errores:
                messages.error(self.request, f'⚠ {e}')
            return self.form_invalid(form)

        _crear_seguimientos(self.request, orden)
        messages.success(self.request, 'Orden de servicio actualizada correctamente.')
        return redirect(self.success_url)


# ══════════════════════════════════════════════════════════
#  ELIMINAR
# ══════════════════════════════════════════════════════════
class OrdenServicioDeleteView(LoginRequiredMixin, SoloAdminMixin, View):
    def get(self, request, pk):
        orden = get_object_or_404(OrdenServicio, pk=pk)
        return render(request, 'OrdenServicio/eliminar.html', {
            'object':     orden,
            'titulo':     'Eliminar Orden de Servicio',
            'listar_url': reverse_lazy('app:orden_servicio_list'),
        })

    def post(self, request, pk):
        orden = get_object_or_404(OrdenServicio, pk=pk)
        SeguimientoMantenimiento.objects.filter(
            orden_servicio=orden
        ).update(activo=False, estado='Completado')
        orden.delete()
        messages.success(request, 'Orden de servicio eliminada correctamente.')
        return redirect('app:orden_servicio_list')