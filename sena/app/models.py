from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum, F, DecimalField


# ══════════════════════════════════════════════════════════
#  USUARIO SISTEMA
# ══════════════════════════════════════════════════════════
class UsuarioSistema(AbstractUser):
    CARGOS = [
        ('ADMIN',    'Administrador'),
        ('MECANICO', 'Mecánico'),
    ]
    TIPOS_DOC = [
        ('CC',  'Cédula de Ciudadanía'),
        ('CE',  'Cédula de Extranjería'),
        ('PAS', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=3, choices=TIPOS_DOC, default='CC')
    cedula         = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono       = models.CharField(max_length=20, null=True, blank=True)
    cargo          = models.CharField(max_length=20, choices=CARGOS, default='ADMIN')
    activo         = models.BooleanField(default=True)
    foto           = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    debe_cambiar_password = models.BooleanField(
        default=False,
        help_text="Si está activo, el usuario deberá cambiar su contraseña al iniciar sesión."
    )
    
    @property
    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

    @property
    def inicial(self):
        return (self.first_name[0] if self.first_name else self.username[0]).upper()

    def __str__(self):
        return self.nombre_completo

    class Meta:
        db_table     = 'usuario_sistema'
        verbose_name = 'Usuario del Sistema'


# ══════════════════════════════════════════════════════════
#  MARCA
# ══════════════════════════════════════════════════════════
class Marca(models.Model):
    CATEGORIAS = [
        ('AUTO',     'Marca de Vehículo'),
        ('REPUESTO', 'Marca de Repuesto/Aceite'),
    ]
    nombre         = models.CharField(max_length=50)
    categoria      = models.CharField(max_length=10, choices=CATEGORIAS, default='AUTO')
    pais_origen    = models.CharField(max_length=50, blank=True, null=True)
    logo           = models.ImageField(upload_to='marcas_logos/', blank=True, null=True)
    descripcion    = models.TextField(blank=True, null=True)
    estado         = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"

    class Meta:
        db_table = 'marca'


# ══════════════════════════════════════════════════════════
#  CAJA
# ══════════════════════════════════════════════════════════
class Caja(models.Model):
    TIPOS = [('INGRESO', 'Ingreso (+)'), ('EGRESO', 'Egreso (-)')]
    CATEGORIAS = [
        ('Ventas',            'Ventas'),
        ('Servicios',         'Servicios'),
        ('Anticipos',         'Anticipos de clientes'),
        ('Arriendo',          'Arriendo'),
        ('ServiciosPublicos', 'Servicios públicos'),
        ('Proveedores',       'Pago a proveedores'),
        ('Nomina',            'Nómina / Salarios'),
        ('Mantenimiento',     'Mantenimiento'),
        ('Otros',             'Otros'),
    ]
    METODOS_PAGO = [
        ('Efectivo',       'Efectivo'),
        ('Transferencia',  'Transferencia bancaria'),
        ('TarjetaDebito',  'Tarjeta débito'),
        ('TarjetaCredito', 'Tarjeta crédito'),
        ('Cheque',         'Cheque'),
        ('Nequi',          'Nequi'),
        ('Daviplata',      'Daviplata'),
    ]
    descripcion   = models.CharField(max_length=255)
    monto         = models.DecimalField(max_digits=12, decimal_places=2)
    tipo          = models.CharField(max_length=10, choices=TIPOS)
    fecha         = models.DateTimeField(default=timezone.now)
    categoria     = models.CharField(max_length=20, choices=CATEGORIAS, default='Otros')
    metodo_pago   = models.CharField(max_length=20, choices=METODOS_PAGO, default='Efectivo')
    comprobante   = models.FileField(upload_to='caja_comprobantes/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} | {self.descripcion} | ${self.monto}"

    class Meta:
        db_table = 'caja'


# ══════════════════════════════════════════════════════════
#  PROVEEDOR
# ══════════════════════════════════════════════════════════
class Proveedor(models.Model):
    nombre    = models.CharField(max_length=100)
    nit       = models.CharField(max_length=20, unique=True)
    telefono  = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150, blank=True)
    activo    = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedor'

# ══════════════════════════════════════════════════════════
#  CATÁLOGO PROVEEDOR-PRODUCTO
# ══════════════════════════════════════════════════════════
class ProveedorProducto(models.Model):
    proveedor        = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='catalogo')
    producto         = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='proveedores')
    precio_proveedor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.proveedor.nombre} → {self.producto.nombre} (${self.precio_proveedor:,.0f})"

    class Meta:
        db_table        = 'proveedor_producto'
        unique_together = ('proveedor', 'producto')
        verbose_name    = 'Producto del Proveedor'



