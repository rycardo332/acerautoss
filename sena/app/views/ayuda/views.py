import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import FileResponse, Http404
from django.conf import settings


@method_decorator(login_required, name='dispatch')
class AyudaView(View):
    def get(self, request):
        context = {
            'titulo': 'Centro de Ayuda',
        }
        return render(request, 'ayuda/ayuda.html', context)


@login_required
def descargar_manual(request, nombre):
    manuales = {
        'administrador': 'manuales/manual_administrador.pdf',
        'mecanico':      'manuales/manual_mecanico.pdf',
    }
    if nombre not in manuales:
        raise Http404

    ruta = os.path.join(settings.BASE_DIR, 'app', 'static', manuales[nombre])
    print("BUSCANDO:", ruta)
    print("EXISTE:", os.path.exists(ruta))
    if not os.path.exists(ruta):
        raise Http404

    return FileResponse(
        open(ruta, 'rb'),
        as_attachment=True,
        filename=f'manual_{nombre}.pdf',
        content_type='application/pdf'
    )