import random

from src.gestor_aplicacion.Decimales import Decimales
from src.gestor_aplicacion.paddock.Chasis import Chasis


class VehiculoCarrera(Chasis, Decimales):
    listaVehiculos = []

    def __init__(self, marca, modelo, velocidad, maniobrabilidad, precio, piloto, motor, neumaticos, aleron):
        super().__init__(marca, modelo, velocidad, maniobrabilidad, precio)
        self.piloto = piloto
        self.idActual = 1
        self.id = self.idActual
        self.idActual += 1
        self.tiempo = 0
        self.distanciaRecorrida = 0
        self.terminado = False
        self.morido = False
        self.velocidadTuneao = 0
        self.velocidadCircumstancias = 0
        self.velocidadActual = 0
        self.probabilidadChoque = 0
        self.motor = motor
        self.neumaticos = neumaticos
        self.aleron = aleron
        self.gasolina = 100
        self.piezasComprar = []
        self.redondear()

    def redondear(self):
        pass  # Implement this method if needed

    def chocar(self, carrera):
        self.tiempo = 0
        self.velocidadActual = 0
        self.terminado = True
        carrera.terminados.append(self)
        self.morido = True
        self.piloto.sanciones += 1

    def cambiarPieza(self, pieza):
        tipoPieza = pieza.tipo
        if tipoPieza == "A":
            self.aleron = pieza
            self.actualizarVelocidadT()
        elif tipoPieza == "N":
            self.neumaticos = pieza
            self.actualizarVelocidadT()
        elif tipoPieza == "M":
            self.motor = pieza
            self.actualizarVelocidadT()

    def configurarVehiculo(self, piezas):
        for pieza in piezas:
            self.cambiarPieza(pieza)
            pieza.elegida = True
        self.llenarGasolina()

    def repararVehiculo(self):
        precio = (self.motor.precio + self.aleron.precio + self.neumaticos.precio) / 2
        equipo = self.piloto.equipo
        if equipo.plata >= precio:
            equipo.plata -= precio
            self.aleron.arreglar()
            self.motor.arreglar()
            self.neumaticos.arreglar()
            return True
        return False

    def llenarGasolina(self):
        self.gasolina = 100

    def defender(self, carrera):
        randomNumber = random.randint(1, 10)
        if randomNumber <= 5:
            self.velocidadCircumstancias = 20
            self.actualizarVelocidadActual()
        else:
            self.velocidadCircumstancias = -20
            self.actualizarVelocidadActual()

    def derrapar(self, carrera):
        randomNumber = random.randint(1, 10)
        if randomNumber == 1:
            self.neumaticos.danado = True
            self.actualizarVelicidadActual()
        elif randomNumber <= 9:
            self.velocidadCircumstancias = 30
            self.actualizarVelocidadActual()
        else:
            numeroAleatorio = random.random()
            if numeroAleatorio <= self.probabilidadChoque:
                self.chocar(carrera)
            else:
                self.velocidadCircumstancias = 30
                self.actualizarVelocidadActual()

    def manejarNormal(self, carrera):
        self.velocidadCircumstancias = 0
        self.actualizarVelocidadActual()
        numeroAleatorio = random.random()
        if numeroAleatorio <= self.probabilidadChoque:
            self.chocar(carrera)

    def sumarGasolina(self):
        if self.gasolina < 100:
            self.gasolina += 10

    def actualizarVelocidadActual(self):
        self.velocidadActual = self.velocidadTuneao + self.velocidadCircumstancias

    def actualizarVelocidadT(self):
        self.velocidadTuneao = self.motor.velocidadAnadida + self.aleron.velocidadAnadida + self.neumaticos.velocidadAnadida + self.velocidad
    
    @staticmethod
    def setVehiculos(lista_vehiculos):
        VehiculoCarrera.listaVehiculos = lista_vehiculos

    @staticmethod
    def getVehiculos():
        return VehiculoCarrera.listaVehiculos

