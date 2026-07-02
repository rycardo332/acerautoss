import re
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import Entrada_vehiculo
from app.forms import Entrada_vehiculoForm

# 1. LISTADO DE ENTRADAS
class Entrada_vehiculoListView(ListView):
    model = Entrada_vehiculo
    template_name = 'Entrada_vehiculo/listar.html'
    context_object_name = 'Entrada_vehiculo'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Entrada de Vehículos'
        context['crear_url'] = reverse_lazy('app:crear_entrada_vehiculo')
        return context

# 2. CREAR ENTRADA
class Entrada_vehiculoCreateView(CreateView):
    model = Entrada_vehiculo
    form_class = Entrada_vehiculoForm
    template_name = 'Entrada_vehiculo/crear.html'
    success_url = reverse_lazy('app:listar_entrada_vehiculo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Ingreso'
        context['listar_url'] = reverse_lazy('app:listar_entrada_vehiculo')
        return context

    def form_valid(self, form):
        # Evitamos el AttributeError convirtiendo a string antes de validar
        documento = str(form.cleaned_data.get('documento', ''))
        placa = form.cleaned_data.get('placa', '').upper()

        # Validación de Placa (3 letras y 3 números)
        if not re.match(r'^[A-Z]{3}[0-9]{3}$', placa):
            form.add_error('placa', '¡Error! Formato inválido (Ej: ABC123).')
            return self.form_invalid(form)

        # Validación de longitud de documento
        if len(documento) < 7:
            form.add_error('documento', '¡Error! El documento debe tener al menos 7 dígitos.')
            return self.form_invalid(form)

        messages.success(self.request, "Vehículo registrado con éxito.")
        return super().form_valid(form)

# 3. EDITAR ENTRADA
class Entrada_vehiculoUpdateView(UpdateView):
    model = Entrada_vehiculo
    form_class = Entrada_vehiculoForm
    template_name = 'Entrada_vehiculo/editar.html' 
    success_url = reverse_lazy('app:listar_entrada_vehiculo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Vehículo'
        context['listar_url'] = reverse_lazy('app:listar_entrada_vehiculo')
        return context

    def form_valid(self, form):
        # Validación extra en edición para asegurar consistencia
        documento = str(form.cleaned_data.get('documento', ''))
        if len(documento) < 7:
            form.add_error('documento', '¡Error! El documento debe tener al menos 7 dígitos.')
            return self.form_invalid(form)

        messages.success(self.request, "Datos actualizados correctamente.")
        return super().form_valid(form)

# 4. ELIMINAR ENTRADA (RESTAURADO Y MEJORADO)
class EntradaVehiculoDeleteView(DeleteView):
    model = Entrada_vehiculo
    template_name = 'Entrada_vehiculo/eliminar.html' 
    success_url = reverse_lazy('app:listar_entrada_vehiculo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Registro'
        context['listar_url'] = reverse_lazy('app:listar_entrada_vehiculo')
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Registro eliminado del sistema.")
        return super().delete(request, *args, **kwargs)