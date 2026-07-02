from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ...models import CompatibilidadProducto, Producto, Marca
from ...forms import CompatibilidadProductoForm


# ── Mixin 1: Solo ADMIN ──────────────────────────────────────────
class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para este módulo.")
        return redirect('app:dashboard')

# ── Mixin 2: ADMIN o MECANICO ────────────────────────────────────
class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


# ── 1. LISTADO — Mecánico puede ver ──────────────────────────────
class CompatibilidadListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = CompatibilidadProducto
    template_name = 'compatibilidadProducto/listar.html'
    context_object_name = 'compatibilidades'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Compatibilidad de Productos'
        return context


# ── 2. CREAR — Solo Admin ─────────────────────────────────────────
class CompatibilidadCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = CompatibilidadProducto
    form_class = CompatibilidadProductoForm
    template_name = 'compatibilidadProducto/crear.html'

    def get_success_url(self):
        next_param = self.request.POST.get('next') or self.request.GET.get('next')
        if next_param == 'orden':
            return reverse_lazy('app:orden_servicio_create')
        return reverse_lazy('app:listar_compatibilidad')

    def form_valid(self, form):
        messages.success(self.request, 'Compatibilidad registrada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']    = 'Nueva Compatibilidad'
        context['es_editar'] = False
        return context


# ── 3. EDITAR — Solo Admin ────────────────────────────────────────
class CompatibilidadUpdateView(LoginRequiredMixin, SoloAdminMixin, SuccessMessageMixin, UpdateView):
    model = CompatibilidadProducto
    form_class = CompatibilidadProductoForm
    template_name = 'compatibilidadProducto/crear.html'
    success_url = reverse_lazy('app:listar_compatibilidad')
    success_message = 'Compatibilidad actualizada exitosamente.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']    = 'Editar Compatibilidad'
        context['es_editar'] = True
        return context


# ── 4. ELIMINAR — Solo Admin ──────────────────────────────────────
class CompatibilidadDeleteView(LoginRequiredMixin, SoloAdminMixin, View):
    def get(self, request, pk):
        comp = get_object_or_404(CompatibilidadProducto, pk=pk)
        return render(request, 'compatibilidadProducto/eliminar.html', {
            'object':     comp,
            'titulo':     'Eliminar Compatibilidad',
            'listar_url': reverse_lazy('app:listar_compatibilidad'),
        })

    def post(self, request, pk):
        comp = get_object_or_404(CompatibilidadProducto, pk=pk)
        comp.delete()
        messages.success(request, 'Compatibilidad eliminada correctamente.')
        return redirect('app:listar_compatibilidad')


# ── AJAX — accesibles para ambos roles ───────────────────────────

class VerificarCompatibilidadView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request):
        producto_id = request.GET.get('producto')
        marca_id    = request.GET.get('marca')   # ← corregido: era brand_id
        servicio_id = request.GET.get('servicio')

        if not producto_id or not marca_id:
            return JsonResponse({'compatible': None, 'tiene_reglas': False, 'mensaje': ''})

        try:
            producto = Producto.objects.get(pk=producto_id)
        except Producto.DoesNotExist:
            return JsonResponse({'compatible': None, 'tiene_reglas': False, 'mensaje': ''})

        total_reglas = CompatibilidadProducto.objects.filter(producto=producto).count()
        if total_reglas == 0:
            return JsonResponse({'compatible': None, 'tiene_reglas': False, 'mensaje': ''})

        qs = CompatibilidadProducto.objects.filter(producto=producto, marca_vehiculo_id=marca_id)

        if servicio_id and qs.filter(tipo_servicio_id=servicio_id).exists():
            return JsonResponse({
                'compatible':  True,
                'tiene_reglas': True,
                'mensaje': f'✓ {producto.nombre} es compatible con esta marca y este servicio.'
            })

        if qs.filter(tipo_servicio__isnull=True).exists():
            return JsonResponse({
                'compatible':  True,
                'tiene_reglas': True,
                'mensaje': f'✓ {producto.nombre} es compatible con esta marca de vehículo.'
            })

        marcas_ok = list(
            CompatibilidadProducto.objects
            .filter(producto=producto)
            .values_list('marca_vehiculo__nombre', flat=True)
            .distinct()
        )
        marcas_str = ', '.join(marcas_ok) if marcas_ok else 'otras marcas'
        return JsonResponse({
            'compatible':  False,
            'tiene_reglas': True,
            'mensaje': f'⚠ {producto.nombre} no tiene compatibilidad registrada para esta marca. Aplica para: {marcas_str}.'
        })


class ProductosCompatiblesView(LoginRequiredMixin, AdminOMecanicoMixin, View):
    def get(self, request):
        marca_id    = request.GET.get('marca')
        servicio_id = request.GET.get('servicio')

        if not marca_id:
            return JsonResponse({'productos': []})

        qs = CompatibilidadProducto.objects.filter(
            marca_vehiculo_id=marca_id
        ).select_related('producto')

        if servicio_id:
            qs = qs.filter(tipo_servicio_id=servicio_id) | \
                 CompatibilidadProducto.objects.filter(
                     marca_vehiculo_id=marca_id,
                     tipo_servicio__isnull=True
                 ).select_related('producto')

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