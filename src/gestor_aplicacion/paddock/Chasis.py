import random

from src.gestor_aplicacion.Decimales import Decimales


class Chasis(Decimales):
    listaChasis = []  # Class attribute
    idActual = 0  # Class attribute

    def __init__(self, marca, modelo, velocidad, maniobrabilidad, precio=0):
        self.id = Chasis.idActual
        Chasis.idActual += 1
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.maniobrabilidad = maniobrabilidad
        self.precio = precio
        Chasis.listaChasis.append(self)

    @classmethod
    def chasis_disponible(cls, piloto):
        precio_maximo = piloto.presupuesto_vehiculo * 0.6
        lista_chasis = [chasis for chasis in Chasis.listaChasis if chasis.precio > precio_maximo and chasis.marca != "Default"]
        return lista_chasis

    def redondear(self):
        self.velocidad = self.dos_decimales(self.velocidad)
        self.maniobrabilidad = self.dos_decimales(self.maniobrabilidad)
        self.precio = self.dos_decimales(self.precio)

    def comprar(self, piloto):
        piloto.equipo.plata -= self.precio
        vehiculo = VehiculoCarrera(self, piloto)
        return vehiculo

    def morir(self):
        self.velocidad = 0
        self.maniobrabilidad = 0

    # Getter and setter methods
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_maniobrabilidad(self):
        return self.maniobrabilidad

    def set_maniobrabilidad(self, maniobrabilidad):
        self.maniobrabilidad = maniobrabilidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    @staticmethod
    def get_lista_chasis():
        return Chasis.listaChasis

    @staticmethod
    def set_lista_chasis(lista_chasis):
        Chasis.listaChasis = lista_chasis

    @staticmethod
    def get_id_actual():
        return Chasis.idActual

    @staticmethod
    def set_id_actual(id_actual):
        Chasis.idActual = id_actual

