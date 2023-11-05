import random
from typing import List
from decimal import Decimal, ROUND_HALF_UP

from src.gestor_aplicacion.campeonato import VehiculoCarrera


class Carrera:
    listaCarreras = []
    idActual = 1

    def __init__(self, nombre, mes, distancia, premio, ciudad, director, dificultad):
        self.id = Carrera.idActual
        Carrera.idActual += 1
        self.nombreCircuito = nombre
        self.mes = mes
        self.distancia = distancia
        self.premioEfectivo = premio
        self.ciudad = ciudad
        self.directorCarrera = director
        director.setCarrera(self)
        self.dificultad = int(dificultad)
        self.clima = Decimal(random.uniform(0.0, 0.2)).quantize(Decimal('0.00'))

        self.posiciones = []
        self.terminados = []
        self.equiposBeneficiados = []
        self.campeonato = None
        self.circuito = None

    def redondear(self):
        self.distancia = self.distancia.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.premioEfectivo = self.premioEfectivo.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.clima = self.clima.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    def actualizarGasolina(self, piloto, carrera):
        carroElegidoCarrera = None
        for vehiculoCarrera in VehiculoCarrera.listaVehiculosCarrera:
            if vehiculoCarrera.getPiloto() == piloto:
                carroElegidoCarrera = vehiculoCarrera
        if carroElegidoCarrera.getGasolina() > 3:
            carroElegidoCarrera.setGasolina(carroElegidoCarrera.getGasolina() - 3)
        else:
            carroElegidoCarrera.chocar(carrera)

    def actualizarPosiciones(self):
        rand = random.Random()
        if self.posiciones:
            for vehiculo in self.posiciones:
                vehiculo.setDistanciaRecorrida(vehiculo.getDistanciaRecorrida() + vehiculo.getVelocidadActual())
                if vehiculo.getDistanciaRecorrida() > self.distancia and vehiculo not in self.terminados:
                    self.terminados.append(vehiculo)
                    vehiculo.setTerminado(True)
                elif vehiculo not in self.terminados:
                    vehiculo.setTiempo(vehiculo.getTiempo() + 1.0)
                    if rand.random() > 0.95:
                        pass
            self.posiciones.sort(key=lambda x: x.getDistanciaRecorrida(), reverse=True)

    def actualizarOpciones(self):
        listaOpciones = []
        rand = random.Random()
        for i in range(5):
            numRandom = rand.randint(0, 9)
            if numRandom >= 2:
                listaOpciones.append(True)
            else:
                listaOpciones.append(False)
        return listaOpciones

    def actualizarTerminado(self):
        return all(vehiculo in self.terminados for vehiculo in self.posiciones)

    def organizarVehiculosTiempos(self):
        self.terminados.sort(key=lambda x: x.getTiempo())
        vehiculosTerminados = [vehiculo for vehiculo in self.terminados if vehiculo.getTiempo() == 0]
        vehiculosTerminados.extend([vehiculo for vehiculo in self.terminados if vehiculo.getTiempo() != 0])
        self.terminados = vehiculosTerminados

        vehiculosTerminados2 = []
        for vehiculo in self.terminados:
            if vehiculo not in vehiculosTerminados2:
                vehiculosTerminados2.append(vehiculo)

    def agregarVehiculoCarrera(self, vehiculoCarrera):
        self.posiciones.append(vehiculoCarrera)

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getMes(self):
        return self.mes

    def setMes(self, mes):
        self.mes = mes

    def getNombreCircuito(self):
        return self.nombreCircuito

    def setNombreCircuito(self, nombre):
        self.nombreCircuito = nombre

    def getDistancia(self):
        return self.distancia

    def setDistancia(self, distancia):
        self.distancia = distancia

    def getPremioEfectivo(self):
        return self.premioEfectivo

    def setPremioEfectivo(self, premio):
        self.premioEfectivo = premio

    def getDirectorCarrera(self):
        return self.directorCarrera

    def setDirectorCarrera(self, director):
        self.directorCarrera = director
        director.setCarrera(self)

    def getCiudad(self):
        return self.ciudad

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def getClima(self):
        return self.clima

    def setClima(self, clima):
        self.clima = clima

    def getDificultad(self):
        return self.dificultad

    def setDificultad(self, dificultad):
        self.dificultad = dificultad

    def getPosiciones(self):
        return self.posiciones

    def setPosiciones(self, posiciones):
        self.posiciones = posiciones

    def getCircuito(self):
        return self.circuito

    def setCircuito(self, circuito):
        self.circuito = circuito

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getCampeonato(self):
        return self.campeonato

    def setCampeonato(self, campeonato):
        self.campeonato = campeonato

    def getEquiposBeneficiados(self):
        return self.equiposBeneficiados

    def setEquiposBeneficiados(self, equiposBeneficiados):
        self.equiposBeneficiados = equiposBeneficiados


