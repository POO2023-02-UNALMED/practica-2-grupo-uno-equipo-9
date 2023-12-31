import random
from typing import List
from enum import Enum
from typing import List
import math
from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad

class Equipo:
    equipos = []  # Class attribute
    idActual = 0  # Class attribute

    def __init__(self, nombre="", plata=0, puntos=0, pilotos_disponibles=None):
        self.id = Equipo.idActual
        Equipo.idActual += 1
        self.nombre = nombre
        self.plata = plata
        self.puntos = puntos
        self.ocupado = False
        self.sedes = []
        self.patrocinadores_equipo = []
        self.elegido = False
        self.crew_members = 5
        self.cant_contratos = 0

        if pilotos_disponibles:
            for piloto in pilotos_disponibles:
                piloto.equipo = self

        Equipo.equipos.append(self)

    @staticmethod
    def create_equipo(nombre):
        plata = random.randint(30 , 60) * 20000
        nuevo_equipo = Equipo(nombre,plata,0,None)
        return nuevo_equipo

    @classmethod
    def puntuarEquipos(cls, terminados, plata, campeonato):
        puntos_actuales = 13
        for vehiculo in terminados:
            piloto = vehiculo.piloto.buscar_piloto(vehiculo.piloto)

            if not vehiculo.morido:
                piloto.puntos += puntos_actuales
                piloto.contrato.recalcular_puntos(campeonato)

                if puntos_actuales >= 8:
                    puntos_actuales -= 2
                else:
                    puntos_actuales -= 1

            if piloto.sanciones == 0:
                piloto.puntos += puntos_actuales

            piloto.registrar_tiempo(vehiculo.tiempo)

        for equipo in campeonato._listaEquipos:
            equipo.recalcular_puntos(campeonato)

        terminados[0].piloto.recibir_plata(plata * 0.9)

        for patrocinador in terminados[0].piloto.contrato.patrocinadores_equipo:
            patrocinador.recibir_plata(plata * 0.5)

        terminados[1].piloto.recibir_plata(plata * 0.3)
        terminados[2].piloto.recibir_plata(plata * 0.2)

        Equipo.organizar_equipos_puntos(campeonato)

    @classmethod
    def organizar_equipos_puntos(cls, campeonato):
        lista_organizada = campeonato._listaEquipos[:]
        for equipo in lista_organizada:
            equipo.puntos = abs(equipo.puntos)

        lista_organizada.sort(key=lambda equipo: equipo.puntos, reverse=True)
        campeonato._listaEquipos = lista_organizada
        return lista_organizada

    @classmethod
    def sedes_equipos(cls):
        for equipo in cls.equipos:
            for ciudad in Ciudad.listaCiudades:
                if (random.choice([True,False])):
                    equipo.sedes.append(ciudad)

    @classmethod
    def equipos_continente(cls,continente):
        equipos_in_continente = []
        for equipo in cls.equipos:
            for sede in equipo.sedes:
                if sede.continente == continente:
                    equipos_in_continente.append(equipo)
                    break
        return equipos_in_continente


    @classmethod
    def equipos_disponibles(cls, equipos):
        equipos_disponibles = [equipo for equipo in equipos if not equipo.ocupado]
        return equipos_disponibles

    @classmethod
    def elegir_contrincantes(cls,equipo_elegido,campeonato,equipos):
        equipos_participantes = []
        equipos_participantes.append(equipo_elegido)
        equipos.remove(equipo_elegido)
        for i in range(0,4,1):
            equip_random = random.choice(equipos)
            equipos_participantes.append(equip_random)
            equipos.remove(equip_random)
        campeonato.setListaEquipos(equipos_participantes)
        return equipos_participantes

    def recalcular_puntos(self, campeonato):
        nuevos_puntos = 0
        for piloto in campeonato._listaPilotos:
            if piloto.contrato == self:
                nuevos_puntos += piloto.puntos

        self.puntos = nuevos_puntos

    def recibir_plata(self, plata):
        self.plata += plata

    def descuento(self, precio_total, vehiculo_carrera):
        piloto = vehiculo_carrera.piloto
        return piloto.habilidad > (precio_total / self.plata)

    def calcular_descuento(self, precio_total, vehiculo_carrera):
        piloto = vehiculo_carrera.piloto
        descuento = 0
        porcentaje = 0
        if piloto.habilidad > (precio_total / self.plata):
            descuento = precio_total * (piloto.habilidad - (precio_total / self.plata))
            porcentaje = descuento / precio_total
        return porcentaje * 100

    def comprar_piezas(self, precio_total, vehiculo_carrera):
        descuento = self.calcular_descuento(precio_total, vehiculo_carrera)
        precio_final = precio_total - descuento * precio_total
        self.plata -= precio_final
        vehiculo_carrera.configurarVehiculo(vehiculo_carrera.piezasComprar)

    def agregar_patrocinador(self, patrocinador):
        self.patrocinadores_equipo.append(patrocinador)

    def agregar_sede(self, ciudad):
        self.sedes.append(ciudad)

    # Getter and setter methods
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_plata(self):
        return self.plata

    def set_plata(self, plata):
        self.plata = round(plata, 2)
        if self.plata < 0:
            for patrocinador in self.patrocinadores_equipo:
                patrocinador.plata += abs(self.plata) * 2
            self.plata = abs(self.plata)

    def get_puntos(self):
        return self.puntos

    def set_puntos(self, puntos):
        self.puntos = puntos

    def get_patrocinadores_equipo(self):
        return self.patrocinadores_equipo

    def set_patrocinadores_equipo(self, patrocinadores_equipo):
        self.patrocinadores_equipo = patrocinadores_equipo

    def get_sedes(self):
        return self.sedes

    def set_sedes(self, sedes):
        self.sedes = sedes

    def is_ocupado(self):
        return self.ocupado

    def set_ocupado(self, ocupado):
        self.ocupado = ocupado

    def is_elegido(self):
        return self.elegido

    def set_elegido(self, elegido):
        self.elegido = elegido

    def get_cant_contratos(self):
        return self.cant_contratos

    def set_cant_contratos(self, cant_contratos):
        self.cant_contratos = cant_contratos

    def get_crew_members(self):
        return self.crew_members

    def set_crew_members(self, crew_members):
        self.crew_members = crew_members

    @staticmethod
    def setEquipos(lista_equipos):
        Equipo.equipos = lista_equipos

    @staticmethod
    def getEquipos():
        return Equipo.equipos

    def agregarPatrocinador(self,patrocinador):
        self.patrocinadores_equipo.append(patrocinador)