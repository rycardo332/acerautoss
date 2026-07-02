from django import forms
import re
from datetime import date
from django.db import transaction
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.utils import timezone
from django.utils.safestring import mark_safe
from .models import (
    ProveedorProducto,
    UsuarioSistema,
    Proveedor, Producto, Compra, CompraDetalle, Cliente, Marca, Vehiculo, Factura,
    TipoServicio, OrdenServicio,
    Notificacion, Caja, DetalleOrdenProducto, CompatibilidadProducto,
    SeguimientoMantenimiento,
)




# ══════════════════════════════════════════════════════════
#  WIDGETS PERSONALIZADOS
# ══════════════════════════════════════════════════════════

class SelectConEmoji(forms.Select):
    def create_option(self, name, value, label, selected, index, **kwargs):
        option = super().create_option(name, value, label, selected, index, **kwargs)
        option['label'] = mark_safe(label)
        return option

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/6.6.6/css/flag-icons.min.css',)
        }


class MultiServicioWidget(forms.MultipleHiddenInput):
    pass


# ══════════════════════════════════════════════════════════
#  INDICATIVOS Y PAÍSES
# ══════════════════════════════════════════════════════════

INDICATIVOS_PAISES = [
    ('',     '-- Indicativo --'),
    ('+57',  '🇨🇴 +57  Colombia'),
    ('+1',   '🇺🇸 +1   Estados Unidos / Canadá'),
    ('+52',  '🇲🇽 +52  México'),
    ('+54',  '🇦🇷 +54  Argentina'),
    ('+55',  '🇧🇷 +55  Brasil'),
    ('+56',  '🇨🇱 +56  Chile'),
    ('+51',  '🇵🇪 +51  Perú'),
    ('+58',  '🇻🇪 +58  Venezuela'),
    ('+593', '🇪🇨 +593 Ecuador'),
    ('+591', '🇧🇴 +591 Bolivia'),
    ('+595', '🇵🇾 +595 Paraguay'),
    ('+598', '🇺🇾 +598 Uruguay'),
    ('+507', '🇵🇦 +507 Panamá'),
    ('+506', '🇨🇷 +506 Costa Rica'),
    ('+503', '🇸🇻 +503 El Salvador'),
    ('+502', '🇬🇹 +502 Guatemala'),
    ('+504', '🇭🇳 +504 Honduras'),
    ('+505', '🇳🇮 +505 Nicaragua'),
    ('+53',  '🇨🇺 +53  Cuba'),
    ('+1809','🇩🇴 +1809 República Dominicana'),
    ('+34',  '🇪🇸 +34  España'),
    ('+44',  '🇬🇧 +44  Reino Unido'),
    ('+33',  '🇫🇷 +33  Francia'),
    ('+49',  '🇩🇪 +49  Alemania'),
    ('+39',  '🇮🇹 +39  Italia'),
    ('+351', '🇵🇹 +351 Portugal'),
    ('+7',   '🇷🇺 +7   Rusia'),
    ('+86',  '🇨🇳 +86  China'),
    ('+81',  '🇯🇵 +81  Japón'),
    ('+82',  '🇰🇷 +82  Corea del Sur'),
    ('+91',  '🇮🇳 +91  India'),
    ('+61',  '🇦🇺 +61  Australia'),
    ('+27',  '🇿🇦 +27  Sudáfrica'),
    ('+20',  '🇪🇬 +20  Egipto'),
    ('+212', '🇲🇦 +212 Marruecos'),
    ('+971', '🇦🇪 +971 Emiratos Árabes'),
    ('+966', '🇸🇦 +966 Arabia Saudita'),
]

PAISES = [
    ('',               '-- Seleccione un país --'),
    ('Alemania',       '<span class="fi fi-de"></span> Alemania'),
    ('Arabia Saudita', '<span class="fi fi-sa"></span> Arabia Saudita'),
    ('Argentina',      '<span class="fi fi-ar"></span> Argentina'),
    ('Australia',      '<span class="fi fi-au"></span> Australia'),
    ('Bolivia',        '<span class="fi fi-bo"></span> Bolivia'),
    ('Brasil',         '<span class="fi fi-br"></span> Brasil'),
    ('Canada',         '<span class="fi fi-ca"></span> Canadá'),
    ('Chile',          '<span class="fi fi-cl"></span> Chile'),
    ('China',          '<span class="fi fi-cn"></span> China'),
    ('Colombia',       '<span class="fi fi-co"></span> Colombia'),
    ('Corea del Sur',  '<span class="fi fi-kr"></span> Corea del Sur'),
    ('Costa Rica',     '<span class="fi fi-cr"></span> Costa Rica'),
    ('Cuba',           '<span class="fi fi-cu"></span> Cuba'),
    ('Ecuador',        '<span class="fi fi-ec"></span> Ecuador'),
    ('Egipto',         '<span class="fi fi-eg"></span> Egipto'),
    ('El Salvador',    '<span class="fi fi-sv"></span> El Salvador'),
    ('Emiratos Arabes','<span class="fi fi-ae"></span> Emiratos Árabes'),
    ('Espana',         '<span class="fi fi-es"></span> España'),
    ('Estados Unidos', '<span class="fi fi-us"></span> Estados Unidos'),
    ('Francia',        '<span class="fi fi-fr"></span> Francia'),
    ('Guatemala',      '<span class="fi fi-gt"></span> Guatemala'),
    ('Honduras',       '<span class="fi fi-hn"></span> Honduras'),
    ('India',          '<span class="fi fi-in"></span> India'),
    ('Italia',         '<span class="fi fi-it"></span> Italia'),
    ('Japon',          '<span class="fi fi-jp"></span> Japón'),
    ('Marruecos',      '<span class="fi fi-ma"></span> Marruecos'),
    ('Mexico',         '<span class="fi fi-mx"></span> México'),
    ('Nicaragua',      '<span class="fi fi-ni"></span> Nicaragua'),
    ('Panama',         '<span class="fi fi-pa"></span> Panamá'),
    ('Paraguay',       '<span class="fi fi-py"></span> Paraguay'),
    ('Peru',           '<span class="fi fi-pe"></span> Perú'),
    ('Portugal',       '<span class="fi fi-pt"></span> Portugal'),
    ('Reino Unido',    '<span class="fi fi-gb"></span> Reino Unido'),
    ('Rep. Dominicana','<span class="fi fi-do"></span> Rep. Dominicana'),
    ('Rusia',          '<span class="fi fi-ru"></span> Rusia'),
    ('Sudafrica',      '<span class="fi fi-za"></span> Sudáfrica'),
    ('Uruguay',        '<span class="fi fi-uy"></span> Uruguay'),
    ('Venezuela',      '<span class="fi fi-ve"></span> Venezuela'),
    ('Otro',           '🌍 Otro'),
]


# ══════════════════════════════════════════════════════════
#  REGLAS DE VALIDACIÓN DE TELÉFONO POR PAÍS
# ══════════════════════════════════════════════════════════

