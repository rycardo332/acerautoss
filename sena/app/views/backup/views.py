"""
VISTAS PARA RESPALDO Y RESTAURACION DE BD
MySQL con mysqldump — Proyecto Acerautos
"""
import os
import subprocess
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

# ========== DIRECTORIO DE BACKUPS ==========
BACKUP_DIR = os.path.join(settings.BASE_DIR, 'backups')

def _asegurar_directorio():
    os.makedirs(BACKUP_DIR, exist_ok=True)

# ========== CREDENCIALES DESDE SETTINGS ==========
def obtener_credenciales():
    db = settings.DATABASES['default']
    return {
        'host':       db.get('HOST', 'localhost'),
        'user':       db.get('USER', 'root'),
        'password':   db.get('PASSWORD', ''),
        'database':   db.get('NAME', 'acerautos_db'),
        'port':       str(db.get('PORT', 3306)),
        'mysql_path': r'C:\Program Files\MySQL\MySQL Server 8.0\bin',
    }

# ========== PROBAR CONEXIÓN ==========
def probar_conexion():
    creds = obtener_credenciales()
    try:
        cmd = [
            os.path.join(creds['mysql_path'], 'mysql.exe'),
            '-h', creds['host'],
            '-u', creds['user'],
            f"--password={creds['password']}",
            '-P', creds['port'],
            '-e', 'SELECT 1;',
            creds['database'],
        ]
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return resultado.returncode == 0
    except Exception:
        return False

# ========== VISTA PRINCIPAL ==========
@require_http_methods(["GET", "POST"])
def backup(request):
    _asegurar_directorio()

    if request.method == "POST":
        accion = request.POST.get('accion')
        try:
            if accion == 'backup_completo':
                if not probar_conexion():
                    return JsonResponse({'error': 'No se puede conectar a MySQL. Verifica que el servidor esté en ejecución.'}, status=400)
                return realizar_respaldo_completo()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    mysql_ok = probar_conexion()
    context = {
        'titulo': 'Respaldo y Restauración de Base de Datos',
        'db_conectada': mysql_ok,
    }
    return render(request, 'backup/menu.html', context)

# ========== VISTA RESTAURAR ==========
@require_http_methods(["POST"])
def restaurar_datos(request):
    if 'archivo' not in request.FILES:
        return JsonResponse({'error': 'No se proporcionó archivo.'}, status=400)

    archivo = request.FILES['archivo']

    try:
        if not archivo.name.endswith('.sql'):
            return JsonResponse({'error': 'El archivo debe tener extensión .sql'}, status=400)

        contenido_sql = archivo.read().decode('utf-8')

        if not contenido_sql.strip():
            return JsonResponse({'error': 'El archivo SQL está vacío, selecciona un respaldo válido.'}, status=400)

        restaurar_bd_desde_sql(contenido_sql)

        return JsonResponse({
            'exito': True,
            'mensaje': 'Base de datos restaurada correctamente.'
        })

    except Exception as e:
        return JsonResponse({'error': f'Error al restaurar: {str(e)}'}, status=400)

# ========== REALIZAR RESPALDO ==========
def realizar_respaldo_completo():
    _asegurar_directorio()
    creds     = obtener_credenciales()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nombre    = f'backup_completo_{timestamp}.sql'
    destino   = os.path.join(BACKUP_DIR, nombre)

    try:
        cmd = [
            os.path.join(creds['mysql_path'], 'mysqldump.exe'),
            '-h', creds['host'],
            '-u', creds['user'],
            f"--password={creds['password']}",
            '-P', creds['port'],
            creds['database'],
        ]

        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if resultado.returncode != 0:
            raise Exception(f'Error mysqldump: {resultado.stderr}')

        sql_content = resultado.stdout
        if not sql_content.strip():
            raise Exception('El respaldo está vacío.')

        # Encabezado informativo
        sql_content = (
            f"-- Respaldo de {creds['database']}\n"
            f"-- Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"-- Tipo: Completo (Estructura + Datos)\n\n"
        ) + sql_content

        # Guardar copia local en /backups/
        with open(destino, 'w', encoding='utf-8') as f:
            f.write(sql_content)

        # Devolver como descarga al navegador
        response = HttpResponse(sql_content.encode('utf-8'), content_type='application/sql')
        response['Content-Disposition'] = f'attachment; filename="{nombre}"'
        return response

    except subprocess.TimeoutExpired:
        raise Exception('Timeout al ejecutar mysqldump.')
    except Exception as e:
        raise Exception(f'Error en respaldo: {str(e)}')

# ========== RESTAURAR DESDE SQL ==========
def restaurar_bd_desde_sql(contenido_sql):
    creds = obtener_credenciales()
    try:
        cmd = [
            os.path.join(creds['mysql_path'], 'mysql.exe'),
            '-h', creds['host'],
            '-u', creds['user'],
            f"--password={creds['password']}",
            '-P', creds['port'],
            creds['database'],
        ]

        proceso = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout, stderr = proceso.communicate(input=contenido_sql, timeout=120)

        if proceso.returncode != 0:
            raise Exception(f'Error MySQL: {stderr}')

        return True

    except subprocess.TimeoutExpired:
        raise Exception('Timeout al restaurar la base de datos.')
    except Exception as e:
        raise Exception(f'Error al restaurar: {str(e)}')