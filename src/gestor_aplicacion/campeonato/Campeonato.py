from random import randint
from enum import Enum
from decimal import Decimal, getcontext
from collections import defaultdict
from src.gestor_aplicacion.ubicaciones.Continente import Continente

class Campeonato:
    campeonatos = []
    idActual = 1
    ano = 2023
    minCarreras = 2

    def __init__(self, listaCarreras, listaEquipos, listaPilotos, id, nombre, continente, cantCarreras, premio, desbloqueado, patrocinadorCampeonato=None):
        self._listaCarreras = listaCarreras
        self._listaEquipos = listaEquipos
        self._listaPilotos = listaPilotos
        if not(id):
            self._id = id
        else:
            self._id = Campeonato.idActual()
            Campeonato.idActual+=1
        self._nombre = nombre
        self._continente = continente
        self._cantCarreras = cantCarreras
        self._premio = premio
        self._desbloqueado = desbloqueado
        self._jugado = False
        self._patrocinadorCampeonato = patrocinadorCampeonato
        if patrocinadorCampeonato:
            patrocinadorCampeonato.setPatrocinadorCampeonato()
        Campeonato.campeonatos.append(self)
        self._mesesCarreras = list(range(1, 13))

        self.redondear()

    @staticmethod
    def create_campeonato_base(nombre,cantCarreras,continente):
        premio = randint(70, 100) * 10000
        campeonato_base = Campeonato(None,None,None,None,nombre,continente,cantCarreras,premio,False,None)
        return campeonato_base

    @classmethod
    def idActual(cls):
        return cls.idActual

    @staticmethod
    def campeonatosContinente(continente):
        campeonatosContinente = []
        for campeonato in Campeonato.campeonatos:
            if campeonato.getContinente() == continente.value:
                campeonatosContinente.append(campeonato)
        return campeonatosContinente

    @staticmethod
    def buscarCampeonato(id):
        for campeonato in Campeonato.campeonatos:
            if campeonato.getId() == id:
                return campeonato
        return None

    @staticmethod
    def campeonatosDisponibles():
        campeonatosDisponibles = []
        for campeonato in Campeonato.campeonatos:
            if not campeonato.isDesbloqueado() and not campeonato.isJugado():
                campeonatosDisponibles.append(campeonato)
        return campeonatosDisponibles

    @staticmethod
    def campeonatosDesbloqueados():
        campeonatosDesbloqueados = []
        for campeonato in Campeonato.campeonatos:
            if campeonato.isDesbloqueado() and not campeonato.isJugado():
                campeonatosDesbloqueados.append(campeonato)
        return campeonatosDesbloqueados

    @staticmethod
    def campeonatoPiloto(piloto):
        for campeonato in Campeonato.campeonatosDesbloqueados():
            for pilotico in campeonato.getListaPilotos():
                if pilotico.isElegido() and pilotico == piloto:
                    return campeonato
        return None

    @staticmethod
    def directoresCarrera(campeonatoElegido):
        maestrosDeCarrera = [carrera.getDirectorCarrera() for carrera in campeonatoElegido.getListaCarreras()]
        maestrosDeCarreraDiferentes = list(set(maestrosDeCarrera))
        return maestrosDeCarreraDiferentes

    def actualizarEquipos(self):
        for piloto in self.getListaPilotos():
            if piloto.getEquipo() not in self.getListaEquipos():
                self.getListaEquipos().append(piloto.getEquipo())

    @classmethod
    def getIdActual(cls):
        return cls.idActual

    @classmethod
    def setIdActual(cls, idActual):
        cls.idActual = idActual

    @classmethod
    def getCampeonatos(cls):
        return cls.campeonatos

    @classmethod
    def setCampeonatos(cls, campeonatos):
        cls.campeonatos = campeonatos

    def premiarCampeones(self, equiposPuntuados):
        self.setListaEquipos(equiposPuntuados)
        multiplicadorDinero = 1.2
        contadorHabilidad = 0.08
        for equipo in equiposPuntuados:
            equipo.setPlata(equipo.getPlata() + self._premio * multiplicadorDinero)
            if equipo.getPatrocinadoresEquipo():
                for patrocinador in equipo.getPatrocinadoresEquipo():
                    patrocinador.recibirPlata(self._premio * multiplicadorDinero / 2)
            if multiplicadorDinero > 0.2:
                multiplicadorDinero -= 0.2
            for piloto in self.getListaPilotos():
                if piloto.getEquipo() == equipo and piloto.getPuntos() != 0 and equiposPuntuados[0] == equipo:
                    piloto.setHabilidad(contadorHabilidad)
                    piloto.agregarVictoria(self)
                elif piloto.getEquipo() == equipo and piloto.getPuntos() != 0:
                    piloto.setHabilidad(contadorHabilidad)
                if contadorHabilidad > 0.02:
                    contadorHabilidad -= 0.01

    def __str__(self):
        return f"{self._nombre} {Campeonato.ano} ({self._continente.name})"

    def agregarCarrera(self, carrerita):
        if self.getNumCarreras() < self._cantCarreras:
            self._listaCarreras.append(carrerita)

    def carrerasPreferidas(self):
        carrerasPreferidas = []
        for carrera in self._listaCarreras:
            if self._patrocinadorCampeonato and carrera.getCiudad() in self._patrocinadorCampeonato.getCiudadesPreferidas():
                carrerasPreferidas.append(carrera)
        return carrerasPreferidas

    def organizarCarreras(self):
        self._listaCarreras.sort(key=lambda carrera: (carrera.getFecha(), carrera.getMes()))

    def actualizarMesCarreras(self, mes):
        self._mesesCarreras.remove(mes)

    def logisticaPremios(self, premio, presupuesto, carrerasPreferidas):
        patrocinador = self._patrocinadorCampeonato
        if patrocinador:
            if patrocinador.getPlata() / 2 > premio:
                self._premio = patrocinador.getPlata() / 2
                patrocinador.setPlata(patrocinador.getPlata() - self._premio)
            else:
                self._premio = premio
                patrocinador.setPlata(patrocinador.getPlata() - self._premio)

        pesoTotal = 0
        for carrera in self._listaCarreras:
            pesoTotal += carrera.getDificultad()
            if carrera in carrerasPreferidas:
                pesoTotal += carrera.getDificultad()

        for carrera in self._listaCarreras:
            premioEfectivo = carrera.getDificultad() / pesoTotal * presupuesto
            if carrera in carrerasPreferidas:
                premioEfectivo *= 2
            carrera.setPremioEfectivo(premioEfectivo)

        if patrocinador:
            patrocinador.setPlata(patrocinador.getPlata() - presupuesto)

        self.organizarCarreras()

    def pilotoCampeonato(self):
        for piloto in self.getListaPilotos():
            if piloto.isElegido():
                return piloto
        return None

    def redondear(self):
        getcontext().prec = 2
        self._premio = Decimal(self._premio)

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getAno(self):
        return Campeonato.ano

    def setAno(self, ano):
        Campeonato.ano = ano

    def getContinente(self):
        return self._continente

    def setContinente(self, continente):
        self._continente = continente

    def getCantidadMaxCarreras(self):
        return self._cantCarreras

    def setCantidadMaxCarreras(self, cantidadCarreras):
        self._cantCarreras = cantidadCarreras

    def getNumCarreras(self):
        return len(self._listaCarreras)

    def getPremio(self):
        return self._premio

    def setPremio(self, premio):
        self._premio = premio

    def getListaCarreras(self):
        return self._listaCarreras

    def setListaCarreras(self, listaCarreras):
        self._listaCarreras = listaCarreras

    def isDesbloqueado(self):
        return self._desbloqueado

    def setDesbloqueado(self, desbloqueado):
        self._desbloqueado = desbloqueado

    def getListaEquipos(self):
        return self._listaEquipos

    def setListaEquipos(self, listaEquipos):
        self._listaEquipos = listaEquipos

    def getListaPilotos(self):
        return self._listaPilotos

    def setListaPilotos(self, listaPilotos):
        listaPilotosElegidos = []
        for piloto in listaPilotos:
            if piloto not in listaPilotosElegidos:
                listaPilotosElegidos.append(piloto)
        self._listaPilotos = listaPilotos

    def getCantCarreras(self):
        return self._cantCarreras

    def setCantCarreras(self, cantCarreras):
        self._cantCarreras = cantCarreras

    def getPatrocinadorCampeonato(self):
        return self._patrocinadorCampeonato

    def setPatrocinadorCampeonato(self, patrocinadorCampeonato):
        self._patrocinadorCampeonato = patrocinadorCampeonato

    def getMesesCarreras(self):
        return self._mesesCarreras

    def setMesesCarreras(self, mesesCarreras):
        self._mesesCarreras = mesesCarreras

    def isJugado(self):
        return self._jugado

    def setJugado(self, jugado):
        self._jugado = jugado

    def equals(self, other):
        return self is other or (isinstance(other, Campeonato) and self._id == other._id)

    def __hash__(self):
        return hash(self._id)

