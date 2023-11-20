import random
# from typing import List
from decimal import Decimal, ROUND_HALF_UP

from src.gestor_aplicacion.campeonato.VehiculoCarrera import VehiculoCarrera


class Carrera:
    listaCarreras = []
    idActual = 1

    def __init__(self, ciudad, dificultad, campeonato, circuito, mes, directorCarrera):
        self.id = Carrera.idActual
        Carrera.idActual += 1
        random.seed()  # Initialize the random seed
        pool_nombres = ["Grand Prix de ", "Trofeo de "]
        self.ciudad = ciudad
        self.mes = mes
        self.dificultad = int(dificultad)
        self.campeonato = campeonato
        self.circuito = circuito
        self.director_carrera = directorCarrera
        self.nombre_circuito = pool_nombres[random.randint(0, 1)] + self.ciudad.nombre
        self.distancia = (random.randint(5, 15) * 1000)
        self.premio_efectivo = (random.randint(1, 3) * 1000)
        random_number = random.randint(1, 28)
        self.fecha = f"{random_number}/{self.mes}/2023"
        self.setPosiciones([])
        self.setEquiposBeneficiados([])
        self.setTerminados([])
        Carrera.listaCarreras.append(self)

    def redondear(self):
        self.distancia = self.distancia.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.premioEfectivo = self.premioEfectivo.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.clima = self.clima.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    def actualizarGasolina(self, piloto, carrera):
        carroElegidoCarrera = None
        for vehiculoCarrera in VehiculoCarrera.listaVehiculos:
            if vehiculoCarrera.getPiloto() == piloto:
                carroElegidoCarrera = vehiculoCarrera
        if carroElegidoCarrera.getGasolina() > 3:
            carroElegidoCarrera.setGasolina(carroElegidoCarrera.getGasolina() - 3)
        else:
            carroElegidoCarrera.chocar(carrera)

    def actualizarPosiciones(self):
        rand = random.Random()
        print(self.posiciones)
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
        return self.nombre_circuito

    def setNombreCircuito(self, nombre):
        self.nombre_circuito = nombre

    def getDistancia(self):
        return self.distancia

    def setDistancia(self, distancia):
        self.distancia = distancia

    def getPremioEfectivo(self):
        return self.premioEfectivo

    def setPremioEfectivo(self, premio):
        self.premioEfectivo = premio

    def getDirectorCarrera(self):
        return self.director_carrera

    def setDirectorCarrera(self, director):
        self.director_carrera = director
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

    def getTerminados(self):
        return self.terminados

    def setTerminados(self, terminados):
        self.terminados = terminados

    def getOpciones(self):
        return self.opciones

    def setOpciones(self, opciones):
        self.opciones = opciones




