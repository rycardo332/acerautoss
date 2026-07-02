
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from app.models import UsuarioSistema
from app.forms import UsuarioSistemaForm          # ← ya existía, la reutilizamos
from app.mixins import AdminRequeridoMixin


class EmpleadoListView(AdminRequeridoMixin, ListView):
    model                = UsuarioSistema
    template_name        = 'Empleado/listar.html'      # ← mismo template, solo cambia el objeto
    context_object_name  = 'object_list'
    login_url            = 'login:login'

    def get_queryset(self):
        # Solo mecánicos y admins activos, ordenados por nombre
        return UsuarioSistema.objects.filter(
            activo=True
        ).order_by('first_name', 'last_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']    = 'Listado de Empleados'
        context['crear_url'] = reverse_lazy('app:crear_empleado')
        return context


class EmpleadoCreateView(AdminRequeridoMixin, CreateView):
    model         = UsuarioSistema
    form_class    = UsuarioSistemaForm
    template_name = 'Empleado/crear_empleado.html'
    success_url   = reverse_lazy('app:listar_empleado')
    login_url     = 'login:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Registrar Empleado'
        context['listar_url'] = reverse_lazy('app:listar_empleado')
        context['es_editar']  = False
        context['next']       = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        # Forzar activo=True al crear desde este módulo
        usuario = form.save(commit=False)
        usuario.activo = True
        usuario.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, f'Empleado "{usuario.nombre_completo}" registrado correctamente.')
        if next_param == 'orden':
            return redirect(reverse_lazy('app:orden_servicio_create'))
        return redirect(self.success_url)


class EmpleadoUpdateView(AdminRequeridoMixin, UpdateView):
    model         = UsuarioSistema
    form_class    = UsuarioSistemaForm
    template_name = 'Empleado/crear_empleado.html'
    success_url   = reverse_lazy('app:listar_empleado')
    login_url     = 'login:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Editar Empleado'
        context['listar_url'] = reverse_lazy('app:listar_empleado')
        context['es_editar']  = True
        context['next']       = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        usuario    = form.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, f'Empleado "{usuario.nombre_completo}" actualizado correctamente.')
        if next_param == 'orden':
            return redirect(reverse_lazy('app:orden_servicio_create'))
        return redirect(self.success_url)


class EmpleadoDeleteView(AdminRequeridoMixin, DeleteView):
    model         = UsuarioSistema
    template_name = 'Empleado/eliminar.html'
    success_url   = reverse_lazy('app:listar_empleado')
    login_url     = 'login:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Eliminar Empleado'
        context['listar_url'] = reverse_lazy('app:listar_empleado')
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Empleado eliminado correctamente.')
        return super().form_valid(form)