REGLAS_TELEFONO = {
    '+57': {
        'longitud': (7, 10),
        'prefijos': ['3','60','61','62','63','64','65','66','67','68'],
        'error_long': "Colombia (+57): ingrese 10 dígitos para celular (ej: 3101234567) o 7 para fijo (ej: 6012345).",
        'error_pref': "Colombia (+57): celular debe empezar por 3 (ej: 3101234567) o fijo por 60–68 (ej: 6012345).",
    },
    '+1': {
        'longitud': (10, 10),
        'prefijos': ['2','3','4','5','6','7','8','9'],
        'error_long': "EEUU/Canadá (+1): ingrese exactamente 10 dígitos (ej: 2125551234).",
        'error_pref': "EEUU/Canadá (+1): el primer dígito debe ser 2–9 (ej: 2125551234). El 0 y el 1 no son válidos.",
    },
    '+52': {
        'longitud': (10, 10),
        'prefijos': ['2','3','4','5','6','7','8','9'],
        'error_long': "México (+52): ingrese exactamente 10 dígitos (ej: 5512345678).",
        'error_pref': "México (+52): el primer dígito debe ser 2–9 (ej: 5512345678). Los números no comienzan por 0 ni 1.",
    },
    '+54': {
        'longitud': (6, 11),
        'prefijos': ['9','11','15','2','3'],
        'error_long': "Argentina (+54): 10–11 dígitos para móvil (ej: 91112345678) o 6–10 para fijo.",
        'error_pref': "Argentina (+54): móvil empieza por 9 (ej: 91112345678), fijo por 11/2xx/3xx.",
    },
    '+55': {
        'longitud': (8, 11),
        'prefijos': ['1','2','3','4','5','6','7','8','9'],
        'error_long': "Brasil (+55): incluya código de área (2 díg) + número. Móvil 11 díg (ej: 11987654321), fijo 10 díg.",
        'error_pref': "Brasil (+55): el número debe iniciar por código de área válido (11–99). No puede empezar por 0.",
    },
    '+56': {
        'longitud': (8, 9),
        'prefijos': ['2','3','4','5','6','7','9'],
        'error_long': "Chile (+56): móvil 9 dígitos (ej: 912345678) o fijo 8 dígitos.",
        'error_pref': "Chile (+56): móvil empieza por 9 (ej: 912345678), fijo por 2–7.",
    },
    '+51': {
        'longitud': (7, 9),
        'prefijos': ['1','9'],
        'error_long': "Perú (+51): móvil 9 dígitos (ej: 987654321) o fijo 7 dígitos (ej: 1234567).",
        'error_pref': "Perú (+51): móvil empieza por 9 (ej: 987654321) o fijo por 1 (Lima).",
    },
    '+58': {
        'longitud': (7, 11),
        'prefijos': ['0412','0414','0416','0424','0426','02'],
        'error_long': "Venezuela (+58): móvil 11 dígitos (ej: 04121234567) o fijo 7–10 dígitos empezando por 02.",
        'error_pref': "Venezuela (+58): móvil empieza por 0412/0414/0416/0424/0426 (ej: 04121234567), fijo por 02.",
    },
    '+593': {
        'longitud': (8, 9),
        'prefijos': ['09','02','03','04','05','06','07'],
        'error_long': "Ecuador (+593): móvil 9 dígitos (ej: 0987654321) o fijo 8 dígitos.",
        'error_pref': "Ecuador (+593): móvil empieza por 09 (ej: 0987654321), fijo por 02–07.",
    },
    '+591': {
        'longitud': (7, 8),
        'prefijos': ['2','3','4','6','7'],
        'error_long': "Bolivia (+591): móvil 8 dígitos (ej: 71234567) o fijo 7 dígitos.",
        'error_pref': "Bolivia (+591): móvil empieza por 6 o 7 (ej: 71234567), fijo por 2/3/4.",
    },
    '+595': {
        'longitud': (5, 9),
        'prefijos': ['09','02','03','04','05','06','07'],
        'error_long': "Paraguay (+595): móvil 9 dígitos (ej: 0981234567) o fijo 5–7 dígitos.",
        'error_pref': "Paraguay (+595): móvil empieza por 09 (ej: 0981234567), fijo por 02–07.",
    },
    '+598': {
        'longitud': (7, 8),
        'prefijos': ['09','2'],
        'error_long': "Uruguay (+598): móvil 8 dígitos (ej: 091234567) o fijo 7 dígitos.",
        'error_pref': "Uruguay (+598): móvil empieza por 09 (ej: 091234567), fijo por 2.",
    },
    '+507': {
        'longitud': (7, 8),
        'prefijos': ['2','3','4','5','6'],
        'error_long': "Panamá (+507): móvil 8 dígitos (ej: 61234567) o fijo 7 dígitos.",
        'error_pref': "Panamá (+507): móvil empieza por 6 (ej: 61234567), fijo por 2–5.",
    },
    '+506': {
        'longitud': (8, 8),
        'prefijos': ['2','5','6','7','8'],
        'error_long': "Costa Rica (+506): exactamente 8 dígitos (ej: 83456789).",
        'error_pref': "Costa Rica (+506): móvil empieza por 5/6/7/8 (ej: 83456789), fijo por 2.",
    },
    '+503': {
        'longitud': (8, 8),
        'prefijos': ['2','6','7'],
        'error_long': "El Salvador (+503): exactamente 8 dígitos (ej: 70123456).",
        'error_pref': "El Salvador (+503): móvil empieza por 6 o 7 (ej: 70123456), fijo por 2.",
    },
    '+502': {
        'longitud': (8, 8),
        'prefijos': ['2','3','4','5','6','7'],
        'error_long': "Guatemala (+502): exactamente 8 dígitos (ej: 51234567).",
        'error_pref': "Guatemala (+502): móvil empieza por 3/4/5 (ej: 51234567), fijo por 2/6/7.",
    },
    '+504': {
        'longitud': (8, 8),
        'prefijos': ['2','3','7','8','9'],
        'error_long': "Honduras (+504): exactamente 8 dígitos (ej: 91234567).",
        'error_pref': "Honduras (+504): móvil empieza por 3/7/8/9 (ej: 91234567), fijo por 2.",
    },
    '+505': {
        'longitud': (8, 8),
        'prefijos': ['2','5','6','7','8'],
        'error_long': "Nicaragua (+505): exactamente 8 dígitos (ej: 81234567).",
        'error_pref': "Nicaragua (+505): móvil empieza por 5/6/7/8 (ej: 81234567), fijo por 2.",
    },
    '+53': {
        'longitud': (7, 8),
        'prefijos': ['2','3','4','5'],
        'error_long': "Cuba (+53): móvil 8 dígitos (ej: 51234567) o fijo 7 dígitos.",
        'error_pref': "Cuba (+53): móvil empieza por 5 (ej: 51234567), fijo por 2/3/4.",
    },
    '+1809': {
        'longitud': (10, 10),
        'prefijos': ['809','829','849'],
        'error_long': "Rep. Dominicana (+1809): exactamente 10 dígitos (ej: 8091234567).",
        'error_pref': "Rep. Dominicana (+1809): debe empezar por 809, 829 o 849 (ej: 8091234567).",
    },
    '+34': {
        'longitud': (9, 9),
        'prefijos': ['6','7','8','9'],
        'error_long': "España (+34): exactamente 9 dígitos (ej: 612345678).",
        'error_pref': "España (+34): móvil empieza por 6 o 7 (ej: 612345678), fijo por 8 o 9.",
    },
    '+44': {
        'longitud': (7, 10),
        'prefijos': ['1','2','3','7'],
        'error_long': "Reino Unido (+44): 7–10 dígitos sin el 0 inicial (ej: 7911123456).",
        'error_pref': "Reino Unido (+44): sin el 0 inicial — móvil empieza por 7 (ej: 7911123456), fijo por 1/2/3.",
    },
    '+33': {
        'longitud': (9, 9),
        'prefijos': ['1','2','3','4','5','6','7'],
        'error_long': "Francia (+33): 9 dígitos sin el 0 inicial (ej: 612345678).",
        'error_pref': "Francia (+33): sin el 0 inicial — móvil empieza por 6 o 7 (ej: 612345678), fijo por 1–5.",
    },
    '+49': {
        'longitud': (3, 12),
        'prefijos': [],
        'error_long': "Alemania (+49): entre 3 y 12 dígitos según la región (ej móvil: 15123456789).",
        'error_pref': "",
    },
    '+39': {
        'longitud': (6, 11),
        'prefijos': ['0','3'],
        'error_long': "Italia (+39): móvil 10 dígitos (ej: 3201234567) o fijo 6–11 dígitos empezando por 0.",
        'error_pref': "Italia (+39): móvil empieza por 3 (ej: 3201234567), fijo por 0.",
    },
    '+351': {
        'longitud': (9, 9),
        'prefijos': ['2','9'],
        'error_long': "Portugal (+351): exactamente 9 dígitos (ej: 912345678).",
        'error_pref': "Portugal (+351): móvil empieza por 9 (ej: 912345678), fijo por 2.",
    },
    '+7': {
        'longitud': (10, 10),
        'prefijos': ['3','4','8','9'],
        'error_long': "Rusia (+7): exactamente 10 dígitos (ej: 9161234567).",
        'error_pref': "Rusia (+7): móvil empieza por 9 (ej: 9161234567), fijo por 3/4/8.",
    },
    '+86': {
        'longitud': (7, 11),
        'prefijos': ['1','2','3','4','5','6','7','8','9'],
        'error_long': "China (+86): móvil 11 dígitos (ej: 13812345678) o fijo 7–8 dígitos con código de área.",
        'error_pref': "China (+86): no puede empezar por 0. Móvil empieza por 1 (ej: 13812345678).",
    },
    '+81': {
        'longitud': (9, 10),
        'prefijos': ['0','7','8','9'],
        'error_long': "Japón (+81): 9–10 dígitos (ej móvil: 09012345678 → ingresar sin el 0: 9012345678).",
        'error_pref': "Japón (+81): móvil empieza por 070/080/090 (ej: 09012345678), fijo por código de área.",
    },
    '+82': {
        'longitud': (9, 11),
        'prefijos': ['0','1','2','3','4','5','6'],
        'error_long': "Corea del Sur (+82): 9–11 dígitos (ej móvil: 01012345678).",
        'error_pref': "Corea del Sur (+82): móvil empieza por 010 (ej: 01012345678), fijo por 02/031/…",
    },
    '+91': {
        'longitud': (10, 10),
        'prefijos': ['6','7','8','9'],
        'error_long': "India (+91): exactamente 10 dígitos (ej: 9876543210).",
        'error_pref': "India (+91): debe empezar por 6, 7, 8 o 9 (ej: 9876543210). No comienza por 0–5.",
    },
    '+61': {
        'longitud': (5, 9),
        'prefijos': ['2','3','4','7','8'],
        'error_long': "Australia (+61): móvil 9 dígitos (ej: 412345678) o fijo 8 dígitos, sin el 0 inicial.",
        'error_pref': "Australia (+61): sin el 0 inicial — móvil empieza por 4 (ej: 412345678), fijo por 2/3/7/8.",
    },
    '+27': {
        'longitud': (9, 9),
        'prefijos': ['1','2','3','4','5','6','7','8'],
        'error_long': "Sudáfrica (+27): exactamente 9 dígitos sin el 0 inicial (ej: 812345678).",
        'error_pref': "Sudáfrica (+27): sin el 0 inicial — móvil empieza por 6/7/8 (ej: 812345678), fijo por 1–5.",
    },
    '+20': {
        'longitud': (7, 10),
        'prefijos': ['01','02','03'],
        'error_long': "Egipto (+20): móvil 10 dígitos (ej: 0101234567) o fijo 8–9 dígitos.",
        'error_pref': "Egipto (+20): móvil empieza por 01 (ej: 0101234567), fijo por 02 o 03.",
    },
    '+212': {
        'longitud': (9, 10),
        'prefijos': ['05','06','07'],
        'error_long': "Marruecos (+212): 9–10 dígitos (ej: 0612345678).",
        'error_pref': "Marruecos (+212): móvil empieza por 06 o 07 (ej: 0612345678), fijo por 05.",
    },
    '+971': {
        'longitud': (7, 9),
        'prefijos': ['02','03','04','05','06','07','09'],
        'error_long': "Emiratos Árabes (+971): móvil 9 dígitos (ej: 0512345678) o fijo 7–8 dígitos.",
        'error_pref': "Emiratos Árabes (+971): móvil empieza por 05 (ej: 0512345678), fijo por 02/03/04/06/07/09.",
    },
    '+966': {
        'longitud': (9, 9),
        'prefijos': ['01','02','03','05'],
        'error_long': "Arabia Saudita (+966): exactamente 9 dígitos (ej: 0512345678).",
        'error_pref': "Arabia Saudita (+966): móvil empieza por 05 (ej: 0512345678), fijo por 01/02/03.",
    },
}

