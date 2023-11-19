import random

from src.gestor_aplicacion.Decimales import Decimales
from src.gestor_aplicacion.paddock.Chasis import Chasis
from src.gestor_aplicacion.paddock.Pieza import Pieza


class VehiculoCarrera(Chasis, Decimales):
    listaVehiculos = []
    idActual = 1

    def __init__(self, chasis, piloto):
        super().__init__(chasis.marca, chasis.modelo, chasis.velocidad, chasis.maniobrabilidad, chasis.precio)
        self.piloto = piloto
        self.id = VehiculoCarrera.idActual
        VehiculoCarrera.idActual += 1
        self.tiempo = 0
        self.distanciaRecorrida = 0
        self.terminado = False
        self.morido = False
        self.velocidadTuneao = 0
        self.velocidadCircumstancias = 0
        self.velocidadActual = 0
        self.probabilidadChoque = max(1 - piloto.habilidad - chasis.maniobrabilidad, 0.3)
        self.gasolina = 100
        self.piezasComprar = []
        self.redondear()
        self.motor = None
        self.aleron = None
        self.neumaticos = None
        VehiculoCarrera.listaVehiculos.append(self)

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
        if self.motor is None or self.aleron is None or self.neumaticos is None:
            self.velocidadTuneao = self.velocidad
        else:
            self.velocidadTuneao = self.motor.velocidadAnadida + self.aleron.velocidadAnadida + self.neumaticos.velocidadAnadida + self.velocidad
        self.actualizarVelocidadActual()

    @staticmethod
    def setVehiculos(lista_vehiculos):
        VehiculoCarrera.listaVehiculos = lista_vehiculos

    @staticmethod
    def getVehiculos():
        return VehiculoCarrera.listaVehiculos

    def setMotor(self, motor):
        self.motor = motor
        self.actualizarVelocidadT()

    def setNeumaticos(self, neumaticos):
        self.neumaticos = neumaticos
        self.actualizarVelocidadT()

    def setAleron(self, aleron):
        self.aleron = aleron
        self.actualizarVelocidadT()



    @classmethod
    def vehiculos_piloto(cls, piloto):
        vehiculos_del_piloto = []
        for vehiculo in cls.listaVehiculos:
            if vehiculo.piloto == piloto:
                vehiculos_del_piloto.append(vehiculo)
        if len(vehiculos_del_piloto) == 0:
            return None
        else:
            return vehiculos_del_piloto

    @classmethod
    def cantidad_vehiculos_default(cls):
        cant = 0
        for carro in cls.listaVehiculos:
            if (carro.marca == "Default"):
                cant+=1
        return cant
    @classmethod
    def crear_vehiculo_pilotos_no_elegidos(cls,piloto):
        modelo = str(cls.cantidad_vehiculos_default() + 1 )
        velocidad = random.randint(1,59) + 200
        precio = random.randint(1,5) * 3000
        maniobrabilidad = random.randint(2,4) / 10
        aleron = Pieza.piezaNoElegida("A")
        llantas = Pieza.piezaNoElegida("N")
        motor = Pieza.piezaNoElegida("M")
        chasis_default = Chasis.create_chasis("Default", modelo)
        vechiculo = cls(chasis_default, piloto)
        vechiculo.setMotor(motor)
        vechiculo.setNeumaticos(llantas)
        vechiculo.setAleron(aleron)

        return vechiculo





