"""Modulo para explicar como se documenta siguiendo el pep 257

(listar las clases, excepciones y funciones publicas)

Clases:

-Documentacion: clase para documentar.

Excepciones:

-LiadaError: Exceocion generia para cuando se producen errores durante la documentacion.
"""
__author__ = 'antonioirizar'


class Documentacion:
    """Clase para la creacion de una buena docuemntacion en Python

    (listar todos los metodos publicos y los atributos publicos)

    Metodos:

    - mi_funcion: (descripcion)

    Atributos:

    - mi_atributo: (descripcion)
    """
    def __init__(self):
        """Crea la clase Documentacion con sus atributos

        (explicacion mas detallada del constructor si hicera falta)

        (Explicar los argumentos que le entran e indicar su tipo)

        (Si pudiera lanzar algun tipo de excepcion se deberia indicar cual es y porque se lanza)
        """
        self.mi_atributo = None

    def mi_funcion(self):
        """Explicacion de mi funcion"""
        pass

    def _mi_funcion_con_argumentos(self, arg):
        """Explicacion de mi funcion con argumentos

        (explicacion mas detallada del metodo y sus efectos)

        (Explicar los argumentos que le entran e indicar su tipo)
        arg: argumento de tipo lo que sea

        (Explicar el return si tuviera e indicar su tipo)

        (Si pudiera lanzar algun tipo de excepcion se deberia indicar cual es y porque se lanza)
        """
        pass


class LiadaError(Exception):
    """excepcion generica para cuando se produczcan errores en la documentacion"""
    pass
