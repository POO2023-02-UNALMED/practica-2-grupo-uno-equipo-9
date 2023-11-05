import random
from enum import Enum

from src.gestor_aplicacion.paddock.Patrocinador import Patrocinador


class Ciudad:
    listaCiudades = []

    class Continente(Enum):
        Africa = 1
        America = 2
        Asia = 3
        Europa = 4
        Oceania = 5

    def __init__(self, nombre, continente):
        self.nombre = nombre
        self.continente = continente
        Ciudad.listaCiudades.append(self)
        self.host = random.choice(Patrocinador.listaPatrocinadores)
        self.precioEstadia = random.uniform(100, 600)

    def __str__(self):
        return self.nombre

    @staticmethod
    def get_lista_ciudades():
        return Ciudad.listaCiudades

    @staticmethod
    def convertir_continente(id):
        if id == 1:
            return Ciudad.Continente.Africa
        elif id == 2:
            return Ciudad.Continente.America
        elif id == 3:
            return Ciudad.Continente.Asia
        elif id == 4:
            return Ciudad.Continente.Europa
        elif id == 5:
            return Ciudad.Continente.Oceania

    @staticmethod
    def ciudades_continente(continente):
        lista_completa = Ciudad.get_lista_ciudades()
        lista_disponibles = [ciudad for ciudad in lista_completa if ciudad.continente == continente]
        return lista_disponibles

    def estadia(self, carrera):
        campeonato = carrera.campeonato
        for equipo in campeonato.lista_equipos:
            precio = self.precioEstadia * equipo.crew_members
            self.host.dinero -= precio

    def host_rosca(self, carrera):
        campeonato = carrera.campeonato
        equipos = campeonato.lista_equipos
        equipos_beneficiados = [equipo for equipo in equipos if self.host in equipo.patrocinadores_equipo]
        carrera.equipos_beneficiados = equipos_beneficiados

    def redondear(self):
        self.precioEstadia = round(self.precioEstadia, 2)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def continente(self):
        return self._continente

    @continente.setter
    def continente(self, continente):
        self._continente = continente

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def precioEstadia(self):
        return self._precioEstadia

    @precioEstadia.setter
    def precioEstadia(self, precioEstadia):
        self._precioEstadia = precioEstadia

    @classmethod
    def set_lista_ciudades(cls, lista_ciudades):
        cls.listaCiudades = lista_ciudades

