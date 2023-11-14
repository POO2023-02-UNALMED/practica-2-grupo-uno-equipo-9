from abc import ABC, abstractmethod

from src.gestor_aplicacion.Decimales import Decimales


class Persona(Decimales, ABC):
    """
    Autores: David Toro Arboleda, Santiago Lopez Ayala, Juan Andres Jimenez Velez, Mariana Valencia Cubillos, Samuel Mira Alvarez
    Descripcion de la clase: Esta clase ha sido diseñada con la finalidad de ser heredada por diferentes entidades utilizadas en el programa, como son los patrocinadores, pilotos y directores de carrera.
    """

    idActual = 1  # Class attribute

    def __init__(self, nombre, pais="Alemania", plata=0.0):
        self.id = Persona.get_id_actual()
        self.nombre = nombre
        self.pais = pais
        Persona.idActual += 1
        self.plata = plata

    @abstractmethod
    def recibir_plata(self, plata):
        pass

    @abstractmethod
    def sin_plata(self):
        pass

    def redondear(self):
        self.plata = self.dos_decimales(self.plata)

    @classmethod
    def get_id_actual(cls):
        return cls.idActual

    # Getter and setter methods
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    @classmethod
    def set_id_actual(cls, id_actual):
        cls.idActual = id_actual

    def get_plata(self):
        return self.plata

    def set_plata(self, plata):
        self.plata = plata
