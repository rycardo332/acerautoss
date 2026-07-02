from django.test import TestCase
from app.models import Marca


class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        """Una prueba simple para validar que CI/CD funciona"""
        self.assertEqual(1 + 1, 2)

    def test_crear_marca(self):
        """Prueba básica de base de datos en memoria"""
        Marca.objects.create(nombre='Toyota', categoria='AUTO')
        consulta = Marca.objects.filter(nombre='Toyota')
        self.assertTrue(consulta.exists())