# ══════════════════════════════════════════════════════════
#  PRODUCTO
# ══════════════════════════════════════════════════════════
class Producto(models.Model):
    UNIDADES = [
        ('UND', 'Unidad'),  ('LT',  'Litro'),      ('ML',  'Mililitro'),
        ('KG',  'Kilogramo'), ('GR', 'Gramo'),      ('MT',  'Metro'),
        ('CM',  'Centímetro'), ('GL', 'Galón'),     ('PAR', 'Par'),
        ('KIT', 'Kit'),     ('CJA', 'Caja'),        ('RLL', 'Rollo'),
        ('JGO', 'Juego'),
    ]
    nombre        = models.CharField(max_length=100, unique=True)
    marca         = models.ForeignKey(Marca, on_delete=models.PROTECT, limit_choices_to={'categoria': 'REPUESTO', 'estado': True})
    descripcion   = models.TextField(blank=True, null=True)
    precio        = models.DecimalField(max_digits=10, decimal_places=2)
    stock         = models.PositiveIntegerField(default=0)
    stock_minimo  = models.PositiveIntegerField(default=0)
    codigo        = models.CharField(max_length=20, unique=True)
    unidad_medida = models.CharField(max_length=5, choices=UNIDADES, default='UND', verbose_name='Unidad de medida')
    imagen        = models.ImageField(upload_to='productos/', blank=True, null=True)
    estado        = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} | Stock: {self.stock}"

    class Meta:
        db_table = 'producto'


# ══════════════════════════════════════════════════════════
#  TIPO SERVICIO
# ══════════════════════════════════════════════════════════
class TipoServicio(models.Model):
    nombre               = models.CharField(max_length=100, unique=True)
    descripcion          = models.TextField(blank=True, null=True)
    precio_mano_obra     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado               = models.BooleanField(default=True)
    requiere_seguimiento = models.BooleanField(
        default=False,
        help_text="Si está activo, al crear una orden con este servicio se pedirá la fecha del próximo mantenimiento."
    )
    requiere_productos   = models.BooleanField(
        default=False,
        help_text="Si está activo, la orden no podrá guardarse sin al menos un producto agregado."
    )
    fecha_creacion      = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio_mano_obra:,.0f}"

    class Meta:
        db_table            = 'tipo_servicio'
        ordering            = ['nombre']
        verbose_name        = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicio"


# ══════════════════════════════════════════════════════════
#  COMPATIBILIDAD PRODUCTO
# ══════════════════════════════════════════════════════════
class CompatibilidadProducto(models.Model):
    producto       = models.ForeignKey(Producto, on_delete=models.CASCADE, limit_choices_to={'estado': True})
    marca_vehiculo = models.ForeignKey(Marca, on_delete=models.CASCADE, limit_choices_to={'categoria': 'AUTO', 'estado': True})
    tipo_servicio  = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        srv = f" — {self.tipo_servicio.nombre}" if self.tipo_servicio else ""
        return f"{self.producto.nombre} → {self.marca_vehiculo.nombre}{srv}"

    class Meta:
        db_table        = 'compatibilidad_producto'
        unique_together = ('producto', 'marca_vehiculo', 'tipo_servicio')


# ══════════════════════════════════════════════════════════
#  CLIENTE
# ══════════════════════════════════════════════════════════
class Cliente(models.Model):
    TIPOS_DOC = [
        ('CC',  'Cédula de Ciudadanía'),
        ('CE',  'Cédula de Extranjería'),
        ('PAS', 'Pasaporte'),
    ]
    nombre           = models.CharField(max_length=150)
    tipo_documento   = models.CharField(max_length=3, choices=TIPOS_DOC, default='CC')
    numero_documento = models.CharField(max_length=20, unique=True)
    telefono         = models.CharField(max_length=20)
    email            = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cliente'


