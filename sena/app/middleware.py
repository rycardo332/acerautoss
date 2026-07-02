from django.utils import timezone

INTERVALO_MINUTOS = 180


class AlertasAutomaticasMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and not request.path.startswith('/static/')
            and not request.path.startswith('/media/')
            and not request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        ):
            self._revisar_si_toca(request)

        return self.get_response(request)

    def _revisar_si_toca(self, request):
        ultima = request.session.get('ultima_revision_alertas')
        ahora  = timezone.now().isoformat()

        if ultima:
            from datetime import datetime
            try:
                dt_ultima  = datetime.fromisoformat(ultima)
                diferencia = (
                    timezone.now() - timezone.make_aware(dt_ultima.replace(tzinfo=None))
                    if dt_ultima.tzinfo is None
                    else timezone.now() - dt_ultima
                )
                if diferencia.total_seconds() < INTERVALO_MINUTOS * 60:
                    return
            except Exception:
                pass

        request.session['ultima_revision_alertas'] = ahora

        try:
            import threading
            from app.views.Notificacion.views import generar_notificaciones_automaticas
            t = threading.Thread(target=generar_notificaciones_automaticas)
            t.daemon = True
            t.start()
        except Exception as e:
            print(f"[MIDDLEWARE] ❌ Error: {e}")