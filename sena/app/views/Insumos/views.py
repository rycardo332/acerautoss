from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models import insumo
from app.forms import InsumoForm
from django.contrib import messages


class InsumoListView(ListView):
    model = insumo
    template_name = 'Insumo/listar.html'
    context_object_name = 'insumo'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Insumos'
        context['crear_url'] = reverse_lazy('app:crear_insumo')
        return context


class InsumoCreateView(CreateView):
    model = insumo
    form_class = InsumoForm
    template_name = 'Insumo/crear.html'
    success_url = reverse_lazy('app:listar_insumo')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Insumo'
        context['listar_url'] = reverse_lazy('app:listar_insumo')
        return context
    #mensajes de confirmacion
    def form_valid(self, form):
        messages.success(self.request,'Se creo un nuevo insumo')
        return super().form_valid(form)


class InsumoUpdateView(UpdateView):
    model = insumo
    form_class = InsumoForm
    template_name = 'Insumo/editar.html'
    success_url = reverse_lazy('app:listar_insumo')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Insumo'
        context['listar_url'] = reverse_lazy('app:listar_insumo')
        return context
    
    #mensajes de confirmacion
    def form_valid(self, form):
        messages.success(self.request,'Se edito el insumo')
        return super().form_valid(form)


class InsumoDeleteView(DeleteView):
    model = insumo
    template_name = 'Insumo/eliminar.html'
    success_url = reverse_lazy('app:listar_insumo')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Insumo'
        context['listar_url'] = reverse_lazy('app:listar_insumo')
        return context
    
    #mensajes de confirmacion
    def form_valid(self, form):
        messages.success(self.request,'Se elimino el insumo')
        return super().form_valid(form)