LONGITUDES_POR_INDICATIVO = {k: v['longitud'] for k, v in REGLAS_TELEFONO.items()}


# ══════════════════════════════════════════════════════════
#  UTILIDADES COMPARTIDAS
# ══════════════════════════════════════════════════════════

def _validar_numero_por_regla(numero, indicativo):
    """
    Valida número local según REGLAS_TELEFONO[indicativo].
    Lanza forms.ValidationError con el mensaje propio del país.
    Retorna el número limpio si es válido.
    Uso interno compartido por clean_numero_telefono y val_telefono_internacional.
    """
    numero_limpio = str(numero).strip()

    if not numero_limpio:
        raise forms.ValidationError("Ingrese el número de teléfono.")
    if not numero_limpio.isdigit():
        raise forms.ValidationError(
            "Solo se permiten dígitos, sin espacios, guiones ni símbolos."
        )

    regla = REGLAS_TELEFONO.get(indicativo)
    if not regla:
     
        if not (6 <= len(numero_limpio) <= 15):
            raise forms.ValidationError(
                f"Número inválido para {indicativo or 'indicativo no seleccionado'}: "
                f"debe tener entre 6 y 15 dígitos."
            )
        return numero_limpio

   
    min_d, max_d = regla['longitud']
    if not (min_d <= len(numero_limpio) <= max_d):
        raise forms.ValidationError(regla['error_long'])

    
    prefijos = regla.get('prefijos', [])
    if prefijos:
        sorted_p = sorted(prefijos, key=len, reverse=True)
        if not any(numero_limpio.startswith(p) for p in sorted_p):
            raise forms.ValidationError(regla['error_pref'])

    return numero_limpio


def val_telefono_internacional(indicativo, numero, campo):
    """
    Valida longitud + prefijo según el país del indicativo.
    Retorna '{indicativo}{numero}' si todo es válido.
    """
    if not indicativo:
        raise forms.ValidationError(f"'{campo}': seleccione el indicativo del país.")
    numero_limpio = _validar_numero_por_regla(numero, indicativo)
    return f"{indicativo}{numero_limpio}"


