from random import random, shuffle, choice

from src.gestor_aplicacion.paddock.Persona import Persona
from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad


class Patrocinador(Persona):
    """
    Autores: David Toro Arboleda, Santiago Lopez Ayala, Juan Andres Jimenez Velez, Mariana Valencia Cubillos, Samuel Mira Alvarez
    Descripcion de la clase: La clase "Patrocinador" desempeña un papel fundamental al crear y asignar los atributos asociados. Su importancia radica en su rol de proveer a los equipos con los recursos financieros necesarios para participar en el campeonato. El flujo de dinero es esencial para el funcionamiento fluido de las interacciones dentro del campeonato.
    """

    listaPatrocinadores = []  # Class attribute

    def __init__(self, nombre, plata=0, dineroOfrecer=0, probAceptar=0, patrocinando=False, rosca=True,
                 ciudadesPreferidas=None):
        super().__init__(nombre, plata)
        self.dineroOfrecer = dineroOfrecer
        self.probAceptar = probAceptar
        self.patrocinando = patrocinando
        self.rosca = rosca
        self.ciudadesPreferidas = ciudadesPreferidas if ciudadesPreferidas is not None else []
        Patrocinador.listaPatrocinadores.append(self)

    @classmethod
    def patrocinadoresDisponibles(cls):
        """
        Descripcion del metodo: este metodo se encarga de filtrar una lista de patrocinadores dependiendo si están o no patrocinando a un piloto, también se encarga de poner un patrocinador por defecto para asegurar que la lista no esté vacía
        Parametros de entrada: sin argumentos
        Parametros de salida: Lista de objetos Patrocinador
        """
        patrocinadoresDisponibles = [patrocinador for patrocinador in cls.listaPatrocinadores if
                                     not patrocinador.isPatrocinando()]
        if not patrocinadoresDisponibles:
            default_patrocinador = cls("Default Patrocinador")
            default_patrocinador.setPlata(100000)
            default_patrocinador.setDineroOfrecido(90000)
            patrocinadoresDisponibles.append(default_patrocinador)
        return patrocinadoresDisponibles

    def pensarNegocio(self, piloto):
        """
        Descripcion del metodo: calcula si acepta o no un trato con el piloto dependiendo las probabilidades de aceptar que tenga el patrocinador
        Parametros de entrada: piloto de tipo Piloto
        Parametros de salida: boolean
        """
        import random
        numRandom = random.uniform(0, 1)
        if numRandom < self.probAceptar:
            piloto.getEquipo().agregarPatrocinador(self)
            self.setPatrocinando(True)
            piloto.recibirPlata(self.dineroOfrecer)
            self.setPlata(self.getPlata() - self.dineroOfrecer)
            piloto.setPatrocinador(self)
            return True
        else:
            return False

    def beneficiarPiloto(self, piloto):
        piloto.setHabilidad(piloto.getHabilidad() + 0.1)

    def setDinero(self, dinero):
        self.setPlata(dinero)
        self.setDineroOfrecido(dinero)
        if self.getPlata() <= 0:
            self.sinPlata()
            self.setDineroOfrecido(self.getPlata())

    def setDineroOfrecido(self, dinero):
        self.dineroOfrecer = dinero

    def setPatrocinadorCampeonato(self):
        """
        Descripcion del metodo: este metodo se encarga de asignar 5 ciudades aleatorias a una lista de ciudadesPreferidas en las cuales si se llega a ganar una carrera el premio se multiplica
        Parametros de entrada: sin argumentos
        Parametros de salida: void
        """
        ciudades = Ciudad.getListaCiudades()
        shuffle(ciudades)
        self.ciudadesPreferidas.extend(ciudades[:5])
        self.setPlata(self.getPlata() * 5000)

    def redondear(self):
        self.dineroOfrecer = round(self.dineroOfrecer, 2)
        self.probAceptar = round(self.probAceptar, 2)
        self.dineroOfrecer = round(self.dineroOfrecer, 2)
        super().redondear()

    def setCiudadesPreferidas(self, ciudadesPreferidas):
        self.ciudadesPreferidas = ciudadesPreferidas

    def isPatrocinando(self):
        return self.patrocinando

    def isRosca(self):
        return self.rosca

    def setRosca(self, rosca):
        self.rosca = rosca

    @classmethod
    def setListaPatrocinadores(cls, listaPatrocinadores):
        cls.listaPatrocinadores = listaPatrocinadores

    def getDineroOfrecer(self):
        return self.dineroOfrecer

    def getProbAceptar(self):
        return self.probAceptar

    def setProbAceptar(self, prob):
        self.probAceptar = prob

    @classmethod
    def randomPatrocinador(cls):
        nombre = f"Random Patrocinador {random()}"
        dineroDisponible = random() * 9000.0 + 20000.0
        patrocinador = cls(nombre, dineroDisponible)
        lowerBound = 0.2
        upperBound = 0.8
        numRandom = lowerBound + (upperBound - lowerBound) * random()
        dineroOfrecer = round(dineroDisponible * numRandom, 2)
        lowerBound = 1.0 - dineroOfrecer / dineroDisponible
        upperBound = 1.0
        numRandom = lowerBound + (upperBound - lowerBound) * random()
        probAceptar = round(numRandom, 2)
        return patrocinador

    @classmethod
    def patrocinadorPiloto(cls, piloto, patrocinadores):
        """
        Descripcion del metodo: este metodo se encarga de filtrar una lista de patrocinadores de acuerdo al precio de contrato más el precio del vehículo de un piloto, teniendo en cuenta el atributo dineroOfrecer
        Parametros de entrada: piloto de tipo Piloto y patrocinadores de tipo List[Patrocinador]
        Parametros de salida: List[Patrocinador]
        """
        valor = piloto.getValorContrato() + piloto.getPresupuestoVehiculo()
        patrocinadoresPiloto = [patrocinador for patrocinador in patrocinadores if patrocinador.dineroOfrecer >= valor]
        if not patrocinadoresPiloto:
            default_patrocinador = cls("Default Patrocinador")
            default_patrocinador.setDinero(valor * 2)
            default_patrocinador.setDineroOfrecido(valor)
            patrocinadoresPiloto.append(default_patrocinador)
        return patrocinadoresPiloto

    @classmethod
    def patrocinadorPilotoContrincante(cls, piloto, patrocinadores):
        """
        Descripcion del metodo: este metodo elige un patrocinador de la lista y se lo asigna a un piloto de un equipo contrincante
        Parametros de entrada: piloto de tipo Piloto , patrocinadores de tipo List[Patrocinador]
        Parametros de salida: Patrocinador
        """
        valor = piloto.getValorContrato() + piloto.getPresupuestoVehiculo()
        patrocinadoresPiloto = [patrocinador for patrocinador in patrocinadores if patrocinador.dineroOfrecer >= valor]
        if not patrocinadoresPiloto:
            default_patrocinador = cls("Default Patrocinador")
            default_patrocinador.setDinero(valor * 2)
            default_patrocinador.setDineroOfrecido(valor)
            patrocinadoresPiloto.append(default_patrocinador)
        patrocinador = choice(patrocinadoresPiloto)
        return patrocinador
