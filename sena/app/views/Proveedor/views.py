from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.http import JsonResponse

from app.models import Proveedor, Producto
from app.forms import ProveedorForm, ProveedorProductoFormSet


class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para gestionar proveedores.")
        return redirect('app:dashboard')


class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


class ProveedorListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Proveedor
    template_name = 'Proveedor/listar.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Listado de Proveedores'
        context['crear_url']  = reverse_lazy('app:crear_proveedor')
        context['listar_url'] = reverse_lazy('app:listar_proveedores')
        return context


class ProveedorCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crear.html'
    success_url = reverse_lazy('app:listar_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']                = 'Registro de Proveedor'
        context['listar_url']            = reverse_lazy('app:listar_proveedores')
        context['action']                = 'add'
        context['productos_disponibles'] = Producto.objects.filter(estado=True).order_by('nombre')
        if 'formset' not in context:
            context['formset'] = ProveedorProductoFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = ProveedorProductoFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        messages.success(self.request, 'Proveedor creado exitosamente.')
        return redirect(self.success_url)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class ProveedorUpdateView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crear.html'
    success_url = reverse_lazy('app:listar_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']                = 'Editar Proveedor'
        context['listar_url']            = reverse_lazy('app:listar_proveedores')
        context['action']                = 'edit'
        context['productos_disponibles'] = Producto.objects.filter(estado=True).order_by('nombre')
        if 'formset' not in context:
            context['formset'] = ProveedorProductoFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = ProveedorProductoFormSet(request.POST, instance=self.object)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        messages.success(self.request, 'Proveedor actualizado exitosamente.')
        return redirect(self.success_url)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class ProveedorDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Proveedor
    template_name = 'Proveedor/eliminar.html'
    success_url = reverse_lazy('app:listar_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Eliminar Proveedor'
        context['listar_url'] = reverse_lazy('app:listar_proveedores')
        return context

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Proveedor eliminado exitosamente.')
        return self.delete(request, *args, **kwargs)


def validar_nit_proveedor(request):
    valor      = request.GET.get('valor', '').strip()
    exclude_pk = request.GET.get('exclude_pk', None)
    if not valor:
        return JsonResponse({'existe': False})
    qs = Proveedor.objects.filter(nit=valor)
    if exclude_pk:
        qs = qs.exclude(pk=exclude_pk)
    return JsonResponse({'existe': qs.exists()})