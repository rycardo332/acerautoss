from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models import Categorias
from app.forms import CategoriaForm

# --- LISTADO ---
class categoriaListView(ListView):
    model = Categorias
    template_name = 'categoria/listar.html'
    context_object_name = 'categorias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        context['crear_url'] = reverse_lazy('app:crear_categoria')
        return context

# --- CREAR ---
class CategoriaCreateView(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/crear.html' # Usa el mismo template
    success_url = reverse_lazy('app:listar_categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva Categoría'
        context['listar_url'] = reverse_lazy('app:listar_categoria')
        context['action'] = 'add' # Opcional, por si quieres diferenciar lógica en el HTML
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Categoría guardada correctamente en Acerautos')
        return super().form_valid(form)

# --- EDITAR ---
class CategoriaUpdateView(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/editar.html' # Usa el mismo template que Crear
    success_url = reverse_lazy('app:listar_categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoría'
        context['listar_url'] = reverse_lazy('app:listar_categoria')
        context['action'] = 'edit'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "La categoría se actualizó correctamente")
        return super().form_valid(form)

# --- ELIMINAR ---
class CategoriaDeleteView(DeleteView):
    model = Categorias
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('app:listar_categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Categoría'
        context['listar_url'] = reverse_lazy('app:listar_categoria')
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Categoría eliminada del sistema")
        return super().delete(request, *args, **kwargs)