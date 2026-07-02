from django.views.generic import TemplateView
from django.db.models import F
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models import Cliente, Vehiculo, Factura, Producto, Proveedor, Notificacion, SeguimientoMantenimiento


def _verificar_mantenimientos():
    """Revisa todos los vehículos a través de sus seguimientos activos."""
    hoy = timezone.now().date()

    seguimientos = SeguimientoMantenimiento.objects.filter(
        activo=True,
        fecha_proximo_mantenimiento__isnull=False
    ).select_related('vehiculo', 'vehiculo__marca', 'vehiculo__cliente')

    for seg in seguimientos:
        vehiculo  = seg.vehiculo
        dias_rest = (seg.fecha_proximo_mantenimiento - hoy).days

        # ── Vencido ──
        if dias_rest <= 0:
            titulo = f"Mantenimiento VENCIDO — {vehiculo.placa}"
            existe = Notificacion.objects.filter(titulo=titulo, leido=False).exists()
            if not existe:
                Notificacion.objects.create(
                    tipo     = 'Urgente',
                    origen   = 'SISTEMA',
                    titulo   = titulo,
                    vehiculo = vehiculo,
                    mensaje  = (
                        f"El vehículo {vehiculo.placa} ({vehiculo.marca.nombre} {vehiculo.modelo}) "
                        f"tiene el mantenimiento VENCIDO. "
                        f"Fecha programada: {seg.fecha_proximo_mantenimiento}."
                    ),
                )
            continue

        # ── Próximo (15 días de anticipación) ──
        if dias_rest <= 15:
            titulo = f"Mantenimiento próximo — {vehiculo.placa}"
            existe = Notificacion.objects.filter(titulo=titulo, leido=False).exists()
            if not existe:
                Notificacion.objects.create(
                    tipo     = 'Mantenimiento',
                    origen   = 'SISTEMA',
                    titulo   = titulo,
                    vehiculo = vehiculo,
                    mensaje  = (
                        f"El vehículo {vehiculo.placa} tiene su mantenimiento próximo. "
                        f"Faltan {dias_rest} días "
                        f"(fecha: {seg.fecha_proximo_mantenimiento})."
                    ),
                )


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    """Dashboard principal — cambia según el rol del usuario"""

    def get_template_names(self):
        user = self.request.user
        if user.cargo == 'MECANICO':
            return ['dashboard/dashboard_mecanico.html']
        return ['dashboard/dashboard.html']

    def get_context_data(self, **kwargs):
        _verificar_mantenimientos()

        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['titulo']               = 'Panel de Control'
        context['total_notificaciones'] = Notificacion.objects.filter(leido=False).count()

        if user.cargo == 'ADMIN':
            context['cant_vehiculos']   = Vehiculo.objects.count()
            context['cant_facturas']    = Factura.objects.count()
            context['cant_clientes']    = Cliente.objects.count()
            context['cant_productos']   = Producto.objects.count()
            context['cant_proveedores'] = Proveedor.objects.count()
            context['stock_bajo']       = Producto.objects.filter(stock__lte=F('stock_minimo')).count()

        if user.cargo == 'MECANICO':
            context['cant_vehiculos']     = Vehiculo.objects.count()
            context['ordenes_pendientes'] = Notificacion.objects.filter(tipo='Mantenimiento', leido=False).count()

        return context