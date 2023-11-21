import pickle
from src.gestor_aplicacion.campeonato.Campeonato import Campeonato
from src.gestor_aplicacion.campeonato.DirectorCarrera import DirectorCarrera
from src.gestor_aplicacion.campeonato.Equipo import Equipo
from src.gestor_aplicacion.campeonato.VehiculoCarrera import VehiculoCarrera
from src.gestor_aplicacion.paddock.Patrocinador import Patrocinador
from src.gestor_aplicacion.paddock.Pieza import Pieza
from src.gestor_aplicacion.paddock.Piloto import Piloto
from src.gestor_aplicacion.paddock.Chasis import Chasis
from src.gestor_aplicacion.paddock.Circuito import Circuito
from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad

class Deserializado():

    @staticmethod
    def deserializar():

        #CAMPEONATOS
        archivo = open('base_Datos/temp/datosCampeonatos.txt','rb')
        datos = pickle.load(archivo)
        Campeonato.setCampeonatos(datos)
        archivo.close()

        #CIUDADES
        archivo = open('base_Datos/temp/datosCiudades.txt','rb')
        datos = pickle.load(archivo)
        Ciudad.set_lista_ciudades(datos) 
        archivo.close()

        #DIRECTORES
        archivo = open('base_Datos/temp/datosDirectores.txt','rb')
        datos = pickle.load(archivo)
        DirectorCarrera.setListaDirectores(datos)
        archivo.close()

        #EQUIPOS
        archivo = open('base_Datos/temp/datosEquipos.txt','rb')
        datos = pickle.load(archivo)
        Equipo.setEquipos(datos)
        archivo.close()

        #PATROCINADORES
        archivo = open('base_Datos/temp/datosPatrocinadores.txt','rb')
        datos = pickle.load(archivo)
        Patrocinador.setPatrocinadores(datos) 
        archivo.close()

        #PIEZAS
        archivo = open('base_Datos/temp/datosPiezas.txt','rb')
        datos = pickle.load(archivo)
        Pieza.setPiezas(datos)
        archivo.close()

        #PILOTOS
        archivo = open('base_Datos/temp/datosPilotos.txt','rb')
        datos = pickle.load(archivo)
        Piloto.setPilotos(datos)
        archivo.close()

        #CHASIS
        archivo = open('base_Datos/temp/datosChasis.txt','rb')
        datos = pickle.load(archivo)
        Chasis.set_lista_chasis(datos)
        archivo.close()

        #VEHICULO CARRERA
        archivo = open('base_Datos/temp/datosVehiculos.txt','rb')
        datos = pickle.load(archivo)
        VehiculoCarrera.setVehiculos(datos)
        archivo.close()

        #CIRCUITOS
        archivo = open('base_Datos/temp/datosCircuitos.txt','rb')
        datos = pickle.load(archivo)
        Circuito.set_circuitos(datos)
        archivo.close()

        # TODO: VERIFICAR LAS COSAS
        for vehiculo in VehiculoCarrera.listaVehiculos:
            for pilotico in Piloto.listaPilotos:
                if vehiculo.piloto.get_nombre() == pilotico.get_nombre():
                    vehiculo.piloto = pilotico
                    break

        for piloto in Piloto.listaPilotos:
            for equipo in Equipo.equipos:
                if equipo.get_nombre() == piloto.contrato.get_nombre():
                    piloto.contrato = equipo
                    break

        for campeonato in Campeonato.campeonatos:
            if campeonato._desbloqueado:
                lista_pilotos=[]
                lista_equipos=[]
                for piloto in Piloto.listaPilotos:
                    for pilotico in campeonato._listaPilotos:
                        if pilotico.get_nombre() == piloto.get_nombre():
                            lista_pilotos.append(piloto)
                            break
                for equipo in Equipo.equipos:
                    for equipito in campeonato._listaEquipos:
                        if equipito.get_nombre() == equipo.get_nombre():
                            lista_equipos.append(equipo)
                            break
                campeonato._listaEquipos = lista_equipos
                campeonato._listaPilotos = lista_pilotos

