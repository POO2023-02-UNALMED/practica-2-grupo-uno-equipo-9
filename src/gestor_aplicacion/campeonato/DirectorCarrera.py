import random
from typing import List

from src.gestor_aplicacion.campeonato.Carrera import Carrera
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
        plata = random.uniform(10000, 50000)
        nuevo_director = DirectorCarrera(nombre, plata, True, None, None)
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
        for piloto1 in campeonato._listaPilotos:
            if piloto.contrato != piloto1.contrato and piloto1.valorContrato * 0.05 < plata and piloto1.contrato not in carrera_director.equiposBeneficiados:
                pilotos_desfavorecidos.append(piloto1)
        if pilotos_desfavorecidos:
            return pilotos_desfavorecidos
        else:
            return random.sample(campeonato._listaPilotos,5)

    def carrera_campeonato(self, campeonato):
        lista_carreras_director = [carrera for carrera in campeonato._listaCarreras if carrera.director_carrera == self]
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

    