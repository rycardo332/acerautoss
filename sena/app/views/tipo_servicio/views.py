from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from app.models import TipoServicio
from app.forms import TipoServicioForm


# ── Mixin 1: Solo ADMIN ──────────────────────────────────────────
class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para gestionar los servicios.")
        return redirect('app:dashboard')

# ── Mixin 2: ADMIN o MECANICO ────────────────────────────────────
class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


# ── 1. LISTADO — Mecánico puede ver ──────────────────────────────
class TipoServicioListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = TipoServicio
    template_name = 'TipoServicio/listar.html'
    context_object_name = 'servicios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']        = 'Listado de Tipos de Servicio'
        context['crear_url']     = reverse_lazy('app:create_servico')
        context['total_activos'] = TipoServicio.objects.filter(estado=True).count()
        return context


# ── 2. CREAR — Solo Admin ─────────────────────────────────────────
class TipoServicioCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model         = TipoServicio
    form_class    = TipoServicioForm
    template_name = 'TipoServicio/crear.html'
    success_url   = reverse_lazy('app:tipo_servicio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Crear Tipo de Servicio'
        context['listar_url'] = reverse_lazy('app:tipo_servicio_list')
        context['es_editar']  = False
        context['next']       = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Tipo de servicio creado exitosamente en Acerautos.')
        if self.request.POST.get('next', '') == 'orden':
            return redirect(reverse_lazy('app:orden_servicio_create'))
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al guardar. Por favor verifica los campos.')
        return super().form_invalid(form)


# ── 3. EDITAR — Solo Admin ────────────────────────────────────────
class TipoServicioUpdateView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model         = TipoServicio
    form_class    = TipoServicioForm
    template_name = 'TipoServicio/crear.html'
    success_url   = reverse_lazy('app:tipo_servicio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Editar Tipo de Servicio'
        context['listar_url'] = reverse_lazy('app:tipo_servicio_list')
        context['es_editar']  = True
        context['next']       = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Tipo de servicio actualizado exitosamente.')
        if self.request.POST.get('next', '') == 'orden':
            return redirect(reverse_lazy('app:orden_servicio_create'))
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar. Por favor verifica los campos.')
        return super().form_invalid(form)


# ── 4. ELIMINAR — Solo Admin ──────────────────────────────────────
class TipoServicioDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model         = TipoServicio
    template_name = 'TipoServicio/eliminar.html'
    success_url   = reverse_lazy('app:tipo_servicio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Eliminar Tipo de Servicio'
        context['listar_url'] = reverse_lazy('app:tipo_servicio_list')
        return context

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre
            self.object.delete()
            messages.success(request, f'El servicio "{nombre}" fue eliminado exitosamente.')
            return redirect(self.success_url)
        except ProtectedError:
            nombre = self.get_object().nombre
            messages.error(
                request,
                f'No se puede eliminar "{nombre}" porque tiene órdenes de servicio asociadas. '
                f'Elimina primero esas órdenes e intenta de nuevo.'
            )
            return redirect('app:tipo_servicio_list')