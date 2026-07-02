from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse

from ...models import Compra, CompraDetalle, Caja, ProveedorProducto, Producto
from ...forms import CompraForm, CompraDetalleFormSet


class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador.")
        return redirect('app:dashboard')


class CompraListView(LoginRequiredMixin, SoloAdminMixin, ListView):
    model = Compra
    template_name = 'Compra/listar.html'
    context_object_name = 'compras'

    def get_queryset(self):
        return Compra.objects.prefetch_related('detalles__producto').order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Historial de Compras'
        return context


def _get_proveedor_id(request, instance=None):
    if request.POST.get('proveedor'):
        return request.POST.get('proveedor')
    if instance and instance.pk and instance.proveedor_id:
        return instance.proveedor_id
    return None


class CompraCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'Compra/crear.html'
    success_url = reverse_lazy('app:lista_compras')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar Nueva Compra'
        proveedor_id = _get_proveedor_id(self.request, self.object)
        if self.request.POST:
            context['formset'] = CompraDetalleFormSet(
                self.request.POST,
                instance=self.object,
                form_kwargs={'proveedor_id': proveedor_id},
            )
        else:
            context['formset'] = CompraDetalleFormSet(
                instance=self.object,
                form_kwargs={'proveedor_id': proveedor_id},
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save(commit=False)
            self.object.fecha = timezone.now()
            total = sum(
                (f.cleaned_data.get('cantidad') or 0) * (f.cleaned_data.get('precio_unitario') or 0)
                for f in formset
                if f.cleaned_data and not f.cleaned_data.get('DELETE')
            )
            self.object.total_pagado = total
            self.object.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, "Compra registrada correctamente.")
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class CompraUpdateView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'Compra/crear.html'
    success_url = reverse_lazy('app:lista_compras')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Compra'
        proveedor_id = _get_proveedor_id(self.request, self.object)
        if self.request.POST:
            context['formset'] = CompraDetalleFormSet(
                self.request.POST,
                instance=self.object,
                form_kwargs={'proveedor_id': proveedor_id},
            )
        else:
            context['formset'] = CompraDetalleFormSet(
                instance=self.object,
                form_kwargs={'proveedor_id': proveedor_id},
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save(commit=False)
            self.object.fecha = timezone.now()
            total = sum(
                (f.cleaned_data.get('cantidad') or 0) * (f.cleaned_data.get('precio_unitario') or 0)
                for f in formset
                if f.cleaned_data and not f.cleaned_data.get('DELETE')
            )
            self.object.total_pagado = total
            self.object.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, "Compra actualizada correctamente.")
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class CompraDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Compra
    template_name = 'Compra/eliminar.html'
    success_url = reverse_lazy('app:lista_compras')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Compra'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Compra eliminada correctamente.")
        return super().form_valid(form)


class PagarCompraView(LoginRequiredMixin, SoloAdminMixin, View):
    def post(self, request, pk):
        compra = get_object_or_404(Compra, pk=pk)

        if compra.estado_pago == 'Pagada':
            messages.warning(request, "Esta compra ya fue pagada.")
            return redirect('app:lista_compras')

        metodo = request.POST.get('metodo_pago')
        if not metodo:
            messages.error(request, "Seleccione un método de pago.")
            return redirect('app:lista_compras')

        compra.estado_pago = 'Pagada'
        compra.metodo_pago = metodo
        compra.fecha_pago = timezone.now()
        compra.save()

        # ── Subir stock al pagar ──
        for detalle in compra.detalles.select_related('producto').all():
            detalle.producto.stock += detalle.cantidad
            detalle.producto.save(update_fields=['stock'])

        Caja.objects.create(
            descripcion=f"Compra Factura {compra.num_factura_proveedor}",
            monto=compra.total_pagado,
            tipo='EGRESO',
            categoria='Proveedores',
            metodo_pago=metodo,
        )

        messages.success(request, f"Compra {compra.num_factura_proveedor} pagada correctamente.")
        return redirect('app:lista_compras')


def productos_por_proveedor(request):
    proveedor_id = request.GET.get('proveedor_id')
    if not proveedor_id:
        return JsonResponse({'productos': []})

    items = ProveedorProducto.objects.filter(
        proveedor_id=proveedor_id,
        producto__estado=True
    ).select_related('producto').values('producto_id', 'producto__nombre', 'precio_proveedor')

    data = [
        {
            'id': i['producto_id'],
            'nombre': i['producto__nombre'],
            'precio': str(i['precio_proveedor']),
        }
        for i in items
    ]
    return JsonResponse({'productos': data})