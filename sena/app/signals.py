from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone
from .models import (
    Producto, Notificacion, DetalleOrdenProducto,
    Compra, Vehiculo, OrdenServicio, SeguimientoMantenimiento
)

CORREO_ADMIN = 'acerautos09@gmail.com'


# ══════════════════════════════════════════════════════════
#  UTILIDAD — Enviar correo HTML
# ══════════════════════════════════════════════════════════
def enviar_correo_html(subject, texto_plano, html):
    try:
        correo = EmailMultiAlternatives(
            subject    = subject,
            body       = texto_plano,
            from_email = settings.DEFAULT_FROM_EMAIL,
            to         = [CORREO_ADMIN],
        )
        correo.attach_alternative(html, "text/html")
        correo.send()
    except Exception:
        pass


def _html_base(color_borde, icono_svg, titulo, filas_html, pie_html=""):
    return f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f0ede8;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0ede8;padding:36px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0"
             style="background:#ffffff;border-radius:14px;overflow:hidden;
                    box-shadow:0 2px 20px rgba(0,0,0,.09);">
        <tr>
          <td style="background:#1a1a1a;padding:28px 32px;text-align:center;">
            <h2 style="margin:0;color:#d32f2f;font-size:1.6rem;font-weight:900;
                       letter-spacing:3px;text-transform:uppercase;">ACERAUTOS</h2>
            <p style="margin:6px 0 0;color:rgba(255,255,255,.4);
                      font-size:.68rem;letter-spacing:2px;text-transform:uppercase;">
              Centro Integral Automotriz
            </p>
            <div style="margin:14px auto 0;width:40px;height:3px;
                        background:#d32f2f;border-radius:2px;"></div>
          </td>
        </tr>
        <tr>
          <td style="background:{color_borde};padding:20px 32px;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="vertical-align:middle;padding-right:12px;">{icono_svg}</td>
                <td style="vertical-align:middle;">
                  <h1 style="margin:0;color:#fff;font-size:1.1rem;font-weight:800;letter-spacing:.5px;">
                    {titulo}
                  </h1>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:28px 32px;">
            <table width="100%" cellpadding="0" cellspacing="0"
                   style="border:1px solid #e8e4df;border-radius:10px;overflow:hidden;">
              {filas_html}
            </table>
            {pie_html}
          </td>
        </tr>
        <tr>
          <td style="background:#1a1a1a;padding:14px 32px;text-align:center;">
            <p style="margin:0;color:rgba(255,255,255,.35);font-size:.68rem;letter-spacing:.5px;">
              ACERAUTOS &mdash; Notificaci&oacute;n autom&aacute;tica &mdash; No responder este correo
            </p>
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""


def _fila(label, valor, ultimo=False):
    borde = "" if ultimo else "border-bottom:1px solid #f0ede8;"
    return f"""
    <tr>
      <td style="padding:11px 16px;{borde}background:#fafaf8;
                 font-size:.78rem;color:#999;font-weight:700;
                 text-transform:uppercase;letter-spacing:.5px;width:42%;">{label}</td>
      <td style="padding:11px 16px;{borde}font-size:.88rem;
                 color:#1a1a1a;font-weight:600;">{valor}</td>
    </tr>"""


SVG_ALERTA  = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
SVG_CRITICO = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'
SVG_MANT    = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93A10 10 0 115.93 19.07"/><polyline points="20 4 20 9 15 9"/></svg>'


# ══════════════════════════════════════════════════════════
#  1. ALERTA DE STOCK BAJO — al guardar Producto
# ══════════════════════════════════════════════════════════
@receiver(post_save, sender=Producto)
def verificar_stock_bajo(sender, instance, **kwargs):
    if instance.stock <= instance.stock_minimo:
        nivel  = "CRITICO" if instance.stock == 0 else "BAJO"
        color  = "#b71c1c" if nivel == "CRITICO" else "#d32f2f"
        icono  = SVG_CRITICO if nivel == "CRITICO" else SVG_ALERTA
        titulo = f"Stock {nivel} — {instance.nombre}"

        existe = Notificacion.objects.filter(
            titulo__icontains=instance.nombre,
            leido=False
        ).exists()

        if not existe:
            Notificacion.objects.create(
                tipo    = 'Alerta',
                origen  = 'SISTEMA',
                titulo  = titulo,
                mensaje = (
                    f"El producto '{instance.nombre}' tiene {instance.stock} unidades. "
                    f"Minimo recomendado: {instance.stock_minimo}."
                ),
            )
            filas = (
                _fila("Producto",       instance.nombre)
                + _fila("Stock actual", f"{instance.stock} unidades")
                + _fila("Stock minimo", f"{instance.stock_minimo} unidades")
                + _fila("Nivel",        nivel, ultimo=True)
            )
            pie = f"""
            <p style="margin:20px 0 0;padding:14px 16px;background:#fff5f5;
                      border-radius:8px;border-left:4px solid {color};
                      font-size:.82rem;color:#555;line-height:1.5;">
              Realice una orden de compra pronto para evitar
              quedarse sin inventario de este producto.
            </p>"""
            html = _html_base(color, icono, f"Alerta de inventario — {instance.nombre}", filas, pie)
            enviar_correo_html(
                subject     = f"Stock {nivel} — {instance.nombre}",
                texto_plano = f"Stock {nivel}: '{instance.nombre}' tiene {instance.stock} uds. Minimo: {instance.stock_minimo}.",
                html        = html,
            )


# ══════════════════════════════════════════════════════════
#  2. VERIFICAR STOCK BAJO AL USAR PRODUCTO EN ORDEN
# ══════════════════════════════════════════════════════════
@receiver(post_save, sender=DetalleOrdenProducto)
def verificar_stock_bajo_despues_uso(sender, instance, created, **kwargs):
    if created:
        producto = instance.producto
        if producto.stock <= producto.stock_minimo:
            nivel  = "CRITICO" if producto.stock == 0 else "BAJO"
            titulo = f"Stock {nivel} — {producto.nombre}"
            existe = Notificacion.objects.filter(titulo=titulo, leido=False).exists()
            if not existe:
                Notificacion.objects.create(
                    tipo    = 'Alerta',
                    origen  = 'SISTEMA',
                    titulo  = titulo,
                    mensaje = (
                        f"Stock {nivel}: '{producto.nombre}' tiene {producto.stock} unidades. "
                        f"Minimo: {producto.stock_minimo}."
                    ),
                )


# ══════════════════════════════════════════════════════════
#  3. DEVOLVER STOCK AL ELIMINAR DETALLE DE ORDEN
# ══════════════════════════════════════════════════════════
@receiver(post_delete, sender=DetalleOrdenProducto)
def devolver_stock_cancelacion(sender, instance, **kwargs):
    Producto.objects.filter(pk=instance.producto.pk).update(
        stock=instance.producto.stock + instance.cantidad
    )


# ══════════════════════════════════════════════════════════
#  4. MANTENIMIENTO — 
# ══════════════════════════════════════════════════════════
@receiver(post_save, sender=OrdenServicio)
def alerta_mantenimiento_vehiculo(sender, instance, **kwargs):
    pass


# ══════════════════════════════════════════════════════════
#  5. SEGUIMIENTO — 
# ══════════════════════════════════════════════════════════
@receiver(post_save, sender=OrdenServicio)
def crear_seguimiento_mantenimiento(sender, instance, created, **kwargs):
    pass