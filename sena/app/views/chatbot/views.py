from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum, Count, F, Q
import json
from app.models import (
    OrdenServicio, Vehiculo, TipoServicio, 
    SeguimientoMantenimiento, Notificacion,
    Producto, DetalleOrdenProducto, Factura,
    Caja
)


MENU_PREGUNTAS = """¿Qué quieres saber?

Vehículos | Órdenes | Mantenimientos | Productos | Ventas | Alertas

Ejemplos: "Órdenes abiertas", "Próximos mantenimientos", "Total vendido"
"""


def _obtener_atributo(obj, *nombres_atributo, default="N/A"):
    """Obtiene un atributo de un objeto, probando múltiples nombres."""
    for nombre in nombres_atributo:
        try:
            valor = getattr(obj, nombre, None)
            if valor is not None:
                return valor
        except:
            pass
    return default


def _responder_pregunta_especifica(pregunta):
    """Responde preguntas específicas con datos REALES."""
    p = pregunta.lower().strip()
    
    # ── VEHÍCULOS ──
    if any(x in p for x in ['cuántos vehículos', 'cuantos vehiculos', 'cuantos vehículos',
                             'listar vehículos', 'listar vehiculos', 'listar vehículos',
                             'vehículos registrados', 'vehiculos registrados', 'vehículos registrados',
                             'vehículos', 'vehiculos', 'vehículo', 'vehiculo']) and 'orden' not in p:
        try:
            total = Vehiculo.objects.count()
            
            if total == 0:
                return True, "No hay vehículos registrados."
            
            vehiculos = Vehiculo.objects.select_related('marca', 'cliente').all()[:6]
            
            lineas = [f"VEHICULOS ({total})"]
            
            for v in vehiculos:
                marca = v.marca.nombre if v.marca else "Desconocida"
                cliente = v.cliente.nombre if v.cliente else "Sin asignar"
                modelo = v.modelo if v.modelo else "Sin modelo"
                
                lineas.append(f"{v.placa} • {marca} {modelo} • {cliente}")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── ÓRDENES ──
    if any(x in p for x in ['órdenes abiertas', 'ordenes abiertas', 'órdenes pendientes', 
                             'ordenes pendientes', 'órdenes en proceso', 'ordenes en proceso',
                             'órdenes', 'ordenes', 'orden']) and 'vehículo' not in p and 'vehiculo' not in p:
        try:
            if 'vencido' in p or 'vencidas' in p:
                ordenes = OrdenServicio.objects.filter(estado='Pendiente').select_related('vehiculo', 'empleado')
                titulo = "ORDENES VENCIDAS"
            elif 'proceso' in p:
                ordenes = OrdenServicio.objects.filter(estado='En Proceso').select_related('vehiculo', 'empleado')
                titulo = "ORDENES EN PROCESO"
            else:
                ordenes = OrdenServicio.objects.filter(estado__in=['Pendiente', 'En Proceso']).select_related('vehiculo', 'empleado')
                titulo = "ORDENES ACTIVAS"
            
            total = ordenes.count()
            
            if total == 0:
                return True, f"No hay {titulo.lower()}."
            
            lineas = [f"{titulo} ({total})"]
            
            for o in ordenes[:6]:
                placa = o.vehiculo.placa if o.vehiculo else "Sin vehículo"
                mecanico = o.empleado.nombre_completo if o.empleado else "Sin asignar"
                
                fecha_obj = _obtener_atributo(o, 'fecha_creacion', 'created_at', 'fecha', 'date_created')
                if fecha_obj and hasattr(fecha_obj, 'strftime'):
                    fecha = fecha_obj.strftime('%d/%m')
                else:
                    fecha = "Sin fecha"
                
                lineas.append(f"#{o.id} • {placa} • {o.estado} • {mecanico} • {fecha}")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── MANTENIMIENTOS ──
    if any(x in p for x in ['próximos mantenimientos', 'proximos mantenimientos', 
                             'mantenimientos vencidos', 'seguimientos', 'seguimiento',
                             'mantenimientos', 'mantenimiento', 'proximos', 'proximo']):
        try:
            hoy = timezone.now().date()
            
            if 'vencido' in p:
                segs = SeguimientoMantenimiento.objects.filter(
                    activo=True,
                    fecha_proximo_mantenimiento__lt=hoy
                ).select_related('vehiculo', 'tipo_servicio')
                titulo = "MANTENIMIENTOS VENCIDOS"
            else:
                segs = SeguimientoMantenimiento.objects.filter(
                    activo=True,
                    fecha_proximo_mantenimiento__isnull=False
                ).select_related('vehiculo', 'tipo_servicio').order_by('fecha_proximo_mantenimiento')
                titulo = "PROXIMOS MANTENIMIENTOS"
            
            total = segs.count()
            
            if total == 0:
                return True, f"No hay {titulo.lower()}."
            
            lineas = [f"{titulo} ({total})"]
            
            for s in segs[:6]:
                tipo = s.tipo_servicio.nombre if s.tipo_servicio else "Mantenimiento"
                
                fecha_mant = _obtener_atributo(s, 'fecha_proximo_mantenimiento', 'next_maintenance_date', 'next_date')
                
                if fecha_mant and hasattr(fecha_mant, 'strftime'):
                    fecha = fecha_mant.strftime('%d/%m/%Y')
                    dias_restantes = (fecha_mant - hoy).days
                    if dias_restantes < 0:
                        estado = f"VENCIDO"
                    else:
                        estado = f"En {dias_restantes}d"
                else:
                    fecha = "Sin fecha"
                    estado = "Sin programar"
                
                lineas.append(f"{s.vehiculo.placa} • {tipo} • {fecha} • {estado}")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── PRODUCTOS ──
    if any(x in p for x in ['qué productos', 'que productos', 'productos disponibles', 
                             'productos hay', 'stock bajo', 'productos']):
        try:
            if 'bajo' in p:
                productos = Producto.objects.filter(estado=True, stock__lte=F('stock_minimo'))
                titulo = "PRODUCTOS CON STOCK BAJO"
            else:
                productos = Producto.objects.filter(estado=True).order_by('-stock')
                titulo = "PRODUCTOS"
            
            total = productos.count()
            
            if total == 0:
                return True, f"No hay {titulo.lower()}."
            
            lineas = [f"{titulo} ({total})"]
            
            for pr in productos[:6]:
                marca = pr.marca.nombre if pr.marca else "Sin marca"
                precio = f"${pr.precio:,.0f}"
                
                lineas.append(f"{pr.nombre} • {marca} • Stock: {pr.stock} • {precio}")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── PRODUCTOS MÁS USADOS ──
    if any(x in p for x in ['productos más usados', 'productos mas usados', 
                             'más vendidos', 'mas vendidos', 'más usado', 'mas usado']):
        try:
            productos = DetalleOrdenProducto.objects.values(
                'producto__nombre', 
                'producto__marca__nombre'
            ).annotate(
                veces=Count('id'),
                cantidad_total=Sum('cantidad')
            ).order_by('-veces')
            
            if not productos:
                return True, "No hay datos de productos utilizados."
            
            lineas = ["PRODUCTOS MAS USADOS"]
            
            for i, p in enumerate(productos[:6], 1):
                nombre = p['producto__nombre']
                marca = p['producto__marca__nombre'] or "Sin marca"
                veces = p['veces']
                
                lineas.append(f"{i}. {nombre} ({marca}) • Usado {veces}x")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── VENTAS Y GANANCIAS (DESDE TABLA CAJA) ──
    if any(x in p for x in ['cuánto ganamos', 'cuanto ganamos', 'total vendido', 
                             'ventas', 'ingresos', 'ganancia', 'ingresos por tipo']):
        try:
            # Total INGRESOS
            total_ingresos = Caja.objects.filter(tipo='INGRESO').aggregate(Sum('monto'))['monto__sum'] or 0
            
            # Total EGRESOS
            total_egresos = Caja.objects.filter(tipo='EGRESO').aggregate(Sum('monto'))['monto__sum'] or 0
            
            # Saldo neto
            saldo = total_ingresos - total_egresos
            
            # Desglose por categoría de INGRESOS
            ingresos_por_cat = Caja.objects.filter(tipo='INGRESO').values('categoria').annotate(
                total=Sum('monto')
            ).order_by('-total')
            
            # Desglose por categoría de EGRESOS
            egresos_por_cat = Caja.objects.filter(tipo='EGRESO').values('categoria').annotate(
                total=Sum('monto')
            ).order_by('-total')
            
            respuesta = f"""RESUMEN DE CAJA

Total Ingresos: ${total_ingresos:,.0f}
Total Egresos: ${total_egresos:,.0f}
Saldo Neto: ${saldo:,.0f}"""
            
            if ingresos_por_cat:
                respuesta += "\n\nIngresos por categoría:"
                for ic in ingresos_por_cat[:5]:
                    cat = ic['categoria']
                    tot = ic['total']
                    respuesta += f"\n  • {cat}: ${tot:,.0f}"
            
            if egresos_por_cat:
                respuesta += "\n\nEgresos por categoría:"
                for ec in egresos_por_cat[:5]:
                    cat = ec['categoria']
                    tot = ec['total']
                    respuesta += f"\n  • {cat}: ${tot:,.0f}"
            
            return True, respuesta
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # ── ALERTAS ──
    if any(x in p for x in ['alertas', 'alertas activas', 'notificaciones', 
                             'notificaciones pendientes', 'hay alertas', 'alerta']):
        try:
            notifs = Notificacion.objects.filter(leido=False).select_related('vehiculo')
            total = notifs.count()
            
            if total == 0:
                return True, "No hay alertas activas."
            
            lineas = [f"ALERTAS ({total})"]
            
            for n in notifs[:6]:
                placa = n.vehiculo.placa if n.vehiculo else "General"
                fecha = n.fecha_creacion.strftime('%d/%m %H:%M') if hasattr(n, 'fecha_creacion') else "Sin fecha"
                
                lineas.append(f"[{n.tipo}] {n.titulo} • {placa} • {fecha}")
            
            return True, "\n".join(lineas)
        
        except Exception as e:
            return True, f"Error: {str(e)}"
    
    # No reconoce la pregunta
    return False, None


