import random

from src.gestor_aplicacion.Decimales import Decimales
from src.gestor_aplicacion.campeonato.Campeonato import Campeonato
from src.gestor_aplicacion.campeonato.Equipo import Equipo
from src.gestor_aplicacion.campeonato.VehiculoCarrera import VehiculoCarrera
from src.gestor_aplicacion.paddock.Persona import Persona


class Piloto(Persona, Decimales):
    listaPilotos = []
    random = random.Random()

    def __init__(self, nombre, contrato, puntos, sanciones, habilidad, lesionado, desbloqueado, elegido, valorContrato, presupuestoVehiculo, patrocinador):
        super().__init__(nombre)
        self.contrato = contrato
        self.puntos = puntos
        self.sanciones = sanciones
        self.habilidad = habilidad
        self.lesionado = lesionado
        self.desbloqueado = desbloqueado
        self.elegido = elegido
        self.valorContrato = valorContrato
        self.presupuestoVehiculo = presupuestoVehiculo
        self.patrocinador = patrocinador
        self.victorias = []
        self.tiemposCarreras = []
        self.redondear()

    @classmethod
    def create_random_piloto(cls, nombre):
        habilidad = 0.1 + (0.3 - 0.1) * random.random()
        valorContrato = random.randint(1000, 5000)
        piloto = cls(nombre, None, 0, 0, habilidad, False, False, False, valorContrato, 0, None)
        cls.listaPilotos.append(piloto)
        return piloto


    @classmethod
    def piloto_aleatorio(cls):
        n = cls.random.randint(0, len(cls.listaPilotos) - 1)
        return cls.listaPilotos[n]

    @classmethod
    def pilotos_desbloqueados(cls):
        pilotos_desbloqueados = []
        for campeonato in Campeonato.campeonatosDesbloqueados():
            for piloto in campeonato.getListaPilotos():
                if piloto.elegido:
                    pilotos_desbloqueados.append(piloto)
        return pilotos_desbloqueados

    @classmethod
    def pilotos_disponibles(cls):
        pilotos_disponibles = [piloto for piloto in cls.listaPilotos if not piloto.lesionado]
        return pilotos_disponibles

    @classmethod
    def pilotos_equipo(cls, equipo, pilotos):
        pilotos_equipo = [piloto for piloto in pilotos if piloto.contrato == equipo]
        return pilotos_equipo

    @classmethod
    def desbloquear_pilotos(cls, pilotos):
        for piloto in pilotos:
            piloto.desbloqueado = True

    @classmethod
    def asignar_equipo(cls):
        pilotos = cls.listaPilotos
        cls.random.shuffle(pilotos)
        i = 0
        c = 0
        for piloto in pilotos:
            if piloto.contrato is None:
                piloto.contrato = Equipo.equipos[i % len(Equipo.equipos)]
                c += 1
                if c % 5 == 0:
                    i += 1

    def contratar(self):
        equipo = self.contrato
        equipo.plata -= self.valorContrato
        self.presupuestoVehiculo = self.valorContrato * self.habilidad * 10

    def buscar_piloto(self, piloto):
        for piloto1 in Piloto.listaPilotos:
            if piloto1 == piloto:
                return piloto1
        return piloto

    def maldecir_piloto(self, plata, piloto, director_carrera, campeonato):
        vehiculos_devolver = [VehiculoCarrera.vehiculos_piloto(piloto)[0]]
        vehiculo_maldito = None

        for vehiculo_carrera in VehiculoCarrera.listaVehiculosCarrera:
            if vehiculo_carrera.piloto == self:
                vehiculo_maldito = vehiculo_carrera
            if campeonato.listaPilotos.__contains__(vehiculo_carrera.piloto) and vehiculo_carrera.piloto != piloto:
                vehiculos_devolver.append(vehiculo_carrera)

        if plata >= (self.valorContrato * 3 / 4):
            self.habilidad = max(self.habilidad - 0.1, 0.0)
        elif plata >= (self.valorContrato / 3):
            self.habilidad /= 2
        else:
            director_carrera.poner_sancion(piloto)

        return vehiculos_devolver

    def recibir_plata(self, plata):
        self.contrato.plata += plata

    def sin_plata(self):
        self.contrato.plata += Piloto.random.randint(2,5) * 10000

    def no_es_elegido(self):
        self.elegido = False
        if not VehiculoCarrera.vehiculos_piloto(self):
            VehiculoCarrera.crear_vehiculo_pilotos_no_elegidos(self)

    def redondear(self):
        self.habilidad = self.dos_decimales(self.habilidad)
        self.valorContrato = self.dos_decimales(self.valorContrato)
        self.presupuestoVehiculo = self.dos_decimales(self.presupuestoVehiculo)

    def sumar_puntos(self, puntos):
        self.puntos += puntos

    def agregar_victoria(self, campeonato):
        self.victorias.append(str(campeonato))

    def registrar_tiempo(self, tiempo):
        self.tiemposCarreras.append(tiempo)

    def set_elegido(self,bool):
        self.elegido=bool

    def set_desbloqueado(self,bool):
        self.desbloqueado=bool

    @staticmethod
    def setPilotos(lista_pilotos):
        Piloto.listaPilotos = lista_pilotos

    @staticmethod
    def getPilotos():
        return Piloto.listaPilotos

    def getValorContrato(self):
        return self.valorContrato

    def getPresupuestoVehiculo(self):
        return self.presupuestoVehiculo

    def getEquipo(self):
        return self.contrato

    def setPatrocinador(self,patrocinador):
        self.patrocinador = patrocinador



