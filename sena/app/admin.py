from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    UsuarioSistema,
    Proveedor, Producto, Compra, Cliente,
    Marca, Vehiculo, TipoServicio, OrdenServicio,
    DetalleOrdenProducto, CompatibilidadProducto,
    Factura, Notificacion, Caja,
    SeguimientoMantenimiento,
)


# ══════════════════════════════════════════════════════════
#  USUARIO SISTEMA
# ══════════════════════════════════════════════════════════
@admin.register(UsuarioSistema)
class UsuarioSistemaAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos del taller', {
            'fields': ('tipo_documento', 'cedula', 'telefono', 'cargo', 'activo')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos del taller', {
            'fields': ('tipo_documento', 'cedula', 'telefono', 'cargo', 'activo')
        }),
    )
    list_display  = ('username', 'email', 'first_name', 'last_name', 'cargo', 'activo', 'is_active')
    list_filter   = ('cargo', 'activo', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'cedula')


# ══════════════════════════════════════════════════════════
#  RESTO DE MODELOS
# ══════════════════════════════════════════════════════════
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Vehiculo)
admin.site.register(TipoServicio)
admin.site.register(OrdenServicio)
admin.site.register(DetalleOrdenProducto)
admin.site.register(CompatibilidadProducto)
admin.site.register(Factura)
admin.site.register(Notificacion)
admin.site.register(Caja)
admin.site.register(SeguimientoMantenimiento)