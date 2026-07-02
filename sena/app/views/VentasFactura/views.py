from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from app.models import VentasFactura
from app.forms import VentasFacturaForm


class VentasFacturaListView(ListView):
    model = VentasFactura
    template_name = 'VentasFactura/listar.html'
    context_object_name = 'facturas'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Facturas'
        context['crear_url'] = reverse_lazy('app:crear_factura')
        return context
    
class VentasFacturaCreateView(CreateView):
    model = VentasFactura
    form_class = VentasFacturaForm
    template_name = 'VentasFactura/crear.html'
    success_url = reverse_lazy('app:listar_factura')

    # @method_decorator(login_required)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Factura"
        context['listar_url'] = reverse_lazy('app:listar_factura')
        return context

    def form_valid(self, form):
        messages.success(self.request, "Se creó correctamente la factura")
        return super().form_valid(form)
    
class VentasFacturaUpdateView(UpdateView):
    model = VentasFactura
    form_class = VentasFacturaForm
    template_name = 'VentasFactura/crear.html'
    success_url = reverse_lazy('app:listar_factura')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Factura'
        context['listar_url'] = reverse_lazy('app:listar_factura')
        return context

    def form_valid(self, form):
        messages.success(self.request, "Se editó correctamente")
        return super().form_valid(form)
    
    
class VentasFacturaDeleteView(DeleteView):
    model = VentasFactura
    template_name = 'VentasFactura/eliminar.html'
    success_url = reverse_lazy('app:listar_factura')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Factura'
        context['listar_url'] = reverse_lazy('app:listar_factura')
        return context

    def form_valid(self, form):
        messages.success(self.request, "Se eliminó correctamente")
        return super().form_valid(form)
    