from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

User = get_user_model()

from .models import PerfilUsuario
from .forms import UserForm, PerfilForm, UserEditForm


#  LISTAR USUARIOS
class ListarUsuariosView(ListView):
    model               = User
    template_name       = 'usuario/listar.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False).select_related('perfil')


#  CREAR USUARIO
class CrearUsuarioView(View):
    def get(self, request):
        context = {
            'titulo'      : 'Crear Nuevo Usuario',
            'user_form'   : UserForm(),
            'perfil_form' : PerfilForm(),
        }
        return render(request, 'usuario/crear.html', context)

    def post(self, request):
        user_form   = UserForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil      = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('usuario:listar')

        context = {
            'titulo'      : 'Crear Nuevo Usuario',
            'user_form'   : user_form,
            'perfil_form' : perfil_form,
        }
        return render(request, 'usuario/crear.html', context)


#  EDITAR USUARIO
class EditarUsuarioView(View):
    def get(self, request, pk):
        usuario         = get_object_or_404(User, pk=pk)
        perfil, created = PerfilUsuario.objects.get_or_create(user=usuario)

        context = {
            'titulo'      : 'Editar Usuario',
            'user_form'   : UserEditForm(instance=usuario),
            'perfil_form' : PerfilForm(instance=perfil),
            'object'      : usuario,
        }
        return render(request, 'usuario/editar.html', context)

    def post(self, request, pk):
        usuario     = get_object_or_404(User, pk=pk)
        perfil      = get_object_or_404(PerfilUsuario, user=usuario)

        user_form   = UserEditForm(request.POST, instance=usuario)
        perfil_form = PerfilForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user           = user_form.save(commit=False)
            nueva_password = user_form.cleaned_data.get('password')
            if nueva_password:
                user.set_password(nueva_password)
            user.save()
            perfil_form.save()

            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('usuario:listar')

        context = {
            'titulo'      : 'Editar Usuario',
            'user_form'   : user_form,
            'perfil_form' : perfil_form,
            'object'      : usuario,
        }
        return render(request, 'usuario/editar.html', context)


#  ELIMINAR USUARIO
class EliminarUsuarioView(View):
    def get(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        context = {
            'titulo'     : 'Desactivar Usuario',
            'object'     : usuario,
            'listar_url' : reverse_lazy('usuario:listar'),
        }
        return render(request, 'usuario/eliminar.html', context)

    def post(self, request, pk):
        usuario           = get_object_or_404(User, pk=pk)
        usuario.is_active = False
        usuario.save()

        messages.success(request, 'Usuario desactivado correctamente.')
        return redirect('usuario:listar')


#  CAMBIAR ESTADO
@method_decorator(csrf_protect, name='dispatch')
class CambiarEstadoUsuarioView(View):
    def post(self, request, pk):
        usuario           = get_object_or_404(User, pk=pk)
        usuario.is_active = not usuario.is_active
        usuario.save()

        estado = "activado" if usuario.is_active else "desactivado"
        messages.success(request, f'Usuario {estado} correctamente.')
        return redirect('usuario:listar')