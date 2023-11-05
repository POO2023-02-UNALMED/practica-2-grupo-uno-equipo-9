import random

from src.gestor_aplicacion.Decimales import Decimales


class Pieza(Decimales):
    """
    Autores: David Toro Arboleda, Santiago Lopez Ayala, Juan Andres Jimenez Velez, Mariana Valencia Cubillos, Samuel Mira Alvarez
    Descripcion de la clase: La funcion principal de esta clase es la asignacion de atributos a cada una de las piezas de los vehiculos que compiten en las carreras del campeonato.
    """

    idActual = 0
    piezas = []
    piezasContrabando = []

    def __init__(self, danado, velocidadAnadida, maniobrabilidadAnadida, marca, nombre, precio, tipo, contrabando=False):
        self.id = Pieza.idActual
        Pieza.idActual += 1
        self.danado = danado
        self.velocidadAnadida = velocidadAnadida
        self.maniobrabilidadAnadida = maniobrabilidadAnadida
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.elegida = False
        if contrabando:
            Pieza.piezasContrabando.append(self)
        else:
            Pieza.piezas.append(self)

    @classmethod
    def piezaNoElegida(cls, tipo):
        random_speed = random.uniform(0, 20)
        random_maniobrability = random.uniform(0.1, 0.4)
        random_price = random.uniform(100, 1000)
        return cls(False, random_speed, random_maniobrability, "Default", "", random_price, tipo)

    @classmethod
    def combinacionesDisponibles(cls, vehiculoCarrera, neumatico):
        combinaciones = []
        motores_disponibles = cls.motoresDisponibles(vehiculoCarrera.marca)
        aleron_disponibles = cls.aleronesDisponibles(vehiculoCarrera.marca)
        neumaticos_disponibles = cls.neumaticosDisponibles(vehiculoCarrera.marca)

        for motor in motores_disponibles:
            for aleron in aleron_disponibles:
                combinacion = [motor, aleron, neumatico]
                price = sum(p.getPrecio() for p in combinacion)

                if price <= vehiculoCarrera.piloto.equipo.plata:
                    combinaciones.append(combinacion)

        return combinaciones

    @classmethod
    def filterAlerones(cls, combinaciones):
        alerones = [pieza for combinacion in combinaciones for pieza in combinacion if pieza.getTipo() == "A"]
        alerones_distintos = list(set(alerones))
        return alerones_distintos

    @classmethod
    def filterNeumaticos(cls, combinaciones):
        neumaticos = [pieza for combinacion in combinaciones for pieza in combinacion if pieza.getTipo() == "N"]
        neumaticos_distintos = list(set(neumaticos))
        return neumaticos_distintos

    @classmethod
    def filterMotores(cls, combinaciones):
        motores = [pieza for combinacion in combinaciones for pieza in combinacion if pieza.getTipo() == "M"]
        motores_distintos = list(set(motores))
        return motores_distintos

    @classmethod
    def piezasDisponibles(cls):
        return [pieza for pieza in cls.piezas if not pieza.isDanado() and not pieza.isElegida()]

    @classmethod
    def motoresDisponibles(cls, marca):
        piezas_disponibles = cls.piezasDisponibles()
        return [pieza for pieza in piezas_disponibles if pieza.getTipo() == "M" and pieza.getMarca() == marca]

    @classmethod
    def neumaticosDisponibles(cls, marca):
        piezas_disponibles = cls.piezasDisponibles()
        return [pieza for pieza in piezas_disponibles if pieza.getTipo() == "N" and pieza.getMarca() == marca]

    @classmethod
    def aleronesDisponibles(cls, marca):
        piezas_disponibles = cls.piezasDisponibles()
        return [pieza for pieza in piezas_disponibles if pieza.getTipo() == "A" and pieza.getMarca() == marca]

    @classmethod
    def precioTotal(cls, piezas, vehiculoCarrera):
        total_price = sum(p.getPrecio() for p in piezas)
        vehiculoCarrera.setPiezasComprar(piezas)
        return total_price

    def arreglar(self):
        self.danado = False

    def comprar(self, vehiculoCarrera):
        equipo = vehiculoCarrera.piloto.equipo
        if self.precio <= equipo.plata:
            equipo.plata -= self.precio
            self.danado = False
            vehiculoCarrera.maniobrabilidad += self.maniobrabilidadAnadida
            return True
        else:
            return False

    def redondear(self):
        self.precio = self.dosDecimales(self.precio)
        self.velocidadAnadida = self.dosDecimales(self.velocidadAnadida)
        self.maniobrabilidadAnadida = self.dosDecimales(self.maniobrabilidadAnadida)

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Nombre: {self.nombre}, Precio: {self.precio}"

    def isDanado(self):
        return self.danado

    def getVelocidadAnadida(self):
        return self.velocidadAnadida

    def getManiobrabilidadAnadida(self):
        return self.maniobrabilidadAnadida

    def getPrecio(self):
        return self.precio

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def getMarca(self):
        return self.marca

    def getNombre(self):
        return self.nombre

    def isElegida(self):
        return self.elegida

    def setDanado(self, danado):
        self.danado = danado

    def setVelocidadAnadida(self, velocidadAnadida):
        self.velocidadAnadida = velocidadAnadida

    def setManiobrabilidadAnadida(self, maniobrabilidadAnadida):
        self.maniobrabilidadAnadida = maniobrabilidadAnadida

    def setPrecio(self, precio):
        self.precio = precio

    def setId(self, id):
        self.id = id

    def setTipo(self, tipo):
        self.tipo = tipo

    def setMarca(self, marca):
        self.marca = marca

    def setNombre(self, nombre):
        self.nombre = nombre

    def setElegida(self, elegida):
        self.elegida = elegida

    @staticmethod
    def getIdActual():
        return Pieza.idActual

    @staticmethod
    def setIdActual(idActual):
        Pieza.idActual = idActual

    @staticmethod
    def getPiezas():
        return Pieza.piezas

    @staticmethod
    def setPiezas(piezas):
        Pieza.piezas = piezas

    @staticmethod
    def getPiezasContrabando():
        return Pieza.piezasContrabando

    @staticmethod
    def setPiezasContrabando(piezasContrabando):
        Pieza.piezasContrabando = piezasContrabando
