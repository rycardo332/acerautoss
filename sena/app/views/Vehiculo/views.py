from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from app.models import Vehiculo, Notificacion, SeguimientoMantenimiento
from app.forms import VehiculoForm


# ── Mixin 1: Solo ADMIN ──────────────────────────────────────────
class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para realizar esta acción.")
        return redirect('app:dashboard')

# ── Mixin 2: ADMIN o MECANICO ────────────────────────────────────
class AdminOMecanicoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo in ('ADMIN', 'MECANICO') or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a este módulo.")
        return redirect('app:dashboard')


# ── GENERAR ALERTAS (sin cambios) ────────────────────────────────
def generar_alertas_mantenimiento():
    hoy = date.today()
    seguimientos = SeguimientoMantenimiento.objects.filter(
        activo=True,
        fecha_proximo_mantenimiento__isnull=False
    ).select_related('vehiculo')

    for seg in seguimientos:
        v        = seg.vehiculo
        dias_para = (seg.fecha_proximo_mantenimiento - hoy).days

        if dias_para <= 0:
            estado = 'vencido'
        elif dias_para <= 15:
            estado = 'alerta'
        else:
            continue

        titulo = (
            f"Mantenimiento VENCIDO — {v.placa}"
            if estado == 'vencido'
            else f"Mantenimiento PRÓXIMO — {v.placa}"
        )

        ya_existe = Notificacion.objects.filter(
            vehiculo=v, tipo='Mantenimiento',
            origen='SISTEMA', leido=False, titulo=titulo
        ).exists()

        if not ya_existe:
            msg = (
                f"El vehículo {v.placa} superó la fecha límite ({seg.fecha_proximo_mantenimiento})."
                if estado == 'vencido'
                else f"El vehículo {v.placa} tiene su próximo servicio el "
                     f"{seg.fecha_proximo_mantenimiento} ({dias_para} días restantes)."
            )
            Notificacion.objects.create(
                tipo='Mantenimiento', origen='SISTEMA', leido=False,
                vehiculo=v, titulo=titulo, mensaje=msg,
            )


# ── 1. LISTADO — Mecánico puede ver ──────────────────────────────
class VehiculoListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model = Vehiculo
    template_name = 'vehiculo/listar.html'
    context_object_name = 'vehiculos'

    def get_queryset(self):
        return Vehiculo.objects.select_related('marca', 'cliente').prefetch_related('seguimientos').all()

    def get_context_data(self, **kwargs):
        generar_alertas_mantenimiento()
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Vehículos'

        hoy = date.today()
        vehiculos_con_estado = []

        for v in context['vehiculos']:
            seg    = v.seguimiento_activo()
            dias   = None
            estado = 'sin_datos'

            if seg and seg.fecha_proximo_mantenimiento:
                dias = (seg.fecha_proximo_mantenimiento - hoy).days
                if dias <= 0:
                    estado = 'vencido'
                elif dias <= 15:
                    estado = 'alerta'
                else:
                    estado = 'ok'

            vehiculos_con_estado.append({
                'vehiculo':       v,
                'seguimiento':    seg,
                'dias_restantes': dias,
                'estado_mant':    estado,
            })

        context['vehiculos_con_estado'] = vehiculos_con_estado
        context['total_vencidos'] = sum(1 for x in vehiculos_con_estado if x['estado_mant'] == 'vencido')
        context['total_alertas']  = sum(1 for x in vehiculos_con_estado if x['estado_mant'] == 'alerta')
        return context


OPCIONES_USO = [
    {'val': 'BAJO',   'label': 'Uso Bajo',   'img': 'ciudadvehiculo.jpeg', 'desc': '~30 km/día'},
    {'val': 'NORMAL', 'label': 'Uso Normal',  'img': 'vehiculoo.jpeg',     'desc': '~50 km/día'},
    {'val': 'ALTO',   'label': 'Uso Alto',    'img': 'viajevehiculo.jpeg', 'desc': '~80 km/día'},
    {'val': 'CARGA',  'label': 'Carga',       'img': 'carga.jpeg',         'desc': '~120 km/día'},
]

# ── 2. CREAR — Mecánico puede crear ──────────────────────────────
class VehiculoCreateView(LoginRequiredMixin, AdminOMecanicoMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/crear.html'
    success_url = reverse_lazy('app:listar_vehiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']       = 'Registrar Nuevo Vehículo'
        context['es_editar']    = False
        context['next']         = self.request.GET.get('next', '')
        context['opciones_uso'] = OPCIONES_USO
        return context

    def form_valid(self, form):
        vehiculo = form.save()
        messages.success(self.request, f'Vehículo {vehiculo.placa} registrado con éxito.')
        if self.request.POST.get('next', '') == 'orden':
            return redirect('app:orden_servicio_create')
        return redirect(self.success_url)


# ── 3. EDITAR — Mecánico puede editar ────────────────────────────
class VehiculoUpdateView(LoginRequiredMixin, AdminOMecanicoMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/crear.html'
    success_url = reverse_lazy('app:listar_vehiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']       = 'Editar Vehículo'
        context['es_editar']    = True
        context['next']         = self.request.GET.get('next', '')
        context['opciones_uso'] = OPCIONES_USO
        return context

    def form_valid(self, form):
        vehiculo = form.save()
        messages.success(self.request, f'Vehículo {vehiculo.placa} actualizado correctamente.')
        if self.request.POST.get('next', '') == 'orden':
            return redirect('app:orden_servicio_create')
        return redirect(self.success_url)


# ── 4. ELIMINAR — Solo Admin ──────────────────────────────────────
class VehiculoDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/eliminar.html'
    success_url = reverse_lazy('app:listar_vehiculos')

    def form_valid(self, form):
        messages.success(self.request, 'El vehículo ha sido eliminado del sistema.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Vehículo'
        return context