# ══════════════════════════════════════════════════════════
#  VEHÍCULO
# ══════════════════════════════════════════════════════════
class Vehiculo(models.Model):
    TIPOS_USO = [
        ('BAJO',   'Uso bajo (ciudad, poco uso)'),
        ('NORMAL', 'Uso normal (estándar)'),
        ('ALTO',   'Uso alto (viajes frecuentes)'),
        ('CARGA',  'Carga / Transporte (intensivo)'),
    ]
    placa              = models.CharField(max_length=10, unique=True)
    modelo             = models.CharField(max_length=50)
    marca              = models.ForeignKey(Marca, on_delete=models.PROTECT, limit_choices_to={'categoria': 'AUTO', 'estado': True})
    cliente            = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_uso           = models.CharField(max_length=10, choices=TIPOS_USO, default='NORMAL')
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def km_diarios_estimados(self):
        estimados = {'BAJO': 30, 'NORMAL': 50, 'ALTO': 80, 'CARGA': 120}
        return estimados.get(self.tipo_uso, 50)

    def seguimiento_activo(self):
        return self.seguimientos.filter(activo=True).order_by('-fecha_creacion').first()

    def estado_mantenimiento(self):
        seg = self.seguimiento_activo()
        if not seg or not seg.fecha_proximo_mantenimiento:
            return 'sin_datos'
        dias = (seg.fecha_proximo_mantenimiento - timezone.now().date()).days
        if dias <= 0:
            return 'vencido'
        if dias <= 15:
            return 'alerta'
        return 'ok'

    def __str__(self):
        return f"{self.placa} - {self.modelo} ({self.marca.nombre})"

    class Meta:
        db_table = 'vehiculo'
        ordering = ['-fecha_actualizacion']


# ══════════════════════════════════════════════════════════
#  NOTIFICACION
# ══════════════════════════════════════════════════════════
from django.core.exceptions import ValidationError
from django.utils import timezone

def validar_fecha_presente_o_futura(value):
    """
    Valida que la fecha de la notificación sea hoy o en el futuro.
    Rechaza cualquier fecha pasada.
    """
    hoy = timezone.now().date()
    if value < hoy:
        dias_atras = (hoy - value).days
        raise ValidationError(
            f"No se permiten notificaciones con fechas pasadas. "
            f"Esta fecha fue hace {dias_atras} día{'s' if dias_atras != 1 else ''}."
        )


