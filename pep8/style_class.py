"""Estilo para las clases"""
# los future siempre despues del docstring
from __future__ import unicode_literals

# Despues de los future van el autor version etc
__author__ = 'antonioirizar'
__version__ = '0.0.1'

# Luego los import siempre tiene que estar agrupados d ela siguiente manera y separado por una linea
# Libreria estandar
# libererias de terceros
# tus import de la aplicacion local
from datetime import datetime
# Mal
import os, sys
# bien
import os
import sys
# despues de los import dos lineas


# Estilo Nombre de clases CamelCase

# MAL
class coche:
    def __init__(self):
        pass


# BIEN
class Coche:
    def __init__(self):
        pass


# siempre dos espacios entre clases

# Clase con nombre compuesto mal escrito
class Coche_rojo:
    def __init__(self):
        pass


# Clase con nombre compuesto bien escrito
class CocheRojo:
    def __init__(self):
        pass


# Estilo nombre metdos de clase y atributos de clase

class Casa:
    def __init__(self, color):
        self.color = color  # público lower_case_with_underscores
        self._fecha_creacion = datetime.now()  # privado con barra baja delante

    # público lower_case_with_underscores
    def color_en_mayusculas(self):
        return self.color.upper()

    # privado lower_case_with_underscores
    def _actualizar_fecha(self):
        self._fecha_creacion = datetime.now()

    # siempre se usa self para los metodos dento de una clase

    # Mal
    def mal_self(this):
        pass

    # siempre se usa cls para metodos de clase

    # Mal
    @classmethod
    def mal_cls(clase):
        pass

    # bien
    @classmethod
    def bin_cls(cls):
        pass


# las Excepciones que creemos que sean para errores deberan tener como sufijo Error
class MiExcepcionError(Exception):
    pass

# linea en blanco al final de los módulos
