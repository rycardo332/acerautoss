from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from app.models import Cliente
from app.forms import ClienteForm
from django.http import JsonResponse
# MIXIN PERSONALIZADO PARA ADMINISTRADORES
class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para realizar esta acción.")
        return redirect('app:dashboard')

# ── Mixin 2: ADMIN o MECANICO (usuarios autenticados con cargo válido) ──
class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')

# ── 1. LISTADO — Mecánico puede ver ──────────────────────────────
class ClienteListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Cliente
    template_name = 'cliente/listar.html'
    context_object_name = 'clientes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        return context

# ── 2. CREAR — Mecánico puede crear ──────────────────────────────
class ClienteCreateView(LoginRequiredMixin, AdminOMecanicoMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:listar_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']    = 'Registrar Nuevo Cliente'
        context['es_editar'] = False
        context['next']      = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        self.object = form.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, 'Cliente registrado con éxito en Acerautos.')
        if next_param == 'orden':
            return redirect(reverse_lazy('app:crear_vehiculo'))
        return redirect(self.success_url)

# ── 3. EDITAR — Mecánico puede editar ────────────────────────────
class ClienteUpdateView(LoginRequiredMixin, AdminOMecanicoMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:listar_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']    = 'Editar Datos del Cliente'
        context['es_editar'] = True
        context['next']      = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        self.object = form.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, 'Datos del cliente actualizados correctamente.')
        if next_param == 'orden':
            return redirect(reverse_lazy('app:orden_servicio_create'))
        return redirect(self.success_url)

# ── 4. ELIMINAR — Solo Admin ──────────────────────────────────────
class ClienteDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('app:listar_clientes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'El cliente ha sido eliminado del sistema.')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Cliente'
        return context
# ══════════════════════════════════════════════════════════
#  AGREGAR AL FINAL DE views/Cliente/views.py
# ══════════════════════════════════════════════════════════


def validar_documento_cliente(request):
    """
    GET /clientes/validar-documento/?valor=12345&exclude_pk=5
    Devuelve {"existe": true/false}
    """
    valor      = request.GET.get('valor', '').strip()
    exclude_pk = request.GET.get('exclude_pk', None)
    if not valor:
        return JsonResponse({'existe': False})
    qs = Cliente.objects.filter(numero_documento=valor)
    if exclude_pk:
        qs = qs.exclude(pk=exclude_pk)
    return JsonResponse({'existe': qs.exists()})


def validar_email_cliente(request):
    """
    GET /clientes/validar-email/?valor=correo@x.com&exclude_pk=5
    Devuelve {"existe": true/false}
    """
    valor      = request.GET.get('valor', '').strip().lower()
    exclude_pk = request.GET.get('exclude_pk', None)
    if not valor:
        return JsonResponse({'existe': False})
    qs = Cliente.objects.filter(email__iexact=valor)
    if exclude_pk:
        qs = qs.exclude(pk=exclude_pk)
    return JsonResponse({'existe': qs.exists()})