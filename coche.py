__author__ = 'antonioirizar'
from datetime import datetime


class Coche:
    def __init__(self, color):
        self.color = color
        self.fecha_creacion = datetime.now()
        self.numero_reparaciones = 0

    def coche_es_de_mala_calidad(self):
        coche_malo = False
        if self.numero_reparaciones > self.fecha_creacion.year - datetime.now().year:
            coche_malo = True
        return coche_malo

    def coche_es_deportivo(self):
        deportivo = True
        if self._validar_color() and self.color != 'rojo':
            deportivo = False
        return deportivo

    def _validar_color(self):
        if isinstance(self.color, str):
            return True
        else:
            raise Exception("El color tiene que ser un String")


