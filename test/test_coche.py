__author__ = 'antonioirizar'

from datetime import date
from unittest import TestCase
from unittest.mock import MagicMock, patch

from coche import Coche


class TestCoche(TestCase):
    def test_creacion_coche(self):
        mi_coche = Coche('rojo')
        self.assertEqual(mi_coche.color, 'rojo')

    def test_deportivo(self):
        mi_coche = Coche('rojo')
        mi_coche._validar_color = MagicMock(return_value=True)
        self.assertTrue(mi_coche.coche_es_deportivo())

    def test_deportivo_excepcion(self):
        mi_coche = Coche('rojo')
        mi_coche._validar_color = MagicMock(side_effect=Exception)
        with self.assertRaises(KeyError):
            mi_coche.coche_es_deportivo()

    @patch('coche.Coche._validar_color', side_effect=Exception)
    def test_deportivo_excepcion2(self, _):
        mi_coche = Coche('rojo')
        # mi_coche._validar_color = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            mi_coche.coche_es_deportivo()

    @patch('coche.datetime')
    def test_coche_mala_calidad_y_devuelve_true(self, mock_datetime):
         mock_datetime.now.return_value = date(2015, 1, 1)
         mi_coche = Coche('rojo')
         mi_coche.fecha_creacion = date(2014, 12, 5)
         mi_coche.numero_reparaciones = 10
         self.assertTrue(mi_coche.coche_es_de_mala_calidad())
