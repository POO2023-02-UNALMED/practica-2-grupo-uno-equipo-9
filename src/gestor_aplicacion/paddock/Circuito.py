import random

from src.gestor_aplicacion.Decimales import Decimales
from src.gestor_aplicacion.ubicaciones.Continente import Continente


class Circuito(Decimales):
    circuitos = []  # Class attribute
    idActual = 0  # Class attribute
    random = random.Random()

    def __init__(self, nombre, precio=None, continente=None):
        self.id = Circuito.idActual
        Circuito.idActual += 1
        self.nombre = nombre
        self.Precio = precio if precio is not None else (random.randint(10000, 50000) / 3)
        self.continentes = continente if continente is not None else self._generate_random_continentes()
        self.disponibilidad = list(range(1, 13))
        Circuito.circuitos.append(self)

    def _generate_random_continentes(self):
        continentes = []
        while len(continentes) < 3:
            continente = random.choice(list(Continente))
            if continente not in continentes:
                continentes.append(continente)
        return continentes

    @classmethod
    def circuitos_ubicacion(cls, campeonato):
        circuitos_ubicacion = []
        for circuito in cls.circuitos:
            if set(circuito.continentes).intersection(campeonato.continente):
                circuitos_ubicacion.append(circuito)
        return circuitos_ubicacion

    @classmethod
    def circuitos_vender(cls, dir, circuitos_disponibles):
        circuitos_vender = []
        for circuito in circuitos_disponibles:
            if dir.plata >= circuito.Precio:
                circuitos_vender.append(circuito)
        return circuitos_vender

    @classmethod
    def circuitos_disponibles(cls, mes, circuitos):
        circuitos_disponibles = []
        for circuito in circuitos:
            if circuito.ver_disponibilidad(mes):
                circuitos_disponibles.append(circuito)
        return circuitos_disponibles

    def vender_circuito(self, dir, mes):
        dir.plata -= self.Precio
        self.disponibilidad.remove(mes)

    def redondear(self):
        self.Precio = self.dos_decimales(self.Precio)

    def ver_disponibilidad(self, dia):
        return dia in self.disponibilidad

    # Getter and setter methods
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.Precio

    def set_precio(self, precio):
        self.Precio = precio

    def get_disponibilidad(self):
        return self.disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    @staticmethod
    def get_circuitos():
        return Circuito.circuitos

    @staticmethod
    def set_circuitos(circuitos):
        Circuito.circuitos = circuitos

    def get_continentes(self):
        return self.continentes

    def set_continentes(self, continentes):
        self.continentes = continentes

    @staticmethod
    def get_id_actual():
        return Circuito.idActual

    @staticmethod
    def set_id_actual(id_actual):
        Circuito.idActual = id_actual

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
