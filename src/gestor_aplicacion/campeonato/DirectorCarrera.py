import random
from typing import List

from src.gestor_aplicacion.paddock.Persona import Persona


class DirectorCarrera(Persona):

    listaDirectores = []

    def __init__(self, nombre, plata, licencia, carrera=None, pais=None):
        super().__init__(nombre, pais)
        self.licencia = licencia
        self.carrera = carrera
        self.corrupcion = 0
        self.posicionesCorruptas = []
        DirectorCarrera.listaDirectores.append(self)
        self.redondear()

    @staticmethod
    def create_director_carrera(nombre):
        nuevo_director = DirectorCarrera(nombre,0,False, None, None)
        return nuevo_director


    @property
    def licencia(self):
        return self._licencia

    @licencia.setter
    def licencia(self, licencia):
        self._licencia = licencia

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    @property
    def corrupcion(self):
        return self._corrupcion

    @corrupcion.setter
    def corrupcion(self, corrupcion):
        self._corrupcion = corrupcion

    def recibir_plata(self, plata, piloto=None):
        self.plata += plata
        if piloto:
            piloto.equipo.plata -= plata

    def sin_plata(self):
        self.plata = random.uniform(10000, 50000)

    def poner_sancion(self, piloto):
        piloto.sanciones += 1

    def pilotos_desfavorecidos(self, plata, piloto, campeonato):
        carrera_director = self.carrera_campeonato(campeonato)
        pilotos_desfavorecidos = []
        for piloto1 in campeonato.lista_pilotos:
            if piloto.equipo != piloto1.equipo and piloto1.valor_contrato * 0.05 < plata and piloto1 not in carrera_director.equipos_beneficiados:
                pilotos_desfavorecidos.append(piloto1)
        return pilotos_desfavorecidos

    def carrera_campeonato(self, campeonato):
        lista_carreras_director = [carrera for carrera in campeonato.lista_carreras if carrera.director_carrera == self]
        return random.choice(lista_carreras_director)

    @staticmethod
    def dc_disponibles():
        disponibles = [dc for dc in DirectorCarrera.listaDirectores if dc.licencia]
        return disponibles

    def redondear(self):
        self.plata = round(self.plata, 2)

    @classmethod
    def setListaDirectores(cls, lista_Directores):
        cls.listaDirectores = lista_Directores

    @staticmethod
    def getListaDirectores():
        return DirectorCarrera.listaDirectores

    