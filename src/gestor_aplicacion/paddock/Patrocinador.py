from random import random, shuffle, choice, randint

from src.gestor_aplicacion.paddock.Persona import Persona


class Patrocinador(Persona):
    """
    Autores: David Toro Arboleda, Santiago Lopez Ayala, Juan Andres Jimenez Velez, Mariana Valencia Cubillos, Samuel Mira Alvarez
    Descripcion de la clase: La clase "Patrocinador" desempeña un papel fundamental al crear y asignar los atributos asociados. Su importancia radica en su rol de proveer a los equipos con los recursos financieros necesarios para participar en el campeonato. El flujo de dinero es esencial para el funcionamiento fluido de las interacciones dentro del campeonato.
    """

    listaPatrocinadores = []  # Class attribute

    def __init__(self, nombre, plata=0, dineroOfrecer=0, probAceptar=0, patrocinando=None, rosca=None,
                 ciudadesPreferidas=None):
        if plata==0:
            plata = randint(10,100)*100000
            self.dineroOfrecer = plata * randint(3,7) * (1/10)
            self.probAceptar = 1
        else:
            self.dineroOfrecer = dineroOfrecer
            self.probAceptar = probAceptar
        super().__init__(nombre, plata)
        if not(patrocinando):
            self.patrocinando = False
        else:
            self.patrocinando = True
        if not(rosca):
            self.rosca = False
        else:
            self.rosca = True

        self.ciudadesPreferidas = ciudadesPreferidas if ciudadesPreferidas is not None else []
        Patrocinador.listaPatrocinadores.append(self)

        self.redondear()

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
        if numRandom <= self.probAceptar:
            piloto.getEquipo().agregarPatrocinador(self)
            self.setPatrocinando(True)
            piloto.recibir_plata(self.dineroOfrecer)
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
            self.sin_plata()
            self.setDineroOfrecido(self.getPlata())

    def setDineroOfrecido(self, dinero):
        self.dineroOfrecer = dinero

    def setPatrocinadorCampeonato(self):
        """
        Descripcion del metodo: este metodo se encarga de asignar 5 ciudades aleatorias a una lista de ciudadesPreferidas en las cuales si se llega a ganar una carrera el premio se multiplica
        Parametros de entrada: sin argumentos
        Parametros de salida: void
        """
        from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad
        ciudades = Ciudad.get_lista_ciudades()
        shuffle(ciudades)
        self.ciudadesPreferidas.extend(ciudades[:5])
        self.setPlata(self.getPlata() * 5000)

    def redondear(self):
        self.dineroOfrecer = round(self.getDineroOfrecer(), 2)
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
        dineroDisponible = randint(10,15) * 20000
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

    def sin_plata(self):
        self.setDinero(randint(1,10)*100000)

    def recibir_plata(self, plata):
        self.setDinero(self.get_plata()+plata)

    @staticmethod
    def setPatrocinadores(lista_patrocinadores):
        Patrocinador.listaPatrocinadores = lista_patrocinadores

    @staticmethod
    def getPatrocinadores():
        return Patrocinador.listaPatrocinadores

    def setPlata(self,plata):
        self.plata = plata

    def getPlata(self):
        return self.plata

    def setPatrocinando(self,bool):
        self.patrocinando = bool