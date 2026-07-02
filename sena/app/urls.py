from django.urls import path

from .views.dashboard              import views as dash
from .views.Cliente                import views as cli
from .views.Vehiculo               import views as veh
from .views.UsuarioSistema         import views as usr
from .views.compra                 import views as compra
from .views.Proveedor              import views as prov
from .views.Marca                  import views as marca
from .views.Producto               import views as prod
from .views.Notificacion           import views as notif
from .views.caja                   import views as caja
from .views.tipo_servicio          import views as tipo_serv
from .views.Orden_servicio         import views as orden
from .views.DetalleOrdenProducto   import views as detalles
from .views.CompatibilidadProducto import views as comp
from .views.factura                import views as factura
from .views.backup                 import views as backup
from .views.seguimiento            import views as seguimiento
from .views.ayuda                  import views as ayuda   
from app                           import reportes as rep
from .views.chatbot                import views as chatbot


app_name = 'app'

urlpatterns = [

    # ── DASHBOARD
    path('dashboard/', dash.DashboardView.as_view(), name='dashboard'),

    # ── AYUDA  
    path('ayuda/', ayuda.AyudaView.as_view(), name='ayuda'),
    path('ayuda/',                        ayuda.AyudaView.as_view(),   name='ayuda'),
    path('ayuda/manual/<str:nombre>/',    ayuda.descargar_manual,      name='descargar_manual'),

    # ── USUARIOS
    path('usuarios/perfil/',                  usr.PerfilView.as_view(),              name='mi_perfil'),
    path('usuarios/listar/',                  usr.UsuarioListView.as_view(),         name='listar_usuario'),
    path('usuarios/crear/',                   usr.UsuarioCreateView.as_view(),       name='crear_usuario'),
    path('usuarios/editar/<int:pk>/',         usr.UsuarioUpdateView.as_view(),       name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/',       usr.UsuarioDeleteView.as_view(),       name='eliminar_usuario'),
    path('usuarios/cambiar-estado/<int:pk>/', usr.CambiarEstadoUsuarioView.as_view(),name='cambiar_estado_usuario'),

    # ── CLIENTES
    path('clientes/listar/',            cli.ClienteListView.as_view(),   name='listar_clientes'),
    path('clientes/crear/',             cli.ClienteCreateView.as_view(), name='crear_cliente'),
    path('clientes/editar/<int:pk>/',   cli.ClienteUpdateView.as_view(), name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', cli.ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('clientes/validar-documento/', cli.validar_documento_cliente, name='validar_documento_cliente'),
    path('clientes/validar-email/',     cli.validar_email_cliente,     name='validar_email_cliente'),

    # ── VEHÍCULOS
    path('vehiculos/listar/',            veh.VehiculoListView.as_view(),   name='listar_vehiculos'),
    path('vehiculos/crear/',             veh.VehiculoCreateView.as_view(), name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>/',   veh.VehiculoUpdateView.as_view(), name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>/', veh.VehiculoDeleteView.as_view(), name='eliminar_vehiculo'),

    # ── MARCAS
    path('marca/listar/',            marca.MarcaListView.as_view(),   name='listar_marca'),
    path('marca/crear/',             marca.MarcaCreateView.as_view(), name='crear_marca'),
    path('marca/editar/<int:pk>/',   marca.MarcaUpdateView.as_view(), name='editar_marca'),
    path('marca/eliminar/<int:pk>/', marca.MarcaDeleteView.as_view(), name='eliminar_marca'),
    path('marca/crear-ajax/',        marca.crear_marca_ajax,          name='crear_marca_ajax'),

    # ── PROVEEDORES
    path('proveedor/listar/',            prov.ProveedorListView.as_view(),   name='listar_proveedores'),
    path('proveedor/crear/',             prov.ProveedorCreateView.as_view(), name='crear_proveedor'),
    path('proveedor/editar/<int:pk>/',   prov.ProveedorUpdateView.as_view(), name='editar_proveedor'),
    path('proveedor/eliminar/<int:pk>/', prov.ProveedorDeleteView.as_view(), name='eliminar_proveedor'),
    path('proveedor/validar-nit/',       prov.validar_nit_proveedor,         name='validar_nit_proveedor'),
    

    # ── PRODUCTOS
    path('producto/listar/',               prod.ProductoListView.as_view(),          name='listar_producto'),
    path('producto/crear/',                prod.ProductoCreateView.as_view(),        name='crear_producto'),
    path('producto/editar/<int:pk>/',      prod.ProductoUpdateView.as_view(),        name='editar_producto'),
    path('producto/eliminar/<int:pk>/',    prod.ProductoDeleteView.as_view(),        name='eliminar_producto'),
    path('producto/cambiar-estado/<int:pk>/', prod.ProductoCambiarEstadoView.as_view(), name='producto_cambiar_estado'), 

    # ── COMPATIBILIDAD
    path('compatibilidad/listar/',            comp.CompatibilidadListView.as_view(),   name='listar_compatibilidad'),
    path('compatibilidad/crear/',             comp.CompatibilidadCreateView.as_view(), name='crear_compatibilidad'),
    path('compatibilidad/editar/<int:pk>/',   comp.CompatibilidadUpdateView.as_view(), name='editar_compatibilidad'),
    path('compatibilidad/eliminar/<int:pk>/', comp.CompatibilidadDeleteView.as_view(), name='eliminar_compatibilidad'),

    # ── TIPO DE SERVICIO
    path('tipo_servicio/listar/',            tipo_serv.TipoServicioListView.as_view(),   name='tipo_servicio_list'),
    path('tipo_servicio/crear/',             tipo_serv.TipoServicioCreateView.as_view(), name='create_servico'),
    path('tipo_servicio/editar/<int:pk>/',   tipo_serv.TipoServicioUpdateView.as_view(), name='tipo_servicio_update'),
    path('tipo_servicio/eliminar/<int:pk>/', tipo_serv.TipoServicioDeleteView.as_view(), name='tipo_servicio_delete'),

    # ── ÓRDENES DE SERVICIO
    path('orden_servicio/listar/',                   orden.OrdenServicioListView.as_view(),       name='orden_servicio_list'),
    path('orden_servicio/crear/',                    orden.OrdenServicioCreateView.as_view(),     name='orden_servicio_create'),
    path('orden_servicio/detalle/<int:pk>/',         orden.OrdenServicioDetailView.as_view(),     name='orden_servicio_detail'),
    path('orden_servicio/editar/<int:pk>/',          orden.OrdenServicioUpdateView.as_view(),     name='orden_servicio_edit'),
    path('orden_servicio/eliminar/<int:pk>/',        orden.OrdenServicioDeleteView.as_view(),     name='orden_servicio_delete'),
    path('orden_servicio/vehiculo-km/<int:pk>/',     orden.VehiculoKmView.as_view(),              name='vehiculo_km'),
    path('orden_servicio/verificar-compatibilidad/', orden.VerificarCompatibilidadView.as_view(), name='verificar_compatibilidad'),
    path('orden_servicio/productos-compatibles/',    orden.ProductosCompatiblesView.as_view(),    name='productos_compatibles'),
    path('orden_servicio/<int:pk>/cambiar-estado/',  orden.CambiarEstadoOrdenView.as_view(),      name='cambiar_estado_orden'),

    # ── DETALLES DE ORDEN
    path('detalles/',                 detalles.DetalleOrdenListView.as_view(),   name='detalle_orden_list'),
    path('detalles/add/',             detalles.DetalleOrdenCreateView.as_view(), name='detalle_orden_add'),
    path('detalles/edit/<int:pk>/',   detalles.DetalleOrdenUpdateView.as_view(), name='detalle_orden_edit'),
    path('detalles/delete/<int:pk>/', detalles.DetalleOrdenDeleteView.as_view(), name='detalle_orden_delete'),

    # ── SEGUIMIENTO MANTENIMIENTO
    path('seguimiento/',                     seguimiento.SeguimientoListView.as_view(),      name='seguimiento_list'),
    path('seguimiento/eliminar/<int:pk>/',   seguimiento.SeguimientoDeleteView.as_view(),    name='seguimiento_eliminar'),
    path('seguimiento/completar/<int:pk>/',  seguimiento.SeguimientoCompletarView.as_view(), name='seguimiento_completar'),
    path('seguimiento/servicios-orden/',     seguimiento.get_servicios_orden,                name='servicios_orden'),

    # ── COMPRAS
    path('compras/listar/',                      compra.CompraListView.as_view(),   name='lista_compras'),
    path('compras/crear/',                       compra.CompraCreateView.as_view(), name='crear_compra'),
    path('compras/eliminar/<int:pk>/',           compra.CompraDeleteView.as_view(), name='eliminar_compra'),
    path('compras/pagar/<int:pk>/',              compra.PagarCompraView.as_view(),  name='pagar_compra'),
    path('compras/productos-por-proveedor/',     compra.productos_por_proveedor,    name='productos_por_proveedor'),

    # ── CAJA
    path('caja/listar/', caja.CajaListView.as_view(), name='caja_listar'),

    # ── FACTURAS
    path('factura/listar/',            factura.FacturaListView.as_view(),   name='listar_factura'),
    path('factura/crear/',             factura.FacturaCreateView.as_view(), name='crear_factura'),
    path('factura/detalle/<int:pk>/',  factura.FacturaDetailView.as_view(), name='detalle_factura'),
    path('factura/eliminar/<int:pk>/', factura.FacturaDeleteView.as_view(), name='eliminar_factura'),
    path('factura/pagar/<int:pk>/',    factura.PagarFacturaView.as_view(),  name='pagar_factura'),

    # ── NOTIFICACIONES
    path('notificaciones/listar/',                notif.NotificacionListView.as_view(),                    name='listar_notificacion'),
    path('notificaciones/crear/',                 notif.NotificacionCreateView.as_view(),                  name='crear_notificacion'),
    path('notificaciones/marcar-leida/<int:pk>/', notif.MarcarLeidaView.as_view(),                         name='marcar_notificacion_leida'),
    path('notificaciones/marcar-todas-leidas/',   notif.MarcarTodasLeidasView.as_view(),                   name='marcar_todas_leidas'),
    path('notificaciones/no-leidas/',             notif.notificaciones_no_leidas,                          name='notificaciones_no_leidas'),
    path('notificaciones/eliminar/<int:pk>/',     notif.NotificacionDeleteView.as_view(),                  name='eliminar_notificacion'),
    path('notificaciones/eliminar-masivo/',        notif.EliminarNotificacionesMasivoView.as_view(),        name='eliminar_notificaciones_masivo'),
    path('notificaciones/eliminar-todas/',         notif.EliminarTodasNotificacionesView.as_view(),         name='eliminar_todas_notificaciones'),

    # ── REPORTES PDF
    path('reportes/clientes/pdf/',    rep.ExportarClientesPDF.as_view(),    name='reporte_clientes_pdf'),
    path('reportes/vehiculos/pdf/',   rep.ExportarVehiculosPDF.as_view(),   name='reporte_vehiculos_pdf'),
    path('reportes/productos/pdf/',   rep.ExportarProductosPDF.as_view(),   name='reporte_productos_pdf'),
    path('reportes/proveedores/pdf/', rep.ExportarProveedoresPDF.as_view(), name='reporte_proveedores_pdf'),
    path('reportes/compras/pdf/',     rep.ExportarComprasPDF.as_view(),     name='reporte_compras_pdf'),
    path('reportes/caja/pdf/',        rep.ExportarCajaPDF.as_view(),        name='reporte_caja_pdf'),
    path('reportes/ordenes/pdf/',     rep.ExportarOrdenesPDF.as_view(),     name='reporte_ordenes_pdf'),
    path('reportes/facturas/pdf/',    rep.ExportarFacturasPDF.as_view(),    name='reporte_facturas_pdf'),

    # ── REPORTES EXCEL
    path('reportes/clientes/excel/',    rep.ExportarClientesExcel.as_view(),    name='reporte_clientes_excel'),
    path('reportes/vehiculos/excel/',   rep.ExportarVehiculosExcel.as_view(),   name='reporte_vehiculos_excel'),
    path('reportes/productos/excel/',   rep.ExportarProductosExcel.as_view(),   name='reporte_productos_excel'),
    path('reportes/proveedores/excel/', rep.ExportarProveedoresExcel.as_view(), name='reporte_proveedores_excel'),
    path('reportes/compras/excel/',     rep.ExportarComprasExcel.as_view(),     name='reporte_compras_excel'),
    path('reportes/caja/excel/',        rep.ExportarCajaExcel.as_view(),        name='reporte_caja_excel'),
    path('reportes/ordenes/excel/',     rep.ExportarOrdenesExcel.as_view(),     name='reporte_ordenes_excel'),
    path('reportes/facturas/excel/',    rep.ExportarFacturasExcel.as_view(),    name='reporte_facturas_excel'),

    # ── BACKUP
    path('backup/',           backup.backup,          name='backup'),
    path('backup/restaurar/', backup.restaurar_datos, name='restaurar_datos'),

    # ── CHATBOT
    path('chatbot/', chatbot.chatbot_responder, name='chatbot'),
    
]