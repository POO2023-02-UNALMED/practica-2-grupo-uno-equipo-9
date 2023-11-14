from src.gestor_aplicacion.campeonato import Campeonato
from src.gestor_aplicacion.paddock.Circuito import Circuito
from src.gestor_aplicacion.ubicaciones.Continente import Continente


campeonato = Campeonato.campeonatos[0]

circuitos = Circuito.circuitos_ubicacion(campeonato)

