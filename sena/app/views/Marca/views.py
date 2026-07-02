from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from app.models import Marca
from app.forms import MarcaForm


class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para gestionar las marcas.")
        return redirect('app:dashboard')


class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


class MarcaListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Marca
    template_name = 'Marca/listar.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Marca.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Listado de Marcas'
        context['crear_url']  = reverse_lazy('app:crear_marca')
        context['listar_url'] = reverse_lazy('app:listar_marca')
        return context


class MarcaCreateView(LoginRequiredMixin, SoloAdminMixin, SuccessMessageMixin, CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('app:listar_marca')
    success_message = 'Marca creada exitosamente.'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['files'] = self.request.FILES
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Registro de Marca'
        context['listar_url'] = reverse_lazy('app:listar_marca')
        context['next']       = self.request.GET.get('next', '')
        context['btn_color']  = 'rojo'      # ← rojo para crear
        context['es_editar']  = False
        return context

    def form_valid(self, form):
        self.object = form.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, 'Marca creada exitosamente.')
        if next_param == 'vehiculos':
            return redirect(reverse_lazy('app:crear_vehiculo'))
        if next_param == 'producto':
            return redirect(reverse_lazy('app:crear_producto'))
        return redirect(self.success_url)


class MarcaUpdateView(LoginRequiredMixin, SoloAdminMixin, SuccessMessageMixin, UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('app:listar_marca')
    success_message = 'Marca actualizada exitosamente.'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['files'] = self.request.FILES
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']     = 'Editar Marca'
        context['listar_url'] = reverse_lazy('app:listar_marca')
        context['next']       = self.request.GET.get('next', '')
        context['btn_color']  = 'azul'      # ← azul para editar
        context['es_editar']  = True
        return context

    def form_valid(self, form):
        self.object = form.save()
        next_param = self.request.POST.get('next', '')
        messages.success(self.request, 'Marca actualizada exitosamente.')
        if next_param == 'vehiculos':
            return redirect(reverse_lazy('app:crear_vehiculo'))
        if next_param == 'producto':
            return redirect(reverse_lazy('app:crear_producto'))
        return redirect(self.success_url)


class MarcaDeleteView(LoginRequiredMixin, SoloAdminMixin, View):
    def get(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        return render(request, 'Marca/eliminar.html', {
            'object':     marca,
            'titulo':     'Eliminar Marca',
            'listar_url': reverse_lazy('app:listar_marca'),
        })

    def post(self, request, pk):
        marca  = get_object_or_404(Marca, pk=pk)
        accion = request.POST.get("accion")

        if accion == "desactivar":
            marca.estado = False
            marca.save()
            messages.success(request, "Marca desactivada correctamente.")
        else:
            try:
                marca.delete()
                messages.success(request, "Marca eliminada definitivamente.")
            except ProtectedError:
                messages.error(request,
                    f"No se puede eliminar '{marca.nombre}' porque está siendo usada "
                    f"por vehículos o productos registrados en el sistema. "
                    f"Primero elimina o reasigna esos registros."
                )
                return redirect('app:listar_marca')

        return redirect('app:listar_marca')


@require_POST
def crear_marca_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Sesión expirada.'})
    if request.user.cargo not in ('ADMIN', 'MECANICO') and not request.user.is_superuser:
        return JsonResponse({'success': False, 'error': 'No tienes permisos para crear marcas.'})

    nombre = request.POST.get('nombre', '').strip()
    pais   = request.POST.get('pais_origen', '').strip()
    desc   = request.POST.get('descripcion', '').strip()

    if not nombre:
        return JsonResponse({'success': False, 'error': 'El nombre es obligatorio.'})
    if len(nombre) < 2:
        return JsonResponse({'success': False, 'error': 'El nombre debe tener al menos 2 caracteres.'})
    if Marca.objects.filter(nombre__iexact=nombre).exists():
        return JsonResponse({'success': False, 'error': f'La marca "{nombre}" ya existe en el sistema.'})

    marca = Marca.objects.create(
        nombre      = nombre,
        pais_origen = pais or None,
        descripcion = desc or None,
    )
    return JsonResponse({'success': True, 'id': marca.pk, 'nombre': marca.nombre})