class Notificacion(models.Model):
    TIPOS = [
        ('Alerta',        'Alerta'),
        ('Recordatorio',  'Recordatorio'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Urgente',       'Urgente'),
        ('Informacion',   'Información'),
    ]
    ORIGENES = [
        ('SISTEMA', 'Automática del sistema'),
        ('ADMIN',   'Creada por administrador'),
    ]
    tipo     = models.CharField(max_length=50, choices=TIPOS)
    origen   = models.CharField(max_length=10, choices=ORIGENES, default='ADMIN')
    titulo   = models.CharField(max_length=150, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    mensaje  = models.TextField()
    leido    = models.BooleanField(default=False)
    fecha    = models.DateField(
        default=timezone.now,
        validators=[validar_fecha_presente_o_futura],
        help_text="Fecha de la notificación (hoy o en el futuro)."
    )

    def __str__(self):
        return f"[{self.get_origen_display()}] {self.tipo} — {self.titulo or self.mensaje[:40]}"

    class Meta:
        db_table = 'notificacion'
        ordering = ['-fecha']


# ══════════════════════════════════════════════════════════
#  ORDEN DE SERVICIO
# ══════════════════════════════════════════════════════════
class OrdenServicio(models.Model):
    ESTADOS = [
        ('Pendiente',  'Pendiente'),
        ('En Proceso', 'En Proceso'),
    ]
    empleado = models.ForeignKey(
        UsuarioSistema,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'cargo': 'MECANICO', 'activo': True},
        verbose_name="Mecánico responsable",
    )
    vehiculo      = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    servicios     = models.ManyToManyField(
        TipoServicio,
        through='OrdenServicioDetalle',
        verbose_name="Servicios",
    )
    fecha         = models.DateTimeField(default=timezone.now)
    km_actual     = models.IntegerField(null=True, blank=True) 
    estado        = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    observaciones = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden #{self.id} — {self.vehiculo.placa}"

    class Meta:
        db_table = 'orden_servicio'

# ══════════════════════════════════════════════════════════
#  ORDEN DE SERVICIO - 
# ══════════════════════════════════════════════════════════
class OrdenServicioDetalle(models.Model):
    orden            = models.ForeignKey(
        OrdenServicio, on_delete=models.CASCADE,
        related_name='servicios_detalle'
    )
    tipo_servicio    = models.ForeignKey(
        TipoServicio, on_delete=models.PROTECT
    )
  
    precio_mano_obra = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        
        if not self.pk and (self.precio_mano_obra is None or self.precio_mano_obra == 0):
            self.precio_mano_obra = self.tipo_servicio.precio_mano_obra
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden #{self.orden_id} — {self.tipo_servicio.nombre} (${self.precio_mano_obra:,.0f})"

    class Meta:
        db_table        = 'orden_servicio_detalle'
        unique_together = ('orden', 'tipo_servicio')
        verbose_name    = "Detalle de Servicio en Orden"


# ══════════════════════════════════════════════════════════
#  SEGUIMIENTO MANTENIMIENTO
# ══════════════════════════════════════════════════════════
class SeguimientoMantenimiento(models.Model):
    ESTADOS = [
        ('Pendiente',  'Pendiente'),
        ('Completado', 'Completado'),
        ('Vencido',    'Vencido'),
    ]
    vehiculo                    = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='seguimientos')
    orden_servicio              = models.ForeignKey(OrdenServicio, on_delete=models.SET_NULL, null=True, blank=True, related_name='seguimientos')
    tipo_servicio               = models.ForeignKey(TipoServicio, on_delete=models.SET_NULL, null=True, blank=True)
    km_al_momento               = models.IntegerField(help_text="Km del vehículo cuando se registró este seguimiento")
    km_proximo_mantenimiento    = models.IntegerField(null=True, blank=True, help_text="A qué km debe volver (opcional)")
    fecha_proximo_mantenimiento = models.DateField(null=True, blank=True, help_text="Cuándo debe volver")
    estado                      = models.CharField(max_length=15, choices=ESTADOS, default='Pendiente')
    activo                      = models.BooleanField(default=True, help_text="Solo el seguimiento activo más reciente importa para alertas")
    observaciones               = models.TextField(blank=True, null=True)
    fecha_creacion              = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion         = models.DateTimeField(auto_now=True)

    # FIX #5 — Al activar este seguimiento, desactiva los anteriores del mismo vehículo
    def save(self, *args, **kwargs):
        if self.activo:
            SeguimientoMantenimiento.objects.filter(
                vehiculo=self.vehiculo,
                activo=True
            ).exclude(pk=self.pk).update(activo=False)
        super().save(*args, **kwargs)

    def dias_restantes(self):
        if not self.fecha_proximo_mantenimiento:
            return None
        return (self.fecha_proximo_mantenimiento - timezone.now().date()).days

    def estado_calculado(self):
        dias = self.dias_restantes()
        if dias is None:
            return 'sin_fecha'
        if dias <= 0:
            return 'vencido'
        if dias <= 15:
            return 'alerta'
        return 'ok'

    def __str__(self):
        return f"Seguimiento #{self.pk} — {self.vehiculo.placa} ({self.estado})"

    class Meta:
        db_table            = 'seguimiento_mantenimiento'
        ordering            = ['-fecha_creacion']
        verbose_name        = "Seguimiento de Mantenimiento"
        verbose_name_plural = "Seguimientos de Mantenimiento"


# ══════════════════════════════════════════════════════════
#  COMPRA Y COMPRA DETALLE
# ══════════════════════════════════════════════════════════

class Compra(models.Model):
    METODOS = [
        ('Efectivo',       'Efectivo'),
        ('Transferencia',  'Transferencia'),
        ('TarjetaDebito',  'Tarjeta débito'),
        ('TarjetaCredito', 'Tarjeta crédito'),
        ('Nequi',          'Nequi'),
        ('Daviplata',      'Daviplata'),
    ]
    ESTADOS_PAGO = [('Pendiente', 'Pendiente'), ('Pagada', 'Pagada')]

    proveedor             = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha                 = models.DateTimeField(default=timezone.now)
    num_factura_proveedor = models.CharField(max_length=50, unique=True)
    metodo_pago           = models.CharField(max_length=20, choices=METODOS, null=True, blank=True)
    total_pagado          = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado_pago           = models.CharField(max_length=10, choices=ESTADOS_PAGO, default='Pendiente')
    fecha_pago            = models.DateTimeField(null=True, blank=True)
    archivo_factura       = models.FileField(upload_to='facturas_proveedores/', blank=True, null=True)

    def __str__(self):
        return f"Compra {self.num_factura_proveedor} - {self.proveedor.nombre}"

    def get_total(self):
        return self.detalles.aggregate(total=Sum(F('cantidad') * F('precio_unitario'), output_field=DecimalField()))['total'] or 0

    class Meta:
        db_table = 'compra'
        ordering = ['-fecha']


