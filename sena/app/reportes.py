from django.views import View
from app.models import (Cliente, Vehiculo, Producto, Proveedor,
                        Compra, Caja, OrdenServicio, Factura)
from app.utils import exportar_pdf, exportar_excel
from datetime import datetime


# ══════════════════════════════════════
#  CLIENTES
# ══════════════════════════════════════
class ExportarClientesPDF(View):
    def get(self, request):
        datos = [(c.id, c.nombre, c.tipo_documento, c.numero_documento, c.telefono, c.email or '-')
                 for c in Cliente.objects.all()]
        return exportar_pdf(
            titulo='REPORTE DE CLIENTES',
            columnas=['ID', 'Nombre', 'Tipo Doc.', 'Documento', 'Teléfono', 'Email'],
            datos=datos,
            nombre_archivo=f'Reporte_Clientes_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarClientesExcel(View):
    def get(self, request):
        datos = [(c.id, c.nombre, c.tipo_documento, c.numero_documento, c.telefono, c.email or '-')
                 for c in Cliente.objects.all()]
        return exportar_excel(
            titulo='REPORTE DE CLIENTES',
            columnas=['ID', 'Nombre', 'Tipo Doc.', 'Documento', 'Teléfono', 'Email'],
            datos=datos,
            nombre_archivo=f'Reporte_Clientes_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  VEHÍCULOS
# ══════════════════════════════════════
class ExportarVehiculosPDF(View):
    def get(self, request):
        datos = [(v.id, v.placa, v.modelo, v.marca.nombre, v.cliente.nombre)
                 for v in Vehiculo.objects.select_related('marca', 'cliente').all()]
        return exportar_pdf(
            titulo='REPORTE DE VEHÍCULOS',
            columnas=['ID', 'Placa', 'Modelo', 'Marca', 'Cliente'],
            datos=datos,
            nombre_archivo=f'Reporte_Vehiculos_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarVehiculosExcel(View):
    def get(self, request):
        datos = [(v.id, v.placa, v.modelo, v.marca.nombre, v.cliente.nombre)
                 for v in Vehiculo.objects.select_related('marca', 'cliente').all()]
        return exportar_excel(
            titulo='REPORTE DE VEHÍCULOS',
            columnas=['ID', 'Placa', 'Modelo', 'Marca', 'Cliente'],
            datos=datos,
            nombre_archivo=f'Reporte_Vehiculos_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  PRODUCTOS
# ══════════════════════════════════════
class ExportarProductosPDF(View):
    def get(self, request):
        datos = [(p.id, p.codigo, p.nombre, p.marca.nombre, str(p.precio),
                  p.stock, p.stock_minimo, 'Activo' if p.estado else 'Inactivo')
                 for p in Producto.objects.select_related('marca').all()]
        return exportar_pdf(
            titulo='REPORTE DE PRODUCTOS / STOCK',
            columnas=['ID', 'Código', 'Nombre', 'Marca', 'Precio', 'Stock', 'Stock Mín.', 'Estado'],
            datos=datos,
            nombre_archivo=f'Reporte_Productos_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarProductosExcel(View):
    def get(self, request):
        datos = [(p.id, p.codigo, p.nombre, p.marca.nombre, str(p.precio),
                  p.stock, p.stock_minimo, 'Activo' if p.estado else 'Inactivo')
                 for p in Producto.objects.select_related('marca').all()]
        return exportar_excel(
            titulo='REPORTE DE PRODUCTOS / STOCK',
            columnas=['ID', 'Código', 'Nombre', 'Marca', 'Precio', 'Stock', 'Stock Mín.', 'Estado'],
            datos=datos,
            nombre_archivo=f'Reporte_Productos_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  PROVEEDORES
# ══════════════════════════════════════
class ExportarProveedoresPDF(View):
    def get(self, request):
        datos = [(p.id, p.nombre, p.nit, p.telefono, p.direccion)
                 for p in Proveedor.objects.all()]
        return exportar_pdf(
            titulo='REPORTE DE PROVEEDORES',
            columnas=['ID', 'Nombre', 'NIT', 'Teléfono', 'Dirección'],
            datos=datos,
            nombre_archivo=f'Reporte_Proveedores_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarProveedoresExcel(View):
    def get(self, request):
        datos = [(p.id, p.nombre, p.nit, p.telefono, p.direccion)
                 for p in Proveedor.objects.all()]
        return exportar_excel(
            titulo='REPORTE DE PROVEEDORES',
            columnas=['ID', 'Nombre', 'NIT', 'Teléfono', 'Dirección'],
            datos=datos,
            nombre_archivo=f'Reporte_Proveedores_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  COMPRAS
# ══════════════════════════════════════
class ExportarComprasPDF(View):
    def get(self, request):
        datos = [(c.id, c.proveedor.nombre, c.producto.nombre, c.cantidad,
                  str(c.total_pagado), c.metodo_pago, c.fecha.strftime('%d/%m/%Y'))
                 for c in Compra.objects.select_related('proveedor', 'producto').all()]
        return exportar_pdf(
            titulo='REPORTE DE COMPRAS',
            columnas=['ID', 'Proveedor', 'Producto', 'Cantidad', 'Total', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Compras_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarComprasExcel(View):
    def get(self, request):
        datos = [(c.id, c.proveedor.nombre, c.producto.nombre, c.cantidad,
                  str(c.total_pagado), c.metodo_pago, c.fecha.strftime('%d/%m/%Y'))
                 for c in Compra.objects.select_related('proveedor', 'producto').all()]
        return exportar_excel(
            titulo='REPORTE DE COMPRAS',
            columnas=['ID', 'Proveedor', 'Producto', 'Cantidad', 'Total', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Compras_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  CAJA
# ══════════════════════════════════════
class ExportarCajaPDF(View):
    def get(self, request):
        datos = [(c.id, c.tipo, c.categoria, c.descripcion,
                  str(c.monto), c.metodo_pago, c.fecha.strftime('%d/%m/%Y'))
                 for c in Caja.objects.all()]
        return exportar_pdf(
            titulo='REPORTE DE MOVIMIENTOS DE CAJA',
            columnas=['ID', 'Tipo', 'Categoría', 'Descripción', 'Monto', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Caja_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarCajaExcel(View):
    def get(self, request):
        datos = [(c.id, c.tipo, c.categoria, c.descripcion,
                  str(c.monto), c.metodo_pago, c.fecha.strftime('%d/%m/%Y'))
                 for c in Caja.objects.all()]
        return exportar_excel(
            titulo='REPORTE DE MOVIMIENTOS DE CAJA',
            columnas=['ID', 'Tipo', 'Categoría', 'Descripción', 'Monto', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Caja_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  ÓRDENES DE SERVICIO
# ══════════════════════════════════════
class ExportarOrdenesPDF(View):
    def get(self, request):
        datos = [(o.id, o.vehiculo.placa, o.vehiculo.cliente.nombre,
                  ', '.join(s.nombre for s in o.servicios.all()),
                  o.estado, o.km_actual,
                  o.fecha.strftime('%d/%m/%Y'))
                 for o in OrdenServicio.objects.select_related(
                     'vehiculo__cliente').prefetch_related('servicios').all()]
        return exportar_pdf(
            titulo='REPORTE DE ÓRDENES DE SERVICIO',
            columnas=['ID', 'Placa', 'Cliente', 'Servicio', 'Estado', 'KM', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Ordenes_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarOrdenesExcel(View):
    def get(self, request):
        datos = [(o.id, o.vehiculo.placa, o.vehiculo.cliente.nombre,
                  ', '.join(s.nombre for s in o.servicios.all()),  # ✅ corregido: M2M igual que PDF
                  o.estado, o.km_actual,
                  o.fecha.strftime('%d/%m/%Y'))
                 for o in OrdenServicio.objects.select_related(
                     'vehiculo__cliente').prefetch_related('servicios').all()]  # ✅ corregido: prefetch_related
        return exportar_excel(
            titulo='REPORTE DE ÓRDENES DE SERVICIO',
            columnas=['ID', 'Placa', 'Cliente', 'Servicio', 'Estado', 'KM', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Ordenes_{datetime.now().strftime("%d_%m_%Y")}'
        )


# ══════════════════════════════════════
#  FACTURAS
# ══════════════════════════════════════
class ExportarFacturasPDF(View):
    def get(self, request):
        datos = [(f.id, f.numero_factura, f.get_tipo_display(),
                  str(f.subtotal), str(f.iva), str(f.total),
                  f.estado_pago, f.metodo_pago or '-',
                  f.fecha_emision.strftime('%d/%m/%Y'))
                 for f in Factura.objects.all()]
        return exportar_pdf(
            titulo='REPORTE DE FACTURAS',
            columnas=['ID', 'N° Factura', 'Tipo', 'Subtotal', 'IVA', 'Total', 'Estado', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Facturas_{datetime.now().strftime("%d_%m_%Y")}'
        )

class ExportarFacturasExcel(View):
    def get(self, request):
        datos = [(f.id, f.numero_factura, f.get_tipo_display(),
                  str(f.subtotal), str(f.iva), str(f.total),
                  f.estado_pago, f.metodo_pago or '-',
                  f.fecha_emision.strftime('%d/%m/%Y'))
                 for f in Factura.objects.all()]
        return exportar_excel(
            titulo='REPORTE DE FACTURAS',
            columnas=['ID', 'N° Factura', 'Tipo', 'Subtotal', 'IVA', 'Total', 'Estado', 'Método Pago', 'Fecha'],
            datos=datos,
            nombre_archivo=f'Reporte_Facturas_{datetime.now().strftime("%d_%m_%Y")}'
        )