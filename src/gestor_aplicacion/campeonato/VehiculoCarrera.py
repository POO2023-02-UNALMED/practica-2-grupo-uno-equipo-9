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
        self.chasis = chasis
        self.id = VehiculoCarrera.idActual
        VehiculoCarrera.idActual += 1
        self.tiempo = 0
        self.distanciaRecorrida = 0
        self.terminado = False
        self.morido = False
        self.velocidadTuneao = chasis.velocidad
        self.velocidadCircumstancias = 0
        self.velocidadActual = chasis.velocidad
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
            self.actualizar_velocidadT()
        elif tipoPieza == "N":
            self.neumaticos = pieza
            self.actualizar_velocidadT()
        elif tipoPieza == "M":
            self.motor = pieza
            self.actualizar_velocidadT()

    def configurarVehiculo(self, piezas):
        for pieza in piezas:
            self.cambiarPieza(pieza)
            pieza.elegida = True
        self.llenar_gasolina()

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

    @staticmethod
    def setVehiculos(lista_vehiculos):
        VehiculoCarrera.listaVehiculos = lista_vehiculos

    @staticmethod
    def getVehiculos():
        return VehiculoCarrera.listaVehiculos

    def setMotor(self, motor):
        self.motor = motor
        self.actualizar_velocidadT()

    def setNeumaticos(self, neumaticos):
        self.neumaticos = neumaticos
        self.actualizar_velocidadT()

    def setAleron(self, aleron):
        self.aleron = aleron
        self.actualizar_velocidadT()



    @classmethod
    def vehiculos_piloto(cls, piloto):
        vehiculos_del_piloto = []
        for vehiculo in cls.listaVehiculos:
            if vehiculo.piloto.get_nombre() == piloto.get_nombre():
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
        aleron = Pieza.piezaNoElegida("A")
        llantas = Pieza.piezaNoElegida("N")
        motor = Pieza.piezaNoElegida("M")
        chasis_default = Chasis.create_chasis("Default", modelo)
        vechiculo = cls(chasis_default, piloto)
        vechiculo.setMotor(motor)
        vechiculo.setNeumaticos(llantas)
        vechiculo.setAleron(aleron)
        vechiculo.actualizar_velocidadT()

        return vechiculo

    def setPiezasComprar(self, piezas):
        self.piezasComprar = piezas

    @classmethod
    def manipular_vehiculos(cls, vehiculo_participantes, pilotos_desfavorecidos, piloto_maldito, piloto, plata,
                            director_carrera, is_method_1=True):
        """
        Manipula la posición de los vehículos en una carrera, aplicando diferentes efectos según las condiciones de los pilotos.

        Parametros de entrada:
        - vehiculo_participantes: Lista de vehículos participantes (tipo ArrayList<VehiculoCarrera>)
        - pilotos_desfavorecidos: Lista de pilotos desfavorecidos (tipo ArrayList<Piloto>)
        - piloto_maldito: Piloto maldito (tipo Piloto)
        - piloto: Piloto (tipo Piloto)
        - plata: Cantidad de plata (tipo double)
        - director_carrera: Director de carrera (tipo DirectorCarrera)
        - is_method_1: Booleano para indicar qué versión del método ejecutar

        Parametros de salida: Lista de vehículos con sus posiciones o velocidades manipuladas.
        """
        rand = random.Random()
        posiciones_corruptas = []

        for vehiculo_carrera in vehiculo_participantes:
            if is_method_1:
                if vehiculo_carrera.piloto == piloto_maldito:
                    vehiculo_carrera.distanciaRecorrida = -50 - rand.randint(1, 10) * 30
                elif vehiculo_carrera.piloto == piloto:
                    vehiculo_carrera.distanciaRecorrida = 50 + rand.randint(1, 10) * 30
                elif vehiculo_carrera.piloto in pilotos_desfavorecidos:
                    vehiculo_carrera.distanciaRecorrida = -10 - rand.randint(1, 10) * 20
            else:
                if vehiculo_carrera.piloto == piloto:
                    vehiculo_carrera.velocidadActual += 50
                else:
                    vehiculo_carrera.velocidadActual = max(vehiculo_carrera.velocidadActual-20,150)

            posiciones_corruptas.append(vehiculo_carrera)

        return posiciones_corruptas

    def aprovechar_drs(self):
        random_number = random.randint(1, 10)
        if random_number == 1:
            self.aleron.danar()
            self.actualizar_velocidad_actual()
        elif random_number <= 9:
            self.velocidad_circunstancias = 50
            self.actualizar_velocidad_actual()
        else:
            random_float = random.random()
            if random_float > 0.5:
                self.velocidad_circunstancias = 30
            else:
                self.velocidad_circunstancias = 60
            self.actualizar_velocidad_actual()

    def frenar(self):
        if self.velocidadActual > 100:
            self.velocidadActual -= 100
        else:
            self.velocidadActual = 70

    def hacer_maniobra(self):
        random_float = random.uniform(0, 1)
        if random_float > 0.5:
            self.velocidadActual += self.velocidadActual * 0.1
        else:
            self.velocidadActual -= self.velocidadActual * 0.1
        self.actualizar_velocidad_actual()

    def defender(self):
        random_float = random.uniform(0, 1)
        if random_float > 0.5:
            self.velocidadActual += self.velocidadActual * 0.05
        else:
            self.velocidadActual -= self.velocidadActual * 0.05
        self.actualizar_velocidad_actual()

    def derrapar(self):
        random_float = random.uniform(0, 1)
        if random_float > 0.5:
            self.velocidadActual -= self.velocidadActual * 0.1
        else:
            self.velocidadActual += self.velocidadActual * 0.1
        self.actualizar_velocidad_actual()

    def llenar_gasolina(self):
        self.gasolina = 100

    def reparar_vehiculo(self):
        precio = (self.motor.precio + self.aleron.precio + self.neumaticos.precio) / 2
        equipo = self.piloto.equipo
        if equipo.plata >= precio:
            equipo.plata -= precio
            self.aleron.arreglar()
            self.motor.arreglar()
            self.neumaticos.arreglar()
            return True
        else:
            return False

    def actualizar_velocidad_actual(self):
        """
        Description: Updates the actual speed of the vehicle based on tuned speed and circumstances speed.
        Parameters: None
        Returns: None
        """
        self.actualizar_velocidadT()  # Update tuned speed
        self.velocidadActual = self.velocidadTuneao + self.velocidadCircumstancias  # Update actual speed

    def actualizar_velocidadT(self):
        """
        Description: Updates the tuned speed of the vehicle based on the speed of individual parts.
        Parameters: None
        Returns: None
        """
        self.velocidad = self.chasis.velocidad
        if self.aleron is not None and not self.aleron.isDanado:
            self.velocidadTuneao = self.get_velocidad() + self.aleron.getVelocidadAnadida()

        if self.neumaticos is not None and not self.neumaticos.isDanado:
            self.velocidadTuneao = self.get_velocidad() + self.neumaticos.getVelocidadAnadida()

        if self.motor is not None and not self.motor.isDanado:
            self.velocidadTuneao = self.get_velocidad() + self.motor.getVelocidadAnadida()

        # self.actualizarVelocidadActual()  # Update actual speed



    def getDistanciaRecorrida(self):
        return self.distanciaRecorrida

    def setDistanciaRecorrida(self, distanciaRecorrida):
        self.distanciaRecorrida = distanciaRecorrida

    def isTerminado(self):
        return self.terminado

    def setTerminado(self, terminado):
        self.terminado = terminado

    def isMorido(self):
        return self.morido

    def setMorido(self, morido):
        self.morido = morido

    def getVelocidadTuneao(self):
        return self.velocidadTuneao

    def setVelocidadTuneao(self, velocidadTuneao):
        self.velocidadTuneao = velocidadTuneao

    def getProbabilidadChoque(self):
        return self.probabilidadChoque

    def setProbabilidadChoque(self, probabilidadChoque):
        self.probabilidadChoque = probabilidadChoque

    def getGasolina(self):
        return self.gasolina

    def setGasolina(self, gasolina):
        self.gasolina = gasolina

    def getPiloto(self):
        return self.piloto

    def setPiloto(self, piloto):
        self.piloto = piloto

    def getTiempo(self):
        return self.tiempo

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getVelocidadActual(self):
        return self.velocidadActual

    def setVelocidadActual(self, velocidadActual):
        self.velocidadActual = velocidadActual

    def getVelocidadCircumstancias(self):
        return self.velocidadCircumstancias

    def setVelocidadCircumstancias(self, velocidadCircumstancias):
        self.velocidadCircumstancias = velocidadCircumstancias

    def getMotor(self):
        return self.motor
    def getNeumaticos(self):
        return self.neumaticos
    def getAleron(self):
        return self.aleron
    def getPiezasComprar(self):
        return self.piezasComprar