class CompraDetalle(models.Model):
    compra          = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto        = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad        = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.compra.num_factura_proveedor} - {self.producto.nombre}"

    class Meta:
        db_table = 'compra_detalle'
        unique_together = ('compra', 'producto')
        
        
# ══════════════════════════════════════════════════════════
#  DETALLE PRODUCTO ORDEN DE SERVICIO
# ══════════════════════════════════════════════════════════
class DetalleOrdenProducto(models.Model):
    orden    = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE, related_name='productos_usados')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

  
    precio_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Precio del producto en el momento de agregarlo a la orden"
    )

    def save(self, *args, **kwargs):
        if self.producto.stock < self.cantidad:
            raise ValueError(f"Stock insuficiente para '{self.producto.nombre}'.")
        if not self.pk:
            self.precio_unitario = self.producto.precio  # snapshot
            self.producto.stock -= self.cantidad
            self.producto.save(update_fields=['stock'])
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.producto.stock += self.cantidad
        self.producto.save(update_fields=['stock'])
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'detalle_orden_producto'


# ══════════════════════════════════════════════════════════
#  FACTURA
#
# ══════════════════════════════════════════════════════════
class Factura(models.Model):
    TIPO_FACTURA = [
        ('SERVICIO', 'Orden de Servicio'),
        ('PRODUCTO', 'Venta de Producto'),
        ('COMPRA',   'Compra a Proveedor'),
    ]
    METODOS_PAGO = [
        ('Efectivo',      'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('TarjetaDebito', 'Tarjeta Débito'),
        ('Nequi',         'Nequi'),
        ('Daviplata',     'Daviplata'),
    ]
    ESTADOS_PAGO = [('Pendiente', 'Pendiente'), ('Pagada', 'Pagada')]

    tipo           = models.CharField(max_length=10, choices=TIPO_FACTURA, default='SERVICIO')
    comprobante_pago = models.FileField(upload_to='facturas_comprobantes/', blank=True, null=True)
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha_emision  = models.DateTimeField(auto_now_add=True)
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.SET_NULL, null=True, blank=True)
    compra         = models.OneToOneField('Compra', on_delete=models.SET_NULL, null=True, blank=True)
    producto       = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad       = models.PositiveIntegerField(default=1)
    subtotal       = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    iva            = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total          = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado_pago    = models.CharField(max_length=10, choices=ESTADOS_PAGO, default='Pendiente')
    metodo_pago    = models.CharField(max_length=20, choices=METODOS_PAGO, null=True, blank=True)
    fecha_pago     = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.tipo == 'SERVICIO':
            if not self.orden_servicio:
                raise ValueError("Una factura de tipo SERVICIO requiere una orden de servicio.")
            servicios = sum(
                d.precio_mano_obra
                for d in self.orden_servicio.servicios_detalle.all()
            )
            productos = sum(
                dp.cantidad * dp.precio_unitario
                for dp in self.orden_servicio.productos_usados.all()
            )
            self.subtotal = servicios + productos
            self.total    = self.subtotal


        elif self.tipo == 'PRODUCTO':
            if not self.producto:
                raise ValueError("Una factura de tipo PRODUCTO requiere un producto.")
            self.subtotal = self.producto.precio * self.cantidad
            self.total    = self.subtotal

        elif self.tipo == 'COMPRA':
            if not self.compra:
                raise ValueError("Una factura de tipo COMPRA requiere una compra.")
            self.subtotal = self.compra.total_pagado
            self.total    = self.subtotal

        if self.estado_pago == 'Pagada' and not self.fecha_pago:
            self.fecha_pago = timezone.now()

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'factura'
        ordering = ['-fecha_emision']