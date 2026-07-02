from datetime import timedelta

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.db import connection
from django.utils import timezone

from app.models import DetalleOrdenProducto
from app.forms import DetalleOrdenProductoForm


# ── MIXINS ────────────────────────────────────────────────

class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.cargo == 'ADMIN' or self.request.user.is_superuser
        )
    def handle_no_permission(self):
        messages.error(self.request, "Acceso denegado: Se requieren permisos de administrador.")
        return redirect('app:detalle_orden_list')


class AccesoLecturaTallerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.cargo is not None
    def handle_no_permission(self):
        messages.error(self.request, "Debes ser parte del personal de Acerautos para ver esto.")
        return redirect('app:dashboard')


# ── 1. LISTADO ────────────────────────────────────────────

class DetalleOrdenListView(LoginRequiredMixin, AccesoLecturaTallerMixin, ListView):
    model = DetalleOrdenProducto
    template_name = 'detalle/detalle_orden_list.html'
    context_object_name = 'detalles'

    def get_queryset(self):
        return DetalleOrdenProducto.objects.select_related(
            'orden__vehiculo__marca',
            'producto__marca',
        ).order_by('-orden__id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        total_registros = qs.count()
        total_ordenes   = qs.values('orden').distinct().count()
        total_unidades  = qs.aggregate(t=Sum('cantidad'))['t'] or 0
        total_general   = sum(d.cantidad * d.producto.precio for d in qs)

        # ── Consumo por mes — últimos 6 meses (SQL directo para evitar problema TZ) ──
        # ── Consumo por mes — últimos 6 meses (ORM, compatible con cualquier BD) ──
        from django.db.models.functions import TruncMonth

        hace_6_meses = timezone.now() - timedelta(days=180)
        consumo_qs = (
            DetalleOrdenProducto.objects
            .filter(orden__fecha__gte=hace_6_meses)
            .annotate(mes=TruncMonth('orden__fecha'))
            .values('mes')
            .annotate(total=Sum('cantidad'))
            .order_by('mes')
        )

        MESES_ES = ['', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                    'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        por_mes = []
        for fila in consumo_qs:
            if fila['mes']:
                por_mes.append({
                    'mes':   f"{MESES_ES[fila['mes'].month]} {fila['mes'].year}",
                    'total': fila['total'],
                })

        # ── Top 5 productos más usados ──
        ranking = list(
            DetalleOrdenProducto.objects
            .values('producto__nombre', 'producto__codigo')
            .annotate(veces=Sum('cantidad'))
            .order_by('-veces')[:5]
        )

        context.update({
            'titulo':          'Análisis de Consumo',
            'total_registros': total_registros,
            'total_ordenes':   total_ordenes,
            'total_unidades':  total_unidades,
            'total_general':   total_general,
            'por_mes':         por_mes,
            'ranking':         ranking,
        })
        return context


# ── 2. CREAR ─────────────────────────────────────────────

class DetalleOrdenCreateView(LoginRequiredMixin, SoloAdminMixin, CreateView):
    model = DetalleOrdenProducto
    form_class = DetalleOrdenProductoForm
    template_name = 'detalle/detalle_orden_add.html'
    success_url = reverse_lazy('app:detalle_orden_list')

    def form_valid(self, form):
        try:
            form.instance.full_clean()
            messages.success(self.request, "Producto registrado correctamente.")
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)


# ── 3. EDITAR ────────────────────────────────────────────

class DetalleOrdenUpdateView(LoginRequiredMixin, SoloAdminMixin, UpdateView):
    model = DetalleOrdenProducto
    form_class = DetalleOrdenProductoForm
    template_name = 'detalle/detalle_orden_add.html'
    success_url = reverse_lazy('app:detalle_orden_list')


# ── 4. ELIMINAR ──────────────────────────────────────────

class DetalleOrdenDeleteView(LoginRequiredMixin, SoloAdminMixin, DeleteView):
    model = DetalleOrdenProducto
    template_name = 'detalle/detalle_orden_confirm_delete.html'
    success_url = reverse_lazy('app:detalle_orden_list')