@csrf_exempt
@login_required(login_url='login:login')
def chatbot_responder(request):
    """Chatbot mejorado - respuestas concisas y claras."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
        mensaje = data.get('mensaje', '').strip()

        if not mensaje:
            return JsonResponse({'error': 'Mensaje vacío'}, status=400)

        print(f"[CHATBOT] Pregunta: {mensaje}")
        
        # Si dice "hola" o similar, mostrar menú
        if mensaje.lower() in ['hola', 'hola!', 'holaaa', 'hi', 'ayuda', 'menu', 
                               'qué puedes hacer', 'que puedes hacer', '?']:
            print("[CHATBOT] Mostrando menú")
            return JsonResponse({'respuesta': MENU_PREGUNTAS})
        
        # Responder pregunta específica
        tiene_respuesta, respuesta = _responder_pregunta_especifica(mensaje)
        
        if tiene_respuesta:
            print("[CHATBOT] Respuesta encontrada")
            return JsonResponse({'respuesta': respuesta})
        
        # No reconoce la pregunta
        print("[CHATBOT] Pregunta no reconocida")
        return JsonResponse({
            'respuesta': 'No entiendo esa pregunta.\n\nEscribe "hola" para ver las preguntas que puedo responder.'
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        print(f"[CHATBOT ERROR] {str(e)}")
        return JsonResponse({
            'error': 'Error al procesar tu pregunta'
        }, status=500)