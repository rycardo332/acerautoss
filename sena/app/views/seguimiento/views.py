from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from app.models import SeguimientoMantenimiento, Vehiculo


# ── Intervalos de cambio de aceite según tipo de uso ──────────────
INTERVALOS_ACEITE = {
    'BAJO':   180,
    'NORMAL': 120,
    'ALTO':   90,
    'CARGA':  60,
}

def calcular_fecha_sugerida(vehiculo):
    dias = INTERVALOS_ACEITE.get(vehiculo.tipo_uso, 120)
    return timezone.now().date() + timedelta(days=dias)


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


# ── LISTAR — Mecánico puede ver ──────────────────────────────────
class SeguimientoListView(LoginRequiredMixin, AdminOMecanicoMixin, ListView):
    model               = SeguimientoMantenimiento
    template_name       = 'seguimiento/seguimiento_list.html'
    context_object_name = 'seguimientos'

    def get_queryset(self):
        return SeguimientoMantenimiento.objects.select_related(
            'vehiculo__marca', 'vehiculo__cliente',
            'orden_servicio', 'tipo_servicio',
        ).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        qs_activos = list(qs.filter(activo=True))
        total_ok = total_alerta = total_vencidos = 0
        for s in qs_activos:
            estado = s.estado_calculado()
            if estado == 'ok':        total_ok += 1
            elif estado == 'alerta':  total_alerta += 1
            elif estado == 'vencido': total_vencidos += 1

        seguimientos_con_estado = []
        for s in qs:
            s.estado_calc = s.estado_calculado()
            seguimientos_con_estado.append(s)

        context['seguimientos'] = seguimientos_con_estado
        context.update({
            'titulo':         'Seguimientos de Mantenimiento',
            'total_ok':       total_ok,
            'total_alertas':  total_alerta,
            'total_vencidos': total_vencidos,
        })
        return context


# ── CREAR — Mecánico puede crear ─────────────────────────────────
class SeguimientoCreateView(LoginRequiredMixin, AdminOMecanicoMixin, CreateView):
    model         = SeguimientoMantenimiento
    template_name = 'seguimiento/seguimiento_form.html'
    success_url   = reverse_lazy('app:seguimiento_list')
    fields        = ['vehiculo', 'orden_servicio', 'tipo_servicio', 'km_al_momento',
                     'fecha_proximo_mantenimiento', 'estado', 'activo', 'observaciones']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from app.models import OrdenServicio, TipoServicio
        form.fields['vehiculo'].queryset       = Vehiculo.objects.select_related('marca', 'cliente').order_by('placa')
        form.fields['orden_servicio'].queryset = OrdenServicio.objects.select_related('vehiculo').order_by('-id')
        form.fields['orden_servicio'].required = False
        form.fields['tipo_servicio'].queryset  = TipoServicio.objects.filter(estado=True)
        form.fields['tipo_servicio'].required  = False
        return form

    def form_valid(self, form):
        seg = form.instance

        if not seg.fecha_proximo_mantenimiento and seg.vehiculo:
            seg.fecha_proximo_mantenimiento = calcular_fecha_sugerida(seg.vehiculo)

        if seg.activo:
            SeguimientoMantenimiento.objects.filter(
                vehiculo=seg.vehiculo, activo=True
            ).update(activo=False)

        messages.success(self.request, "Seguimiento registrado correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'titulo': 'Nuevo Seguimiento', 'accion': 'Registrar', 'es_editar': False})
        return context


# ── EDITAR — Mecánico puede editar ───────────────────────────────
class SeguimientoUpdateView(LoginRequiredMixin, AdminOMecanicoMixin, UpdateView):
    model         = SeguimientoMantenimiento
    template_name = 'seguimiento/seguimiento_form.html'
    success_url   = reverse_lazy('app:seguimiento_list')
    fields        = ['fecha_proximo_mantenimiento', 'observaciones', 'activo']

    def form_valid(self, form):
        from app.models import Notificacion
        seg = form.instance
        hoy = timezone.now().date()

        if not seg.fecha_proximo_mantenimiento and seg.vehiculo:
            seg.fecha_proximo_mantenimiento = calcular_fecha_sugerida(seg.vehiculo)

        Notificacion.objects.filter(
            vehiculo=seg.vehiculo,
            origen='SISTEMA',
            fecha=hoy,
        ).delete()

        messages.success(self.request, "Seguimiento actualizado correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        seg = self.object
        fecha_sugerida = None
        if seg.vehiculo:
            fecha_sugerida = calcular_fecha_sugerida(seg.vehiculo)
            intervalo_dias = INTERVALOS_ACEITE.get(seg.vehiculo.tipo_uso, 120)
        else:
            intervalo_dias = 120

        context.update({
            'titulo':         'Editar Seguimiento',
            'accion':         'Guardar cambios',
            'es_editar':      True,
            'fecha_sugerida': fecha_sugerida,
            'intervalo_dias': intervalo_dias,
            'tipo_uso_display': seg.vehiculo.get_tipo_uso_display() if seg.vehiculo else '',
        })
        return context


# ── ELIMINAR — Solo Admin ─────────────────────────────────────────
class SeguimientoDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model         = SeguimientoMantenimiento
    template_name = 'seguimiento/seguimiento_confirm_delete.html'
    success_url   = reverse_lazy('app:seguimiento_list')

    def form_valid(self, form):
        messages.success(self.request, "Seguimiento eliminado.")
        return super().form_valid(form)


# ── COMPLETAR — Solo Admin ────────────────────────────────────────
class SeguimientoCompletarView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model       = SeguimientoMantenimiento
    fields      = []
    success_url = reverse_lazy('app:seguimiento_list')

    def form_valid(self, form):
        seg        = form.instance
        seg.estado = 'Completado'
        seg.activo = False
        seg.save()
        messages.success(self.request, f"Seguimiento #{seg.pk} marcado como completado.")
        return redirect(self.success_url)


# ── AJAX — accesible para ambos roles ─────────────────────────────
def get_servicios_orden(request):
    if not request.user.is_authenticated:
        return JsonResponse({'servicios': [], 'km_orden': None, 'fecha_sugerida': None}, status=403)
    if request.user.cargo not in ('ADMIN', 'MECANICO') and not request.user.is_superuser:
        return JsonResponse({'servicios': [], 'km_orden': None, 'fecha_sugerida': None}, status=403)

    orden_id = request.GET.get('orden_id')
    if not orden_id:
        return JsonResponse({'servicios': [], 'km_orden': None, 'fecha_sugerida': None})
    try:
        from app.models import OrdenServicio
        orden    = OrdenServicio.objects.select_related('vehiculo').get(pk=orden_id)
        servicios = list(orden.servicios.values('id', 'nombre'))

        fecha_sugerida  = None
        intervalo_label = None
        if orden.vehiculo:
            dias = INTERVALOS_ACEITE.get(orden.vehiculo.tipo_uso, 120)
            fecha_sugerida  = (timezone.now().date() + timedelta(days=dias)).isoformat()
            intervalo_label = f"{orden.vehiculo.get_tipo_uso_display()} → cada {dias} días (~{dias//30} meses)"

        return JsonResponse({
            'servicios':       servicios,
            'km_orden':        orden.km_actual,
            'fecha_sugerida':  fecha_sugerida,
            'intervalo_label': intervalo_label,
        })
    except OrdenServicio.DoesNotExist:
        return JsonResponse({'servicios': [], 'km_orden': None, 'fecha_sugerida': None})