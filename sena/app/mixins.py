from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages


def es_super(user):
    return user.is_authenticated and user.is_superuser

def es_admin(user):
    return user.is_authenticated and (user.is_superuser or user.cargo == 'ADMIN')

def es_mecanico(user):
    return user.is_authenticated and user.cargo == 'MECANICO'


# ── Solo Super Admin ──────────────────────────────────────
class SoloSuperAdminMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not es_super(request.user):
            messages.error(request, 'No tienes permiso para acceder a esta sección.')
            return redirect('app:dashboard')
        return super().dispatch(request, *args, **kwargs)


# ── Admin o Superior ─────────────────────────────────────
class AdminRequeridoMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not es_admin(request.user):
            messages.error(request, 'No tienes permiso para acceder a esta sección.')
            return redirect('app:dashboard')
        return super().dispatch(request, *args, **kwargs)


# ── Solo lectura para Mecánico ────────────────────────────
class SoloLecturaMecanico(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if es_mecanico(request.user) and request.method != 'GET':
            messages.error(request, 'No tienes permiso para realizar esta acción.')
            return redirect('app:dashboard')
        return super().dispatch(request, *args, **kwargs)


# ── Cualquier usuario autenticado ────────────────────────
class LoginRequeridoMixin(LoginRequiredMixin):
    pass