def val_solo_letras(valor, campo):
    if not re.match(r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$', str(valor).strip()):
        raise forms.ValidationError(f"'{campo}' solo permite letras y espacios, sin números ni símbolos.")
    return valor.strip()

def val_solo_numeros(valor, campo):
    limpio = str(valor).strip()
    if not limpio.isdigit():
        raise forms.ValidationError(f"'{campo}' solo permite números, sin letras ni símbolos.")
    return limpio

def val_placa_colombiana(valor):
    placa = str(valor).strip().upper().replace(" ", "")
    if not (re.match(r'^[A-Z]{3}[0-9]{3}$', placa) or re.match(r'^[A-Z]{3}[0-9]{2}[A-Z]{1}$', placa)):
        raise forms.ValidationError("Placa inválida. Use el formato ABC123 (carro) o ABC12D (moto).")
    numeros = re.findall(r'[0-9]+', placa)
    if numeros and numeros[0] == '000':
        raise forms.ValidationError("La placa no puede tener '000' como dígitos. Ej válido: ABC123.")
    return placa

def val_no_negativo(valor, campo):
    if valor < 0:
        raise forms.ValidationError(f"'{campo}' no puede ser un valor negativo.")
    return valor

def val_positivo(valor, campo):
    if valor <= 0:
        raise forms.ValidationError(f"'{campo}' debe ser mayor que 0.")
    return valor

def val_email(valor, campo):
    if not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$', str(valor).strip()):
        raise forms.ValidationError(f"'{campo}' no tiene un formato de correo válido. Ej: correo@dominio.com")
    return valor.strip().lower()

def val_telefono_colombiano(valor, campo):
    """Mantenida por compatibilidad — úsala solo para campos puramente colombianos."""
    limpio = str(valor).strip()
    if not limpio.isdigit():
        raise forms.ValidationError(f"'{campo}' solo permite números, sin espacios, guiones ni símbolos.")
    if len(limpio) == 10:
        if limpio.startswith('3') or limpio.startswith('60') or limpio.startswith('61'):
            return limpio
        raise forms.ValidationError(f"'{campo}': celular debe empezar por 3 o fijo con indicativo por 60/61.")
    elif len(limpio) == 7:
        return limpio
    raise forms.ValidationError(
        f"'{campo}' inválido. Use 10 dígitos para celular o 7 para fijo. Recibido: {len(limpio)} dígitos."
    )

def val_documento_colombiano(valor, campo, tipo_doc=None):
    limpio = str(valor).strip()
    if tipo_doc == 'CC':
        if not limpio.isdigit() or not (8 <= len(limpio) <= 14):
            raise forms.ValidationError(f"'{campo}': Cédula debe tener entre 8 y 14 dígitos.")
    elif tipo_doc == 'CE':
        if not limpio.isdigit() or not (8 <= len(limpio) <= 14):
            raise forms.ValidationError(f"'{campo}': Cédula de extranjería debe tener entre 8 y 14 dígitos.")
    elif tipo_doc == 'PAS':
        if not re.match(r'^[A-Z0-9]{5,12}$', limpio.upper()):
            raise forms.ValidationError(f"'{campo}': Pasaporte debe tener entre 5 y 12 caracteres alfanuméricos.")
    else:
        if not limpio.isdigit():
            raise forms.ValidationError(f"'{campo}' solo permite números.")
        if not (8 <= len(limpio) <= 14):
            raise forms.ValidationError(f"'{campo}' debe tener entre 8 y 14 dígitos.")
    return limpio


# ══════════════════════════════════════════════════════════
#  USUARIO SISTEMA
# ══════════════════════════════════════════════════════════

class UsuarioSistemaForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña", required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Mínimo 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña", required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = UsuarioSistema
        fields = ['username', 'first_name', 'last_name', 'email',
                  'tipo_documento', 'cedula', 'telefono', 'cargo',
                  'is_active', 'foto']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required  = True
        self.fields['email'].required      = True
        self.fields['foto'].required       = False  
        if self.instance.pk:
            self.fields['password1'].help_text = "Dejar vacío para no cambiar la contraseña."

    def clean_first_name(self):
        nombre = val_solo_letras(self.cleaned_data['first_name'], "Nombre")
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_last_name(self):
        apellido = val_solo_letras(self.cleaned_data['last_name'], "Apellido")
        if len(apellido) < 2:
            raise forms.ValidationError("El apellido debe tener al menos 2 caracteres.")
        return apellido

    def clean_email(self):
        email = val_email(self.cleaned_data['email'], "Email")
        qs = UsuarioSistema.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un usuario con este email.")
        return email

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if cedula:
            cedula = val_solo_numeros(cedula, "Cédula")
            if not (8 <= len(cedula) <= 14):
                raise forms.ValidationError("La cédula debe tener entre 8 y 14 dígitos.")
            qs = UsuarioSistema.objects.filter(cedula=cedula)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe un usuario con esta cédula.")
        return cedula

    def clean_password1(self):
        password = self.cleaned_data.get('password1', '')
        if not password and self.instance.pk:
            return password
        if password:
            if len(password) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
            if not re.search(r'[A-Z]', password):
                raise forms.ValidationError("Debe tener al menos una letra mayúscula.")
            if not re.search(r'[a-z]', password):
                raise forms.ValidationError("Debe tener al menos una letra minúscula.")
            if not re.search(r'[0-9]', password):
                raise forms.ValidationError("Debe tener al menos un número.")
            if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>\/?]', password):
                raise forms.ValidationError("Debe tener al menos un carácter especial. Ej: !@#$%&*")
        return password

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1', '')
        p2 = cleaned.get('password2', '')
        if p1 and p1 != p2:
            self.add_error('password2', "Las contraseñas no coinciden.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        elif not self.instance.pk:
            user.set_unusable_password()
        if commit:
            user.save()
        return user


# ══════════════════════════════════════════════════════════
#  PROVEEDOR
# ══════════════════════════════════════════════════════════

class ProveedorForm(forms.ModelForm):
    indicativo_telefono = forms.ChoiceField(
        choices=INDICATIVOS_PAISES, required=True, label="Indicativo",
        widget=forms.HiddenInput()
    )
    numero_telefono = forms.CharField(
        max_length=15, required=True, label="Teléfono",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = Proveedor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.telefono:
            tel = self.instance.telefono
            for code, _ in INDICATIVOS_PAISES:
                if code and tel.startswith(code):
                    self.fields['indicativo_telefono'].initial = code
                    self.fields['numero_telefono'].initial = tel[len(code):]
                    break
            else:
                self.fields['indicativo_telefono'].initial = '+57'
                self.fields['numero_telefono'].initial = tel

    def clean_nombre(self):
        nombre = val_solo_letras(self.cleaned_data['nombre'], "Nombre del proveedor")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del proveedor debe tener al menos 3 caracteres.")
        return nombre

    def clean_nit(self):
        nit = val_solo_numeros(self.cleaned_data['nit'], "NIT")
        if not (9 <= len(nit) <= 10):
            raise forms.ValidationError("El NIT debe tener 9 o 10 dígitos.")
        if int(nit) <= 0:
            raise forms.ValidationError("El NIT debe ser mayor que 0.")
        if len(set(nit)) == 1:
            raise forms.ValidationError("El NIT no puede tener todos los dígitos iguales.")
        qs = Proveedor.objects.filter(nit=nit)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un proveedor registrado con este NIT.")
        return nit

    def clean_numero_telefono(self):
        numero     = self.cleaned_data.get('numero_telefono', '').strip()
        indicativo = self.data.get('indicativo_telefono', '').strip()
        _validar_numero_por_regla(numero, indicativo)
        return numero

    def clean_telefono(self):
        return self.cleaned_data.get('telefono')

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion', '').strip()
        if direccion and len(direccion) < 5:
            raise forms.ValidationError("La dirección es demasiado corta (mínimo 5 caracteres).")
        return direccion

    def clean(self):
        cleaned    = super().clean()
        indicativo = cleaned.get('indicativo_telefono', '')
        numero     = cleaned.get('numero_telefono', '')
        if indicativo and numero:
            telefono_completo = f"{indicativo}{numero}"
            cleaned['telefono'] = telefono_completo
            qs = Proveedor.objects.filter(telefono=telefono_completo)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error('numero_telefono', "Ya existe un proveedor registrado con este teléfono.")
        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            instance.telefono = telefono
        if commit:
            instance.save()
        return instance


# ══════════════════════════════════════════════════════════
#  PROVEEDOR PRODUCTO FORMSET
# ══════════════════════════════════════════════════════════

class ProveedorProductoForm(forms.ModelForm):
    class Meta:
        model  = ProveedorProducto
        fields = ['producto', 'precio_proveedor']
        widgets = {
            'producto':         forms.Select(attrs={'class': 'form-field-styled'}),
            'precio_proveedor': forms.NumberInput(attrs={'class': 'form-field-styled', 'placeholder': 'Precio del proveedor'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].required         = False
        self.fields['precio_proveedor'].required = False

class BaseProveedorProductoFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            if form.cleaned_data.get('DELETE'):
                continue
            producto = form.cleaned_data.get('producto')
            precio   = form.cleaned_data.get('precio_proveedor')
            if not producto and not precio:
                continue
            if producto and not precio:
                form.add_error('precio_proveedor', 'Ingresa el precio para este producto.')
            if precio and not producto:
                form.add_error('producto', 'Selecciona un producto.')

ProveedorProductoFormSet = inlineformset_factory(
    Proveedor,
    ProveedorProducto,
    form=ProveedorProductoForm,
    formset=BaseProveedorProductoFormSet,
    extra=1,
    can_delete=True,
    min_num=0,
    validate_min=False,
)
# ══════════════════════════════════════════════════════════
#  MARCA
# ══════════════════════════════════════════════════════════

class MarcaForm(forms.ModelForm):
    pais_origen = forms.ChoiceField(
        choices=PAISES, required=False, label="País de origen",
        widget=SelectConEmoji(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = Marca
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not re.match(r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ0-9\s\-]+$', nombre):
            raise forms.ValidationError("El nombre solo permite letras, números, espacios y guiones.")
        if nombre and nombre[0].isdigit():
            raise forms.ValidationError("El nombre de la marca no puede iniciar con un número.")
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_pais_origen(self):
        return self.cleaned_data.get('pais_origen', '') or ''

    def clean_descripcion(self):
        desc = self.cleaned_data.get('descripcion', '').strip()
        if desc:
            if len(desc) < 5:
                raise forms.ValidationError("La descripción es demasiado corta (mínimo 5 caracteres).")
            if len(desc) > 200:
                raise forms.ValidationError("La descripción no puede superar 200 caracteres.")
        return desc

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo and hasattr(logo, 'name'):
            ext = logo.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                raise forms.ValidationError("Solo se permiten imágenes JPG, PNG o WEBP.")
            if logo.size > 2 * 1024 * 1024:
                raise forms.ValidationError("La imagen no puede superar los 2 MB.")
        return logo


# ══════════════════════════════════════════════════════════
#  PRODUCTO
# ══════════════════════════════════════════════════════════

class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].queryset = Marca.objects.filter(categoria='REPUESTO', estado=True)
        if self.instance.pk:
            self.fields['stock'].widget.attrs['readonly'] = True
            self.fields['stock'].widget.attrs['style']    = 'background:#f1f5f9;cursor:not-allowed;color:#888;'
            self.fields['stock'].help_text = '⚠ El stock solo se actualiza desde el módulo de Compras.'
        else:
            self.fields['stock'].initial = 0
            self.fields['stock'].widget.attrs['readonly'] = True
            self.fields['stock'].widget.attrs['style']    = 'background:#f1f5f9;cursor:not-allowed;color:#888;'
            self.fields['stock'].help_text = 'Arranca en 0. Se actualizará automáticamente desde el módulo de Compras.'

    def clean_codigo(self):
        codigo = val_solo_numeros(self.cleaned_data['codigo'], "Código")
        if len(codigo) < 3:
            raise forms.ValidationError("El código debe tener al menos 3 dígitos.")
        qs = Producto.objects.filter(codigo=codigo)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un producto con este código.")
        return codigo

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del producto debe tener al menos 3 caracteres.")
        qs = Producto.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un producto con este nombre.")
        return nombre

    def clean_precio(self):
        precio = val_positivo(self.cleaned_data['precio'], "Precio")
        if precio > 99999999:
            raise forms.ValidationError("El precio ingresado es demasiado alto.")
        return precio

    def clean_stock(self):
        if self.instance.pk:
            return self.instance.stock
        return 0

    def clean_stock_minimo(self):
        return val_no_negativo(self.cleaned_data['stock_minimo'], "Stock mínimo")

    def clean(self):
        cleaned   = super().clean()
        stock     = self.instance.stock if self.instance.pk else 0
        stock_min = cleaned.get('stock_minimo')
        if stock_min is not None and stock_min > stock and stock > 0:
            self.add_error(
                'stock_minimo',
                f"El stock mínimo ({stock_min}) no puede ser mayor al stock actual ({stock})."
            )
        return cleaned


import re

# ══════════════════════════════════════════════════════════
#  COMPRA
# ══════════════════════════════════════════════════════════

class CompraForm(forms.ModelForm):
    class Meta:
        model  = Compra
        fields = ['proveedor', 'num_factura_proveedor', 'archivo_factura']

    def clean_num_factura_proveedor(self):
        nf = self.cleaned_data['num_factura_proveedor'].strip()
        if not nf:
            raise forms.ValidationError("El número de factura es obligatorio.")
        if len(nf) < 3:
            raise forms.ValidationError("El número de factura debe tener al menos 3 caracteres.")
        if len(nf) > 20:
            raise forms.ValidationError("El número de factura no puede superar 20 caracteres.")
        if not re.match(r'^[a-zA-Z0-9\-]+$', nf):
            raise forms.ValidationError("El número de factura solo puede contener letras, números y guiones.")
        qs = Compra.objects.filter(num_factura_proveedor=nf)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe una compra registrada con este número de factura.")
        return nf


# ══════════════════════════════════════════════════════════
#  COMPRA DETALLE
# ══════════════════════════════════════════════════════════

class CompraDetalleForm(forms.ModelForm):
    class Meta:
        model  = CompraDetalle
        fields = ['producto', 'cantidad', 'precio_unitario']

    def __init__(self, *args, **kwargs):
        self.proveedor_id = kwargs.pop('proveedor_id', None)
        super().__init__(*args, **kwargs)

        proveedor_id = self.proveedor_id
        if not proveedor_id and self.instance.pk and self.instance.compra_id:
            proveedor_id = self.instance.compra.proveedor_id
        elif not proveedor_id and self.data.get('proveedor'):
            proveedor_id = self.data.get('proveedor')

        if proveedor_id:
            ids = ProveedorProducto.objects.filter(
                proveedor_id=proveedor_id
            ).values_list('producto_id', flat=True)
            self.fields['producto'].queryset = Producto.objects.filter(id__in=ids, estado=True)
        else:
            self.fields['producto'].queryset = Producto.objects.none()

    def clean_cantidad(self):
        cantidad = val_positivo(self.cleaned_data['cantidad'], "Cantidad")
        if cantidad > 10000:
            raise forms.ValidationError("La cantidad no puede superar 10.000 unidades por producto.")
        return cantidad

    def clean_precio_unitario(self):
        precio = val_no_negativo(self.cleaned_data['precio_unitario'], "Precio unitario")
        if precio > 999999999:
            raise forms.ValidationError("El precio unitario es demasiado alto. Verifique el valor.")
        return precio


class BaseCompraDetalleFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return

        productos_vistos    = []
        formularios_validos = 0

        for form in self.forms:
            if not hasattr(form, 'cleaned_data') or not form.cleaned_data:
                continue
            if form.cleaned_data.get('DELETE'):
                continue

            producto = form.cleaned_data.get('producto')
            if not producto:
                continue

            formularios_validos += 1

            if producto in productos_vistos:
                form.add_error('producto', "Este producto ya fue agregado en otra fila.")
            productos_vistos.append(producto)

        if formularios_validos == 0:
            raise forms.ValidationError("Debes agregar al menos un producto a la compra.")


CompraDetalleFormSet = inlineformset_factory(
    Compra,
    CompraDetalle,
    form=CompraDetalleForm,
    formset=BaseCompraDetalleFormSet,
    fields=['producto', 'cantidad', 'precio_unitario'],
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

# ══════════════════════════════════════════════════════════
#  CLIENTE
# ══════════════════════════════════════════════════════════

class ClienteForm(forms.ModelForm):
    indicativo_telefono = forms.ChoiceField(
        choices=INDICATIVOS_PAISES, required=True, label="Indicativo",
        widget=forms.HiddenInput()
    )
    numero_telefono = forms.CharField(
        max_length=15, required=True, label="Teléfono",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.telefono:
            tel = self.instance.telefono
            for code, _ in INDICATIVOS_PAISES:
                if code and tel.startswith(code):
                    self.fields['indicativo_telefono'].initial = code
                    self.fields['numero_telefono'].initial = tel[len(code):]
                    break
            else:
                self.fields['indicativo_telefono'].initial = '+57'
                self.fields['numero_telefono'].initial = tel

    def clean_nombre(self):
        nombre = val_solo_letras(self.cleaned_data['nombre'], "Nombre del cliente")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_numero_documento(self):
        tipo_doc = self.cleaned_data.get('tipo_documento', 'CC')
        doc      = self.cleaned_data['numero_documento'].strip()
        doc      = val_documento_colombiano(doc, "Número de documento", tipo_doc)
        qs = Cliente.objects.filter(numero_documento=doc)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un cliente registrado con este número de documento.")
        return doc

    def clean_numero_telefono(self):
        """
        Valida el número local según el indicativo seleccionado.
        Usa REGLAS_TELEFONO para dar el mensaje correcto por país.
        """
        numero     = self.cleaned_data.get('numero_telefono', '').strip()
        indicativo = self.data.get('indicativo_telefono', '').strip()
        _validar_numero_por_regla(numero, indicativo)
        return numero

    def clean_telefono(self):
        return self.cleaned_data.get('telefono')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = val_email(email, "Email")
            qs = Cliente.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe un cliente registrado con este email.")
        return email

    def clean(self):
        cleaned    = super().clean()
        indicativo = cleaned.get('indicativo_telefono', '')
        numero     = cleaned.get('numero_telefono', '')
        if indicativo and numero:
            telefono_completo = f"{indicativo}{numero}"
            cleaned['telefono'] = telefono_completo
            qs = Cliente.objects.filter(telefono=telefono_completo)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error('numero_telefono', "Ya existe un cliente registrado con este teléfono.")
        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            instance.telefono = telefono
        if commit:
            instance.save()
        return instance


# ══════════════════════════════════════════════════════════
#  VEHÍCULO
# ══════════════════════════════════════════════════════════

class VehiculoForm(forms.ModelForm):
    class Meta:
        model  = Vehiculo
        fields = ['placa', 'modelo', 'marca', 'cliente', 'tipo_uso']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].queryset = Marca.objects.filter(categoria='AUTO', estado=True)
        self.fields['placa'].label     = "Placa del Vehículo"
        self.fields['placa'].help_text = "Ej: ABC123 o ABC12D"
        self.fields['placa'].widget.attrs.update({'placeholder': 'ABC123'})
        self.fields['marca'].label   = "Marca"
        self.fields['cliente'].label = "Propietario"
        self.fields['modelo'].label     = "Año del Vehículo"
        self.fields['modelo'].help_text = "Ej: 2020"
        self.fields['modelo'].widget.attrs.update({'placeholder': '2020'})
        self.fields['tipo_uso'].required  = True
        self.fields['tipo_uso'].label     = "¿Cómo se usa este vehículo?"
        self.fields['tipo_uso'].help_text = "Ayuda a estimar el próximo mantenimiento"

    def clean_placa(self):
        placa = val_placa_colombiana(self.cleaned_data['placa'])
        qs = Vehiculo.objects.filter(placa=placa)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(f"Ya existe un vehículo con la placa '{placa}'.")
        return placa

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo'].strip()
        if not re.match(r'^\d{4}$', modelo):
            raise forms.ValidationError("El año debe tener exactamente 4 dígitos. Ej: 2019")
        anio = int(modelo)
        if anio < 1900 or anio > date.today().year:
            raise forms.ValidationError(f"El año debe estar entre 1900 y {date.today().year}.")
        return modelo

    

# ══════════════════════════════════════════════════════════
#  TIPO DE SERVICIO
# ══════════════════════════════════════════════════════════
class TipoServicioForm(forms.ModelForm):
    class Meta:
        model  = TipoServicio
        fields = ['nombre', 'descripcion', 'precio_mano_obra', 'estado', 'requiere_seguimiento', 'requiere_productos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre del Servicio"
        self.fields['nombre'].help_text = "Ej: Cambio de aceite y filtro"
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Ej: Cambio de aceite y filtro'})
        self.fields['descripcion'].label = "Descripción (Opcional)"
        self.fields['descripcion'].widget = forms.Textarea(attrs={'placeholder': 'Ej: Cambio de aceite sintético 5W-30', 'rows': 3})
        self.fields['precio_mano_obra'].label = "Precio de Mano de Obra"
        self.fields['precio_mano_obra'].widget.attrs.update({'placeholder': '35000'})
        self.fields['estado'].label = "¿Está disponible?"
        self.fields['requiere_seguimiento'].label = "¿Requiere seguimiento de mantenimiento?"
        self.fields['requiere_seguimiento'].help_text = "Actívalo para servicios como cambio de aceite — pedirá fecha del próximo mantenimiento al crear una orden."
        self.fields['requiere_productos'].label = "¿Requiere productos obligatorios?"
        self.fields['requiere_productos'].help_text = "Actívalo para exigir al menos un producto en la orden (ej: cambio de aceite)."

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if not re.match(r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ0-9\s\-\/]+$', nombre):
            raise forms.ValidationError("El nombre solo permite letras, números, espacios, guiones y barras.")
        qs = TipoServicio.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un tipo de servicio con este nombre.")
        return nombre

    def clean_precio_mano_obra(self):
        precio = val_positivo(self.cleaned_data['precio_mano_obra'], "Precio de mano de obra")
        if precio > 99999999:
            raise forms.ValidationError("El precio de mano de obra es demasiado alto.")
        return precio


# ══════════════════════════════════════════════════════════
#  ORDEN DE SERVICIO
# ══════════════════════════════════════════════════════════

class OrdenServicioForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset      = TipoServicio.objects.filter(estado=True),
        required      = True,
        label         = "Servicios",
        widget        = forms.CheckboxSelectMultiple(),
        error_messages= {'required': "Debe seleccionar al menos un servicio."},
    )
    fecha_proximo_mantenimiento = forms.DateField(
        required  = False,
        label     = "Fecha próximo mantenimiento",
        widget    = forms.DateInput(attrs={'type': 'date'}),
        help_text = "Solo aparece si el servicio requiere seguimiento."
    )

    class Meta:
        model  = OrdenServicio
        fields = ['empleado', 'vehiculo', 'servicios', 'fecha', 'km_actual', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empleado'].queryset    = UsuarioSistema.objects.filter(cargo='MECANICO', activo=True).order_by('first_name', 'last_name')
        self.fields['empleado'].required    = False
        self.fields['empleado'].empty_label = "-- Sin asignar --"
        self.fields['servicios'].queryset   = TipoServicio.objects.filter(estado=True).order_by('nombre')

        if self.instance and self.instance.pk:
            
            self.fields['vehiculo'].queryset = Vehiculo.objects.filter(
                Q(marca__estado=True) | Q(pk=self.instance.vehiculo_id)
            )
        else:
            # Crear: solo vehículos cuya marca esté activa
            self.fields['vehiculo'].queryset = Vehiculo.objects.filter(marca__estado=True)

        self.fields['km_actual'].required = False

    def clean_fecha_proximo_mantenimiento(self):
        fecha     = self.cleaned_data.get('fecha_proximo_mantenimiento')
        servicios = self.cleaned_data.get('servicios')
        if servicios and servicios.filter(requiere_seguimiento=True).exists():
            if not fecha:
                raise forms.ValidationError("Este servicio requiere la fecha del próximo mantenimiento.")
            if fecha < timezone.now().date():
                raise forms.ValidationError("La fecha del próximo mantenimiento debe ser futura.")
        return fecha

    def clean_servicios(self):
        servicios = self.cleaned_data.get('servicios')
        if not servicios:
            raise forms.ValidationError("Debe seleccionar al menos un servicio.")
        return servicios

    def clean_km_actual(self):
        km = self.cleaned_data.get('km_actual')
        if km is None:
            return km

        if not isinstance(km, int):
            raise forms.ValidationError("El kilometraje debe ser un número entero, sin decimales.")
        if km < 0:
            raise forms.ValidationError("El kilometraje no puede ser negativo.")
        if km == 0:
            raise forms.ValidationError("El kilometraje debe ser mayor que 0.")
        if km > 1000000:
            raise forms.ValidationError("El kilometraje ingresado es demasiado alto (máx. 1.000.000 km).")

        vehiculo = self.cleaned_data.get('vehiculo') or (
            self.instance.vehiculo if self.instance and self.instance.pk else None
        )
        if vehiculo:
            ultima_orden = OrdenServicio.objects.filter(
                vehiculo=vehiculo
            ).exclude(
                pk=self.instance.pk if self.instance and self.instance.pk else None
            ).order_by('-km_actual').first()

            if ultima_orden and ultima_orden.km_actual is not None and km < ultima_orden.km_actual:
                raise forms.ValidationError(
                    f"El km ingresado ({km:,}) no puede ser menor al registrado "
                    f"en la última orden (#{ultima_orden.pk}: {ultima_orden.km_actual:,} km)."
                )
        return km

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        estados_validos = [e[0] for e in OrdenServicio.ESTADOS]
        if estado not in estados_validos:
            raise forms.ValidationError(f"Estado no válido. Opciones: {', '.join(estados_validos)}.")
        if estado == 'Terminado':
            raise forms.ValidationError(
                "El estado 'Terminado' se asigna automáticamente al pagar la factura, no se puede seleccionar manualmente."
            )
        if self.instance.pk and self.instance.estado == 'Terminado':
            raise forms.ValidationError("Esta orden ya está terminada y no puede modificarse.")
        return estado

    def clean(self):
        cleaned   = super().clean()
        vehiculo  = cleaned.get('vehiculo')
        estado    = cleaned.get('estado')
        servicios = cleaned.get('servicios')
        km        = cleaned.get('km_actual')

        requiere_seguimiento = bool(servicios and servicios.filter(requiere_seguimiento=True).exists())

        if requiere_seguimiento and km is None:
            self.add_error('km_actual', "Este servicio requiere registrar el kilometraje actual.")
        elif not requiere_seguimiento:
            cleaned['km_actual'] = None

        if self.instance.pk and self.instance.estado == 'Terminado':
            raise forms.ValidationError("Esta orden ya está terminada y no puede modificarse.")
        if vehiculo and not self.instance.pk:
            orden_activa = OrdenServicio.objects.filter(
                vehiculo=vehiculo, estado__in=['Pendiente', 'En Proceso']
            ).first()
            if orden_activa:
                self.add_error('vehiculo',
                    f"El vehículo '{vehiculo.placa}' tiene una orden activa "
                    f"(#{orden_activa.pk} - {orden_activa.estado}). Finalícela antes de crear una nueva."
                )
        return cleaned
# ══════════════════════════════════════════════════════════
#  SEGUIMIENTO MANTENIMIENTO 
# ══════════════════════════════════════════════════════════

class SeguimientoMantenimientoForm(forms.ModelForm):
    class Meta:
        model  = SeguimientoMantenimiento
        fields = [
            'vehiculo', 'orden_servicio', 'tipo_servicio',
            'km_al_momento', 'km_proximo_mantenimiento',
            'fecha_proximo_mantenimiento', 'estado', 'observaciones',
        ]
        widgets = {
            'fecha_proximo_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_servicio'].required           = False
        self.fields['tipo_servicio'].required            = False
        self.fields['km_proximo_mantenimiento'].required = False
        self.fields['observaciones'].required            = False
        self.fields['fecha_proximo_mantenimiento'].required = True
        self.fields['vehiculo'].label                       = "Vehículo"
        self.fields['km_al_momento'].label                  = "Km actuales del vehículo"
        self.fields['km_proximo_mantenimiento'].label       = "Km para el próximo mantenimiento (opcional)"
        self.fields['fecha_proximo_mantenimiento'].label    = "Fecha del próximo mantenimiento"

    def clean_fecha_proximo_mantenimiento(self):
        fecha = self.cleaned_data.get('fecha_proximo_mantenimiento')
        if fecha and fecha <= timezone.now().date():
            raise forms.ValidationError("La fecha del próximo mantenimiento debe ser futura.")
        return fecha

    def clean_km_proximo_mantenimiento(self):
        km_prox   = self.cleaned_data.get('km_proximo_mantenimiento')
        km_actual = self.cleaned_data.get('km_al_momento')
        if km_prox and km_actual and km_prox <= km_actual:
            raise forms.ValidationError(
                f"El km del próximo mantenimiento ({km_prox:,}) debe ser mayor al actual ({km_actual:,})."
            )
        return km_prox


# ══════════════════════════════════════════════════════════
#  DETALLE ORDEN PRODUCTO
# ══════════════════════════════════════════════════════════

class DetalleOrdenProductoForm(forms.ModelForm):
    class Meta:
        model  = DetalleOrdenProducto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(stock__gt=0, estado=True)

    def clean_cantidad(self):
        cantidad = val_positivo(self.cleaned_data['cantidad'], "Cantidad")
        if cantidad > 1000:
            raise forms.ValidationError("La cantidad no puede superar 1.000 unidades por detalle.")
        return cantidad

    def clean(self):
        cleaned  = super().clean()
        producto = cleaned.get('producto')
        cantidad = cleaned.get('cantidad')
        if producto and cantidad:
            if cantidad > producto.stock:
                raise forms.ValidationError(
                    f"Stock insuficiente para '{producto.nombre}'. "
                    f"Disponible: {producto.stock}, solicitado: {cantidad}."
                )
        return cleaned


# ══════════════════════════════════════════════════════════
#  COMPATIBILIDAD PRODUCTO
# ══════════════════════════════════════════════════════════

class CompatibilidadProductoForm(forms.ModelForm):
    class Meta:
        model  = CompatibilidadProducto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset         = Producto.objects.filter(estado=True)
        self.fields['marca_vehiculo'].queryset   = Marca.objects.filter(categoria='AUTO', estado=True)
        self.fields['tipo_servicio'].required    = False
        self.fields['tipo_servicio'].empty_label = "-- Aplica para cualquier servicio --"

    def clean(self):
        cleaned        = super().clean()
        producto       = cleaned.get('producto')
        marca_vehiculo = cleaned.get('marca_vehiculo')
        tipo_servicio  = cleaned.get('tipo_servicio')
        if producto and marca_vehiculo:
            qs = CompatibilidadProducto.objects.filter(
                producto=producto, marca_vehiculo=marca_vehiculo, tipo_servicio=tipo_servicio
            )
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    f"Ya existe la compatibilidad entre '{producto.nombre}', "
                    f"'{marca_vehiculo.nombre}' y el servicio seleccionado."
                )
        return cleaned


# ══════════════════════════════════════════════════════════
#  CAJA
# ══════════════════════════════════════════════════════════

class CajaForm(forms.ModelForm):
    class Meta:
        model   = Caja
        exclude = ['descripcion']

    def clean_monto(self):
        monto = val_positivo(self.cleaned_data['monto'], "Monto")
        if monto > 999999999:
            raise forms.ValidationError("El monto es demasiado alto. Verifique el valor.")
        return monto

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha > timezone.now():
            raise forms.ValidationError("La fecha del movimiento no puede ser una fecha futura.")
        return fecha

    def clean_comprobante(self):
        archivo = self.cleaned_data.get('comprobante')
        if archivo:
            ext = archivo.name.split('.')[-1].lower()
            if ext not in ['pdf', 'jpg', 'jpeg', 'png']:
                raise forms.ValidationError("Solo se permiten archivos PDF, JPG o PNG.")
            if archivo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("El archivo no puede superar los 5 MB.")
        return archivo

    def clean_observaciones(self):
        obs = self.cleaned_data.get('observaciones', '').strip()
        if obs and len(obs) < 10:
            raise forms.ValidationError("Las observaciones son demasiado cortas (mínimo 10 caracteres).")
        return obs or None

class NotificacionForm(forms.ModelForm):
    TIPOS_NOTIFICACION = [
        ('',             '-- Seleccione un tipo --'),
        ('Alerta',       'Alerta'),
        ('Recordatorio', 'Recordatorio'),
        ('Mantenimiento','Mantenimiento'),
        ('Urgente',      'Urgente'),
        ('Informacion',  'Información'),
    ]
    tipo = forms.ChoiceField(
        choices=TIPOS_NOTIFICACION,
        label="Tipo de Notificación",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = Notificacion
        fields = ['tipo', 'titulo', 'vehiculo', 'mensaje', 'leido', 'fecha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehiculo'].required    = False
        self.fields['vehiculo'].empty_label = "-- Sin vehículo asociado --"
        self.fields['vehiculo'].widget.attrs.update({'required': False})
        self.fields['titulo'].required      = False
        self.fields['titulo'].help_text     = "Opcional. Resumen corto de la notificación."
        self.fields['leido'].initial        = False

        hoy = timezone.now().date()
        max_fecha = hoy.replace(year=hoy.year + 2)  # ── límite 2 años

        if 'fecha' in self.fields:
            self.fields['fecha'].widget = forms.DateInput(attrs={
                'type':  'date',
                'class': 'form-control',
                'id':    'id_fecha',
                'min':   hoy.strftime('%Y-%m-%d'),
                'max':   max_fecha.strftime('%Y-%m-%d'),  # ── NUEVO
            })

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha:
            hoy = timezone.now().date()
            if fecha < hoy:
                dias_atras = (hoy - fecha).days
                raise forms.ValidationError(
                    f"No se pueden registrar notificaciones con fechas pasadas. "
                    f"Esta fecha fue hace {dias_atras} día{'s' if dias_atras != 1 else ''}."
                )
            limite = hoy.replace(year=hoy.year + 2)  # ── NUEVO
            if fecha > limite:
                raise forms.ValidationError(
                    "La fecha no puede ser mayor a 2 años desde hoy."
                )
        return fecha

    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if not tipo:
            raise forms.ValidationError("Seleccione un tipo de notificación.")
        tipos_validos = [t[0] for t in self.TIPOS_NOTIFICACION if t[0]]
        if tipo not in tipos_validos:
            raise forms.ValidationError("Tipo de notificación no válido.")
        return tipo

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if titulo and len(titulo) > 150:
            raise forms.ValidationError("El título no puede superar 150 caracteres.")
        return titulo

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje', '').strip()
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje es demasiado corto (mínimo 10 caracteres).")
        if len(mensaje) > 500:
            raise forms.ValidationError("El mensaje no puede superar 500 caracteres.")
        return mensaje

# ══════════════════════════════════════════════════════════
#  FACTURA
# ══════════════════════════════════════════════════════════

class FacturaForm(forms.ModelForm):
    class Meta:
        model  = Factura
        fields = ['tipo', 'numero_factura', 'orden_servicio']
        widgets = {
            'tipo'          : forms.Select(attrs={'class': 'form-control', 'id': 'id_tipo'}),
            'numero_factura': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Se genera automáticamente'}),
            'orden_servicio': forms.Select(attrs={'class': 'form-control', 'id': 'id_orden_servicio'}),
        }

    producto = forms.ModelChoiceField(
        queryset=Producto.objects.filter(estado=True, stock__gt=0),
        required=False, empty_label="-- Seleccione un Producto --",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_producto'})
    )
    cantidad = forms.IntegerField(
        required=False, min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'id_cantidad'})
    )

    def _generar_numero(self):
        ultimo    = Factura.objects.order_by('-id').first()
        siguiente = (ultimo.id + 1) if ultimo else 1
        return f'FAC-{siguiente:04d}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_servicio'].queryset = (
            OrdenServicio.objects
            .filter(estado__in=['En Proceso', 'Terminado'])
            .select_related('vehiculo')
            .prefetch_related('servicios')
        )
        self.fields['orden_servicio'].empty_label = "-- Seleccione una Orden --"
        self.fields['orden_servicio'].required    = False
        if not self.instance.pk:
            self.fields['numero_factura'].initial = self._generar_numero()

    def clean(self):
        cleaned  = super().clean()
        tipo     = cleaned.get('tipo')
        orden    = cleaned.get('orden_servicio')
        producto = cleaned.get('producto')
        cantidad = cleaned.get('cantidad')

        if tipo == 'SERVICIO':
            if not orden:
                self.add_error('orden_servicio', "Seleccione una Orden de Servicio.")
            elif Factura.objects.filter(
                orden_servicio=orden, estado_pago='Pagada'
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                self.add_error('orden_servicio', "Esta orden ya tiene una factura pagada asociada.")
        elif tipo == 'PRODUCTO':
            if not producto:
                self.add_error('producto', "Seleccione un Producto.")
            if not cantidad or cantidad < 1:
                self.add_error('cantidad', "Ingrese una cantidad válida (mínimo 1).")
            elif producto and cantidad > producto.stock:
                self.add_error('cantidad', f"Stock insuficiente. Disponible: {producto.stock}, solicitado: {cantidad}.")

        nf = cleaned.get('numero_factura', '').strip()
        if not nf:
            nf = self._generar_numero()
            cleaned['numero_factura'] = nf

        qs = Factura.objects.filter(numero_factura=nf)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            from django.db import transaction
            with transaction.atomic():
                base = Factura.objects.select_for_update().order_by('-id').first()
                sig  = (base.id + 1) if base else 1
                while Factura.objects.filter(numero_factura=f'FAC-{sig:04d}').exists():
                    sig += 1
                cleaned['numero_factura'] = f'FAC-{sig:04d}'

        return cleaned


# ══════════════════════════════════════════════════════════
#  FACTURA — PAGAR
# ══════════════════════════════════════════════════════════

class PagarFacturaForm(forms.ModelForm):
    class Meta:
        model   = Factura
        fields  = ['metodo_pago']
        widgets = {'metodo_pago': forms.Select(attrs={'class': 'form-control'})}

    def clean_metodo_pago(self):
        metodo = self.cleaned_data.get('metodo_pago')
        if not metodo:
            raise forms.ValidationError("Seleccione un método de pago.")
        return metodo

# ══════════════════════════════════════════════════════════
#  REGISTRO DE USUARIOS DEL SISTEMA
# ══════════════════════════════════════════════════════════
from django.contrib.auth.forms import UserCreationForm
class RegistroUsuarioSistemaForm(UserCreationForm):
    class Meta:
        model  = UsuarioSistema
        fields = ['username', 'first_name', 'last_name', 'email',
                  'tipo_documento', 'cedula', 'telefono', 'cargo', 'foto']  # ← foto

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required  = True
        self.fields['email'].required      = True
        self.fields['foto'].required       = False

    def clean_first_name(self):
        return val_solo_letras(self.cleaned_data['first_name'], "Nombre")

    def clean_last_name(self):
        return val_solo_letras(self.cleaned_data['last_name'], "Apellido")

    def clean_email(self):
        email = val_email(self.cleaned_data['email'], "Email")
        if UsuarioSistema.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este email.")
        return email

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if cedula:
            cedula = val_solo_numeros(cedula, "Cédula")
            if not (8 <= len(cedula) <= 14):
                raise forms.ValidationError("La cédula debe tener entre 8 y 14 dígitos.")
            if UsuarioSistema.objects.filter(cedula=cedula).exists():
                raise forms.ValidationError("Ya existe un usuario con esta cédula.")
        return cedula

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').strip()
        if not telefono:
            raise forms.ValidationError("El teléfono es obligatorio.")
        if not telefono.isdigit():
            raise forms.ValidationError("Solo se permiten números, sin espacios ni símbolos.")
        if len(telefono) == 10:
            if not (telefono.startswith('3')):
                raise forms.ValidationError("Celular colombiano debe empezar por 3. Ej: 3101234567")
        elif len(telefono) == 7:
            pass  # fijo sin indicativo
        else:
            raise forms.ValidationError("Ingrese 10 dígitos para celular (ej: 3101234567) o 7 para fijo.")
        return telefono

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto and hasattr(foto, 'name'):
            ext = foto.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                raise forms.ValidationError("Solo se permiten imágenes JPG, PNG o WEBP.")
            if foto.size > 2 * 1024 * 1024:
                raise forms.ValidationError("La imagen no puede superar los 2 MB.")
        return foto

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.activo    = True
        user.is_active = True
        if commit:
            user.save()
        return user