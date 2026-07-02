from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.db.models import ProtectedError

from app.models import Producto
from app.forms import ProductoForm

STOCK_MINIMO_DEFAULT = 5


def get_stock_status(producto):
    if producto.stock == 0:
        return 'sin'
    minimo = producto.stock_minimo if producto.stock_minimo > 0 else STOCK_MINIMO_DEFAULT
    if producto.stock <= minimo:
        return 'bajo'
    return 'ok'


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


# ── LISTAR — Mecánico solo puede ver ─────────────────────────────
class ProductoListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Producto
    template_name = 'producto/listar.html'
    context_object_name = 'productos'

    def get_queryset(self):
        qs = Producto.objects.select_related('marca').order_by('-id')
        for p in qs:
            p.stock_status = get_stock_status(p)
            p.stock_minimo_efectivo = p.stock_minimo if p.stock_minimo > 0 else STOCK_MINIMO_DEFAULT
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Producto.objects.all()
        context['titulo']              = 'Inventario de Productos'
        context['crear_url']           = reverse_lazy('app:crear_producto')
        context['total_productos']     = qs.count()
        context['activos']             = qs.filter(estado=True).count()
        context['sin_stock']           = qs.filter(stock=0).count()
        context['stock_bajo']          = sum(1 for p in qs.filter(stock__gt=0) if get_stock_status(p) == 'bajo')
        context['valor_inventario']    = sum(p.precio * p.stock for p in qs.filter(estado=True))
        context['stock_minimo_default'] = STOCK_MINIMO_DEFAULT
        return context


# ── CREAR — Solo Admin ────────────────────────────────────────────
class ProductoCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url == 'orden':
            return reverse_lazy('app:orden_servicio_create')
        return reverse_lazy('app:listar_producto')

    def form_valid(self, form):
        messages.success(self.request, 'Producto creado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Crear Producto'
        context['listar_url'] = reverse_lazy('app:listar_producto')
        context['next']       = self.request.GET.get('next', '')
        return context


# ── EDITAR — Solo Admin ───────────────────────────────────────────
class ProductoUpdateView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('app:listar_producto')

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Editar Producto'
        context['listar_url'] = reverse_lazy('app:listar_producto')
        context['next']       = self.request.GET.get('next', '')
        return context


# ── ELIMINAR — Solo Admin ─────────────────────────────────────────
class ProductoDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Producto
    template_name = 'producto/eliminar.html'
    success_url = reverse_lazy('app:listar_producto')

    def form_valid(self, form):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, 'Producto eliminado correctamente.')
        except ProtectedError:
            # El producto está referenciado en órdenes de servicio (DetalleOrdenProducto)
            # y no se puede eliminar sin perder el historial. Avisamos y redirigimos
            # de vuelta sin tocar la base de datos.
            messages.error(
                self.request,
                f"No se puede eliminar '{self.object.nombre}' porque ya fue usado en una o más "
                f"órdenes de servicio. Para conservar el historial, desactívalo en su lugar "
                f"(editar producto → Estado: Inactivo)."
            )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Eliminar Producto'
        context['listar_url'] = reverse_lazy('app:listar_producto')
        return context


# ── CAMBIAR ESTADO (toggle rápido activo/inactivo) — Solo Admin ──
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


class ProductoCambiarEstadoView(LoginRequiredMixin, SoloAdminMixin, View):
    """
    Alterna el campo `estado` del producto (activo/inactivo) vía AJAX,
    sin recargar la página. Se usa desde el botón switch en la tabla
    y en las tarjetas del catálogo.
    """
    def post(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        producto.estado = not producto.estado
        producto.save(update_fields=['estado'])
        return JsonResponse({
            'ok': True,
            'estado': producto.estado,
            'mensaje': f"'{producto.nombre}' ahora está {'activo' if producto.estado else 'inactivo'}.",
        })

    def handle_no_permission(self):
        return JsonResponse({'ok': False, 'mensaje': 'No tienes permisos para realizar esta acción.'}, status=403)