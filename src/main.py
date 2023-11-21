import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the sys.path
sys.path.append(os.path.join(current_dir, '..'))

import random
import tkinter as tk
from tkinter import messagebox

from PIL import ImageSequence
from PIL import Image, ImageTk
from tkinter import ttk

import sv_ttk as sk

# Imports de las clases
from src.base_datos.Serializado import Serializado
from src.base_datos.Deserializado import Deserializado
from src.gestor_aplicacion.campeonato.Carrera import Carrera
from src.gestor_aplicacion.campeonato.DirectorCarrera import DirectorCarrera
from src.gestor_aplicacion.campeonato.Campeonato import Campeonato
from src.gestor_aplicacion.campeonato.Equipo import Equipo
from src.gestor_aplicacion.campeonato.VehiculoCarrera import VehiculoCarrera
from src.gestor_aplicacion.paddock.Chasis import Chasis
from src.gestor_aplicacion.paddock.Circuito import Circuito
from src.gestor_aplicacion.paddock.Patrocinador import Patrocinador
from src.gestor_aplicacion.paddock.Pieza import Pieza
from src.gestor_aplicacion.paddock.Piloto import Piloto
from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad
from src.gestor_aplicacion.ubicaciones.Continente import Continente
from src.excepciones.IncorrectTypeException import IncorrectTypeException
from src.excepciones.NoInputException import NoInputException
from src.excepciones.NullPointerException import NullPointerException
from src.excepciones.OutOfBoundsException import OutOfBoundsException
from src.excepciones.RepeatedSelectionException import RepeatedSelectionException


class FieldFrame(tk.Frame):

    def __init__(self, parent, color, nombre_proceso="", descripcion="", logo_path="random"):
        super().__init__(parent, width=1000, height=600, bg=color)
        self.nombre_proceso = nombre_proceso
        self.descripcion = descripcion

        description_label = tk.Label(self, text=descripcion, anchor="center")

        # inner_frame = tk.Frame(self, padx=5, pady=5, bg=color)
        # inner_frame.grid(row=0, column=0, columnspan=2, pady=5)

        # Create labels for the title and description
        title_label = tk.Label(self, text=nombre_proceso, font=("Helvetica", 16), anchor="center", width=70)
        self.configure(padx=20, pady=20)
        # self.grid(row=0, column=0, sticky="nsew")

        # Use grid to make labels span the same width as the window
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        title_label.configure(justify="center")
        description_label.grid(row=1, column=0, padx=20, sticky="nsew")
        description_label.configure(justify="center")

        if logo_path == "random":
            img_paths = ["src/img/formula-1-3.png", "src/img/podio.png", "src/img/fato-de-corrida.png", "src/img/teste.png",
                         "src/img/car.png", "src/img/maquineta.png", "src/img/comentarista.png",
                         "src/img/bandeira-de-corrida.png", "src/img/bomba-de-combustivel.png", "src/img/boot.png",
                         "src/img/capacete.png", "src/img/chaqueta-de-carreras.png", "src/img/chassis.png", "src/img/comecar.png",
                         "src/img/corridas.png", "src/img/equipe-tecnica.png", "src/img/f1.ico", "src/img/ferramentas-de-reparacao.png",
                         "src/img/formula-1-1.png", "src/img/formula-1-2.png", "src/img/luvas.png", "src/img/motorista.png",
                         "src/img/o-circuito.png", "src/img/parada.png", "src/img/perfurador.png", "src/img/pista-de-corrida.png",
                         "src/img/pneus.png", "src/img/roda.png", "src/img/semaforo.png", "src/img/trofeu.png", "src/img/velocimetro.png",
                         "src/img/videogame.png", "src/img/volante.png", "src/img/formula-1-4.png"]
            logo_path = random.choice(img_paths)


        self.img = Image.open(logo_path)
        resized_image = self.img.resize((50, 50))

        # Load the logo image
        self.logo_img1 = ImageTk.PhotoImage(resized_image)
        self.logo_img2 = ImageTk.PhotoImage(resized_image)

        # Create a label for the logo and place it in the right top corner
        logo_label1 = tk.Label(self, image=self.logo_img1)
        logo_label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        logo_label1.configure(justify="center")
        logo_label2 = tk.Label(self, image=self.logo_img2)
        logo_label2.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        logo_label2.configure(justify="center")


class MenuApp:
    def __init__(self, root):
        self.menu_bar = None
        self.root = root
        # self.root.geometry("1200x600")
        sk.set_theme("dark")
        self.frames = {}  # Dictionary to store frames

        self.create_frames()
        self.acerca_de("acerca_de")
        self.create_menu()

    def create_frames(self):
        self.frames["app"] = FieldFrame(self.root, None, "Aplicacion", "Bienvenido a la aplicacion de GP Racing")
        self.frames["preparar_campeonato"] = FieldFrame(self.root, None, "Preparar Un Nuevo Campeonato",
                                                        "Aqui puedes preparar un nuevo campeonato desde cero!")
        self.frames["planificar_calendario"] = FieldFrame(self.root, None, "Planificar Calendario de Carreras",
                                                          "Aqui puedes planificar el calendario de carreras de un campeonato")
        self.frames["personalizar_vehiculo"] = FieldFrame(self.root, None, "Personalizar Vehiculo de Carreras",
                                                          "Aqui puedes personalizar tu vehiculo de carreras. Comprar piezas, chasis, etc.")
        self.frames["forjar_alianza"] = FieldFrame(self.root, None, "Forjar Alianza con el Maestro de Carreras,",
                                                   "Quizas es buena idea hablar con algun Director de Carrera antes que empiece el campeonato\n"
                                                   "Esperamos que no te arrepientas...~")
        self.frames["gp_racing"] = FieldFrame(self.root, None, "GP Racing",
                                              "Es momento de poner a prueba tus habilidades en la pista!")
        self.frames["acerca_de"] = FieldFrame(self.root, None)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # sub menu archivo
        archivo = tk.Menu(self.menu_bar, tearoff=0)
        archivo.add_command(label='Aplicacion', command=lambda: self.aplicacion())
        archivo.add_command(label='Salir', command=lambda: self.pasar_a_ventana_inicial())
        self.menu_bar.add_cascade(label='Archivo', menu=archivo)

        # sub menu procesos y consultas
        procesos_consultas = tk.Menu(self.menu_bar, tearoff=False)
        procesos_consultas.add_command(label='Preparar Nuevo Campeonato',
                                       command=lambda: self.change_frame('preparar_campeonato'))
        procesos_consultas.add_command(label="Planificar Calendario de Carreras",
                                       command=lambda: self.change_frame("planificar_calendario"))
        procesos_consultas.add_separator()
        procesos_consultas.add_command(label='Personalizar Vehiculo de Carreras',
                                       command=lambda: self.change_frame('personalizar_vehiculo'))
        procesos_consultas.add_command(label='Forjar Alianza con el Maestro de Carreras',
                                       command=lambda: self.change_frame('forjar_alianza'))
        procesos_consultas.add_command(label='GP Racing', command=lambda: self.change_frame('gp_racing'))
        self.menu_bar.add_cascade(label='Procesos y Consultas', menu=procesos_consultas)

        # sub menu ayuda
        ayuda = tk.Menu(self.menu_bar, tearoff=False)
        ayuda.add_command(label='Acerca de', command=lambda: self.acerca_de_2())
        ayuda.add_command(label='Guardar', command=lambda: Serializado.serializar())

        self.menu_bar.add_cascade(label='Ayuda', menu=ayuda)

        # Putting the Initiation Buttons

        # Prepare a New Championship
        boton_fun_1 = tk.Button(self.frames["preparar_campeonato"], text="Comenzar a Preparar el Campeonato",
                                command=lambda: self.preparar_campeonato("preparar_campeonato"))
        boton_fun_1.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Plan a New Calendar
        boton_fun_2 = tk.Button(self.frames["planificar_calendario"], text="Planifiquemos el Calendario de carreras",
                                command=lambda: self.planificar_calendario("planificar_calendario"))
        boton_fun_2.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Personalize a Vehicle
        boton_fun_3 = tk.Button(self.frames["personalizar_vehiculo"], text="Personaliza tu Vehiculo de Carreras",
                                command=lambda: self.personalizar_vehiculo("personalizar_vehiculo"))
        boton_fun_3.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Forging an alliance with a Race Master
        boton_fun_4 = tk.Button(self.frames["forjar_alianza"], text="Forjar una amistad con un Maestro de Carreras",
                                command=lambda: self.forjar_amistad("forjar_alianza"))
        boton_fun_4.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # GOTTA GO FAST
        boton_fun_5 = tk.Button(self.frames["gp_racing"], text="¡GOTTA RUN!",
                                command=lambda: self.simulacion_campeonato("gp_racing"))
        boton_fun_5.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

    def pasar_a_ventana_inicial(self):
        root.iconify()
        ventana.deiconify()
        ventana.tkraise()

    def aplicacion(self):
        self.acerca_de("acerca_de")
        tk.messagebox.showinfo("Aplicacion",
                               "La aplicación brinda la posibilidad de gestionar de manera completa un campeonato de carreras automovilísticas, permitiendo desde la planificación de eventos y la selección de directores de carrera hasta la personalización de vehículos. Con opciones flexibles para escoger fechas, dificultades y ubicaciones, así como la elección de circuitos y ciudades, los usuarios pueden definir premios y disfrutar de una experiencia emocionante. La aplicación se presenta de manera sencilla y modular, diseñada para proporcionar una gestión integral y emocionante de los campeonatos.")

    def acerca_de_2(self):
        self.acerca_de("acerca_de")
        tk.messagebox.showinfo("Acerca de",
                               "Bienvenido a nuestra emocionante aplicación de gestión de campeonatos de carreras automovilísticas. Este proyecto ha sido cuidadosamente desarrollado por un talentoso equipo de autores comprometidos con brindar una experiencia integral a los usuarios. Santiago Lopez Ayala, David Toro Arboleda, Juan Andrés Jiménez Vélez, Mariana Valencia Cubillos y Samuel Mira Álvarez son los mentes creativas detrás de esta aplicación, cada uno contribuyendo con su experiencia única para hacer de esta plataforma una herramienta envolvente y emocionante. ¡Explora las emocionantes funcionalidades que hemos creado para ti y sumérgete en el mundo apasionante de la gestión de campeonatos automovilísticos!")

    # To change frames
    def change_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()

    # Funcionalidad 1: Preparar un Nuevo Campeonato
    def preparar_campeonato(self, frame_name):
        # Metodos importantes para la funcionalidad
        # Para frame 1
        def elegir_continente():
            global continente, campeonatos_para_elegir
            try:
                lista_continentes = [c for c in Continente]
                if entry1.get()=="":
                    missing_fields = ["Seleccion de Continente"]
                    raise NoInputException("", missing_fields)
                continente = lista_continentes[int(entry1.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el continente " + continente.value)

                campeonatos_disponibles = Campeonato.campeonatosDisponibles()
                campeonatos_continente = Campeonato.campeonatosContinente(continente)
                campeonatos_para_elegir = []
                for campeonato in campeonatos_disponibles:
                    if campeonato.getContinente() == continente:
                        campeonatos_para_elegir.append(campeonato)
                jj = 1

                for campeonatico in campeonatos_para_elegir:
                    tablaCampeonatos.insert(parent='', index=tk.END, values=(jj, campeonatico.getNombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            except NoInputException:
                pass
            except IndexError:
                raise OutOfBoundsException(1,len(lista_continentes))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 2
        def elegir_campeonato():
            global continente, campeonato_elegido, campeonatos_para_elegir, equipos_disponibles
            try:
                if entry2.get()=="":
                    missing_fields = ["Seleccion de Campeonato"]
                    raise NoInputException("", missing_fields)
                campeonato_elegido = campeonatos_para_elegir[int(entry2.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato_elegido.getNombre())

                equipos_continente = Equipo.equipos_continente(continente)
                equipos_disponibles = Equipo.equipos_disponibles(equipos_continente)
                # Colocar los equipos disponibles
                jj = 1
                for equipo in equipos_disponibles:
                    tablaEquipos.insert(parent='', index=tk.END, values=(jj, equipo.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame2.grid_remove()
                frame2.grid_forget()
                frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame3.tkraise()
            except NoInputException:
                pass
            except IndexError:
                raise OutOfBoundsException(1,len(campeonatos_para_elegir))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 3
        def elegir_equipo():
            global equipo_elegido, campeonato_elegido, equipos_disponibles, participantes
            try:
                if entry3.get()=="":
                    missing_fields = ["Seleccion de Equipo"]
                    raise NoInputException("", missing_fields)
                equipo_elegido = equipos_disponibles[int(entry3.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el equipo " + equipo_elegido.get_nombre())
                participantes = Equipo.elegir_contrincantes(equipo_elegido, campeonato_elegido, equipos_disponibles)
                campeonato_elegido._listaEquipos = participantes
                jj = 1
                for equipo in participantes:
                    tablaParticipantes.insert(parent='', index=tk.END, values=(jj, equipo.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame3.grid_remove()
                frame3.grid_forget()
                frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame4.tkraise()
            except NoInputException:
                pass
            except IndexError:
                raise OutOfBoundsException(1,len(equipos_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 4
        def confirmar_equipos():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo
            try:
                # tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
                pilotos_disponibles = Piloto.pilotos_disponibles()
                pilotos_equipo = Piloto.pilotos_equipo(equipo_elegido, pilotos_disponibles)
                jj = 1
                for piloto in pilotos_equipo:
                    tablaPilotos.insert(parent='', index=tk.END, values=(jj, piloto.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame4.grid_remove()
                frame4.grid_forget()
                frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame5.tkraise()
            except:
                pass

        # Para frame 5.1
        def elegir_primer_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, pilotos_participar
            try:
                if entry5_1.get()=="":
                    missing_fields = ["Seleccion de Piloto"]
                    raise NoInputException("", missing_fields)
                piloto_1 = pilotos_equipo[int(entry5_1.get()) - 1]
                piloto_1.set_elegido(True)
                piloto_1.set_desbloqueado(True)
                pilotos_participar = []
                pilotos_participar.append(piloto_1)
                listbox5.delete(int(entry5_1.get()) - 1)
                # Quitar label y boton
                entry5_1.destroy()
                button5_1.destroy()
                # Colocar nuevo boton
                button5_2.configure(text="Elegir Segundo Piloto")
            except NoInputException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(pilotos_equipo))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 5.2
        def elegir_segundo_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, piloto_2, pilotos_participar, patrocinadores_disponibles, patrocinadores_piloto_1
            try:
                if entry5_2.get()=="":
                    missing_fields = ["Seleccion de Piloto"]
                    raise NoInputException("", missing_fields)
                piloto_2 = pilotos_equipo[int(entry5_2.get()) - 1]
                if piloto_2 == piloto_1:
                    raise RepeatedSelectionException(entry5_2.get())
                pilotos_participar.append(piloto_2)
                # tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos pilotos de tu equipo")
                piloto_2.no_es_elegido()
                # Elegir pilotos contrincantes
                pilotos_disponibles = Piloto.pilotos_disponibles()
                for equipo in participantes:
                    if not (equipo == equipo_elegido):
                        pilotos_equipo = Piloto.pilotos_equipo(equipo, pilotos_disponibles)
                        piloto_contrincante_1 = random.choice(pilotos_equipo)
                        pilotos_participar.append(piloto_contrincante_1)
                        pilotos_equipo.remove(piloto_contrincante_1)
                        piloto_contrincante_2 = random.choice(pilotos_equipo)
                        pilotos_participar.append(piloto_contrincante_2)
                # Patrocinadores y Vehiculos Contrincantes
                patrocinadores_disponibles = Patrocinador.patrocinadoresDisponibles()
                for pilotico in pilotos_participar:
                    pilotico.contratar()
                    if not (pilotico.elegido) and not (pilotico.contrato == equipo_elegido):
                        pilotico.no_es_elegido()
                        Patrocinador.patrocinadorPilotoContrincante(pilotico, patrocinadores_disponibles)
                campeonato_elegido.setListaPilotos(pilotos_participar)

                # Patrocinadores del primer piloto
                patrocinadores_piloto_1 = Patrocinador.patrocinadorPiloto(piloto_1, patrocinadores_disponibles)
                jj = 1
                for patrocinador in patrocinadores_piloto_1:
                    tablaPatrocinadores1.insert(parent='', index=tk.END, values=(jj, patrocinador.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(pilotos_equipo))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 6.1
        def elegir_primer_patrocinador():
            global campeonato_elegido, equipo_elegido, participantes, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1
            try:
                if entry6_1.get()=="":
                    missing_fields = ["Seleccion de Patrocinador"]
                    raise NoInputException("", missing_fields)
                patrocinador_1 = patrocinadores_piloto_1[int(entry6_1.get()) - 1]
                patrocinador_1.pensarNegocio(piloto_1)

                # Patrocinadores segundo piloto
                patrocinadores_piloto_2 = Patrocinador.patrocinadorPiloto(piloto_2, patrocinadores_disponibles)
                jj = 1
                for patrocinador in patrocinadores_piloto_2:
                    tablaPatrocinadores2.insert(parent='', index=tk.END, values=(jj, patrocinador.get_nombre()))
                    jj += 1
                # Quitar label y boton
                entry6_1.destroy()
                button6_1.destroy()
                listbox6_1.destroy()
                # Colocar nuevo boton
                button6_2.configure(text="Elegir Segundo Patrocinador")
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(patrocinadores_piloto_1))
            except ValueError:
                raise IncorrectTypeException("número")


        # Para frame 6.2
        def elegir_segundo_patrocinador():
            global continente, campeonato_elegido, equipo_elegido, participantes, pilotos_participar, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1, patrocinador_2
            try:
                if entry6_2.get()=="":
                    missing_fields = ["Seleccion de Patrocinador"]
                    raise NoInputException("", missing_fields)
                patrocinador_2 = patrocinadores_piloto_2[int(entry6_2.get()) - 1]
                if patrocinador_1 == patrocinador_2:
                    raise RepeatedSelectionException(entry6_2.get())
                patrocinador_2.pensarNegocio(piloto_2)
                # tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos patrocinadores de tu equipo")

                # Campeonato is now unlocked
                campeonato_elegido.setDesbloqueado(True)

                # listbox7_1.insert(0, "Nombre del campeonato: " + campeonato_elegido.getNombre())
                # listbox7_1.insert(1, "Continente: " + continente.value)
                # listbox7_1.insert(2, "Cantidad de carreras:" + str(campeonato_elegido.getCantidadMaxCarreras()))

                tablaCampeonatoResultante.insert(parent='', index=tk.END,
                                                 values=("Nombre del campeonato:", campeonato_elegido.getNombre()))
                tablaCampeonatoResultante.insert(parent='', index=tk.END, values=("Continente: ", continente.value))
                tablaCampeonatoResultante.insert(parent='', index=tk.END, values=(
                    "Cantidad de carreras:", str(campeonato_elegido.getCantidadMaxCarreras())))
                tablaCampeonatoResultante.configure(height=1)

                jj = 1
                for piloto in pilotos_participar:
                    tablaPilotosParticipantes.insert(parent='', index=tk.END, values=(jj, piloto.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame6.grid_remove()
                frame6.grid_forget()
                frame7.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame7.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(patrocinadores_piloto_2))
            except ValueError:
                raise IncorrectTypeException("número")

        def muerte_y_destruccion():
            self.preparar_campeonato(frame_name)
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()
            frame7.destroy()

        # Cambiar al frame de la funcionalidad
        self.change_frame(frame_name)

        # Frame 1: Escoger Continente
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un Continente",
                            "Primero, elige el continente donde quieres que se lleve a cabo el campeonato")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame

        listbox1 = tk.Listbox(frame1)
        # crear Tabla
        tablaContinentes = ttk.Treeview(frame1, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaContinentes.heading('OPCION', text='OPCION')
        tablaContinentes.heading('NOMBRE', text='NOMBRE')
        tablaContinentes.column('OPCION', anchor='c')
        tablaContinentes.column('NOMBRE', anchor='c')
        lista_continentes = [c for c in Continente]
        # agregar inofrmacion
        jj = 1
        for continentico in Continente:
            tablaContinentes.insert(parent='', index=tk.END, values=(jj, continentico.value))
            jj += 1
        # ubicar tabla
        tablaContinentes.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
        entry1 = tk.Entry(frame1)
        entry1.grid(column=0, row=6, padx=20, pady=20)
        entry1.configure(justify="center")
        button1 = tk.Button(frame1, text="Elegir Continente", command=lambda: elegir_continente())
        button1.grid(column=0, row=7, padx=20, pady=20)
        button1.configure(justify="center")
        # Guardando el continente
        continente = None
        # Campeonatos para elegir
        campeonatos_para_elegir = []

        # Frame 2: Escoger Campeonato
        frame2 = FieldFrame(self.frames[frame_name], None, "Elegir tu Campeonato",
                            "De los campeonatos disponibles en el continente elegido,\nelige el que mas te guste")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)

        # crear Tabla
        tablaCampeonatos = ttk.Treeview(frame2, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaCampeonatos.heading('OPCION', text='OPCION')
        tablaCampeonatos.heading('NOMBRE', text='NOMBRE')
        tablaCampeonatos.column('OPCION', width=20, anchor='c')

        tablaCampeonatos.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")

        entry2 = tk.Entry(frame2)
        entry2.grid(column=0, row=6, padx=20, pady=20)
        entry2.configure(justify="center")
        button2 = tk.Button(frame2, text="Elegir Campeonato", command=lambda: elegir_campeonato())
        button2.grid(column=0, row=7, padx=20, pady=20)
        button2.configure(justify="center")
        # Campeonato elegido
        campeonato_elegido = None
        # Equipos disponibles
        equipos_disponibles = []

        # Frame 3: Escoger Equipo
        frame3 = FieldFrame(self.frames[frame_name], None, "Escoger un Equipo",
                            "Estos son los equipos disponibles para correr.\nEscoge uno!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox3 = tk.Listbox(frame3)

        # crear Tabla
        tablaEquipos = ttk.Treeview(frame3, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaEquipos.heading('OPCION', text='OPCION')
        tablaEquipos.heading('NOMBRE', text='NOMBRE')
        tablaEquipos.column('OPCION', width=20, anchor='c')

        tablaEquipos.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")

        entry3 = tk.Entry(frame3)
        entry3.grid(column=0, row=6, padx=20, pady=20)
        entry3.configure(justify="center")
        button3 = tk.Button(frame3, text="Elegir Equipo", command=lambda: elegir_equipo())
        button3.grid(column=0, row=7, padx=20, pady=20)
        button3.configure(justify="center")
        # El equipo que elige el usuario
        equipo_elegido = None
        # Equipos totales
        participantes = []
        # Pilotos del equipo
        pilotos_equipo = []

        # Frame 4: Confirmar Equipo
        frame4 = FieldFrame(self.frames[frame_name], None, "Los Equipos Participantes",
                            "Estos son los equipos que correran en el campeonato")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Comp4onentes del frame
        listbox4 = tk.Listbox(frame4)

        # crear Tabla
        tablaParticipantes = ttk.Treeview(frame4, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaParticipantes.heading('OPCION', text='OPCION')
        tablaParticipantes.heading('NOMBRE', text='NOMBRE')
        tablaParticipantes.column('OPCION', width=20, anchor='c')

        tablaParticipantes.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        button4 = tk.Button(frame4, text="Confirmar Equipos", command=lambda: confirmar_equipos())
        button4.grid(column=0, row=7, padx=20, pady=20)
        button4.configure(justify="center")

        # Frame 5: Escoger Equipo
        frame5 = FieldFrame(self.frames[frame_name], None, "Escoger Pilotos para Correr",
                            "Estos son los pilotos pertenecientes al equipo que elegiste.\nEscoge los dos que mas te llamen la atencion")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox5 = tk.Listbox(frame5)

        # crear Tabla
        tablaPilotos = ttk.Treeview(frame5, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPilotos.heading('OPCION', text='OPCION')
        tablaPilotos.heading('NOMBRE', text='NOMBRE')
        tablaPilotos.column('OPCION', width=20, anchor='c')

        tablaPilotos.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        # Colocar otro label y boton
        entry5_2 = tk.Entry(frame5)
        entry5_2.grid(column=0, row=6, padx=20, pady=20)
        entry5_2.configure(justify="center")
        button5_2 = tk.Button(frame5, command=lambda: elegir_segundo_piloto())
        button5_2.grid(column=0, row=7, padx=20, pady=20)
        button5_2.configure(justify="center")
        entry5_1 = tk.Entry(frame5)
        entry5_1.grid(column=0, row=6, padx=20, pady=20)
        entry5_1.configure(justify="center")
        button5_1 = tk.Button(frame5, text="Elegir Primer Piloto", command=lambda: elegir_primer_piloto())
        button5_1.grid(column=0, row=7, padx=20, pady=20)
        button5_1.configure(justify="center")
        # Primer y Segundo piloto del equipo
        piloto_1 = None
        piloto_2 = None
        # Pilotos Participantes
        pilotos_participar = []
        # Patrocinadores disponibles
        patrconadores_disponibles = []
        patrocinadores_piloto_1 = []
        patrocinadores_piloto_2 = []
        # Ambos patrocinadores del equipo
        patrocinadores_piloto_1 = []
        patrocinadores_piloto_2 = []

        # Frame 6: Escoger Patrocinadores
        frame6 = FieldFrame(self.frames[frame_name], None, "Escoger Patrocinadores del Equipo",
                            "Estos son los patrocinadores dispuestos a hacer negocios.\nEscoge dos para patrocinar a tus pilotos!")
        frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox6_2 = tk.Listbox(frame6)

        # crear Tabla
        tablaPatrocinadores2 = ttk.Treeview(frame6, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPatrocinadores2.heading('OPCION', text='OPCION')
        tablaPatrocinadores2.heading('NOMBRE', text='NOMBRE')
        tablaPatrocinadores2.column('OPCION', width=20, anchor='c')

        tablaPatrocinadores2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")

        listbox6_1 = tk.Listbox(frame6)

        tablaPatrocinadores1 = ttk.Treeview(frame6, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPatrocinadores1.heading('OPCION', text='OPCION')
        tablaPatrocinadores1.heading('NOMBRE', text='NOMBRE')
        tablaPatrocinadores1.column('OPCION', width=20, anchor='c')

        tablaPatrocinadores1.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")

        # Colocar otro label y boton
        entry6_2 = tk.Entry(frame6)
        entry6_2.grid(column=0, row=6, padx=20, pady=20)
        entry6_2.configure(justify="center")
        button6_2 = tk.Button(frame6, command=lambda: elegir_segundo_patrocinador())
        button6_2.grid(column=0, row=7, padx=20, pady=20)
        button6_2.configure(justify="center")
        entry6_1 = tk.Entry(frame6)
        entry6_1.grid(column=0, row=6, padx=20, pady=20)
        entry6_1.configure(justify="center")
        button6_1 = tk.Button(frame6, text="Elegir Primer Patrocinador", command=lambda: elegir_primer_patrocinador())
        button6_1.grid(column=0, row=7, padx=20, pady=20)
        button6_1.configure(justify="center")

        # Frame 7: Mostrar el Campeonato Creado
        frame7 = FieldFrame(self.frames[frame_name], None, "Campeonato Resultante",
                            "Con todo lo que has organizado,\nfinalmente este es el campeonato que has creado")
        frame7.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame

        label7_1 = tk.Label(frame7, text="Los detalles de tu campeonato y pilotos participantes")
        label7_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        inner_frame = tk.Frame(frame7, padx=5, pady=5, bg=None)
        inner_frame.grid(row=4, column=0, columnspan=2, pady=5)
        listbox7_1 = tk.Listbox(frame7)

        # crear Tabla
        tablaCampeonatoResultante = ttk.Treeview(inner_frame, columns=('1', '2'), show="")

        tablaCampeonatoResultante.grid(column=0, row=0, rowspan=4, padx=20, pady=20, sticky="nsew")

        listbox7_2 = tk.Listbox(frame7)

        # crear Tabla
        tablaPilotosParticipantes = ttk.Treeview(inner_frame, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPilotosParticipantes.heading('OPCION', text='POSICION')
        tablaPilotosParticipantes.heading('NOMBRE', text='NOMBRE')
        tablaPilotosParticipantes.column('OPCION', width=50, anchor='c')

        tablaPilotosParticipantes.grid(column=2, row=0, rowspan=3, padx=20, pady=20, sticky="nsew")

        button7 = tk.Button(frame7, text="Volver a Crear un Campeonato", command=lambda: muerte_y_destruccion())
        button7.grid(column=0, row=11, padx=20, pady=20)
        button7.configure(justify="center")

        frame1.tkraise()

    # Funcionalidad 2: Planificar Calendario de Carreras
    def planificar_calendario(self, frame_name):
        global carreras_listo, meses_disponibles, mes_seleccionado, campeonato, mes_elegido, dificultad_elegida
        carreras_listo = 0
        meses_disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

        # Metodos importantes para la funcionalidad
        # Para frame 1
        def elegir_campeonato():
            global campeonato, cantidad_carreras, circuitos_ubicacion, directores_para_elegir, ciudades_disponibles, meses_disponibles, dificultades
            try:
                if entry1.get() == "":
                    missing_fields = ["Seleccion de Campeonato"]
                    raise NoInputException("", missing_fields)
                campeonato = campeonatos_desbloqueados[int(entry1.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato.getNombre() + "\nEl campeonato tiene " + str(campeonato.getCantidadMaxCarreras()) + " carreras, debes planificarlas todas")
                cantidad_carreras = campeonato.getCantidadMaxCarreras()
                circuitos_ubicacion = Circuito.circuitos_ubicacion(campeonato)
                ciudades_disponibles = Ciudad.ciudades_continente(campeonato.getContinente())

                directores_para_elegir = DirectorCarrera.dc_disponibles()
                jj = 1

                for director in directores_para_elegir:
                    tablaDirectoresCarrera.insert(parent='', index=tk.END, values=(jj,director.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(campeonatos_desbloqueados))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 2
        def elegir_director():
            # all variables used
            global directores_para_elegir, director_elegido, circuitos_ubicacion, ciudades_nombres, circuitos_vender, ciudades_disponibles, ciudad_seleccionada, ciudad_elegida, circuitos_para_elegir, meses_disponibles, mes_seleccionado, mes_elegido, dificultades, dificultad_seleccionada, dificultad_elegida
            try:
                if entry2.get() == "":
                    missing_fields = ["Seleccion de Director"]
                    raise NoInputException("", missing_fields)
                director_elegido = directores_para_elegir[int(entry2.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + director_elegido.get_nombre())

                circuitos_vender = Circuito.circuitos_vender(director_elegido, circuitos_ubicacion)

                combobox_meses['values'] = meses_disponibles
                mes_seleccionado.set(meses_disponibles[0])
                # Pasar al siguiente frame
                frame2.grid_remove()
                frame2.grid_forget()
                frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame3.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(directores_para_elegir))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 3
        def elegir_mes(event):
            global mes_seleccionado, meses_disponibles, mes_elegido
            mes_elegido = combobox_meses.get()

        def elegir_dificultad(event):
            global dificultad_seleccionada, dificultad_elegida, dificultades
            dif = combobox_dificultad.get()
            dificultades_dict = {"Principiante": 1, "Avanzado": 2, "Experto": 3}
            dificultad_elegida = dificultades_dict.get(dif)

        def elegir_mes_dificutad():
            global circuitos_para_elegir, mes_elegido, dificultad_elegida, circuitos_vender, ciudades_nombres, ciudades_disponibles
            try:
                if not mes_elegido or not dificultad_elegida:
                    missing_fields = []
                    if mes_elegido == None:
                        missing_fields += ["Seleccion de Mes"]
                    if dificultad_elegida == None:
                        missing_fields += ["Seleccion de Dificultad"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                circuitos_para_elegir = Circuito.circuitos_disponibles(int(mes_elegido), circuitos_vender)
                jj = 1
                for circuito in circuitos_para_elegir:
                    tablaCiudadesDisponibles.insert(parent='', index=tk.END, values=(jj,circuito.get_nombre()))
                    jj += 1

                ciudades_nombres = [ciudad.get_nombre() for ciudad in ciudades_disponibles]
                combobox_ciudad['values'] = ciudades_nombres

                # Pasar al siguiente frame
                frame3.grid_remove()
                frame3.grid_forget()
                frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame4.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, 12)
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 4
        def elegir_ciudad(event):
            global ciudad_seleccionada, ciudad_elegida, ciudades_disponibles
            ciudad_seleccionada = combobox_ciudad.get()
            ciudad_elegida = [ciudad for ciudad in ciudades_disponibles if ciudad.get_nombre() == ciudad_seleccionada][
                0]

        def elegir_circuito():
            global circuito_elegido, circuitos_para_elegir, carrera_creada, ciudad_elegida, dificultad_elegida, dificultad_elegida, circuito_elegido, mes_elegido, director_elegido, campeonato, carreras_listo, meses_disponibles
            try:
                if entry4.get()=="" or not ciudad_elegida:
                    missing_fields = []
                    if entry4.get()=="":
                        missing_fields += ["Seleccion de Circuito"]
                    if dificultad_elegida == None:
                        missing_fields += ["Seleccion de Ciudad"]
                    raise NoInputException("", missing_fields)
                circuito_elegido = circuitos_para_elegir[int(entry4.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
                carrera_creada = Carrera(ciudad_elegida, dificultad_elegida, dificultad_elegida, circuito_elegido,
                                         int(mes_elegido), director_elegido)
                carreras_listo += 1

                campeonato.agregarCarrera(carrera_creada)
                meses_disponibles.remove(mes_elegido)

                # Borrar datos
                combobox_meses.set('')
                combobox_dificultad.set('')
                entry4.delete(0,"end")
                mes_elegido = None
                dificultad_elegida = None

                if carreras_listo == campeonato.getCantidadMaxCarreras():
                    # Pasar al siguiente frame
                    frame4.grid_remove()
                    frame4.grid_forget()
                    frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                    frame5.tkraise()
                else:  # volver al frame 2
                    frame4.grid_remove()
                    frame4.grid_forget()
                    frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                    frame2.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(circuitos_para_elegir))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 5
        def elegir_premios():
            global premio_campeonato, premio_carreras, campeonato
            try:
                if entry5_1.get()=="" or entry5_2.get()=="":
                    missing_fields = []
                    if entry4.get()=="":
                        missing_fields += ["Premio del Campeonato"]
                    if dificultad_elegida == None:
                        missing_fields += ["Premio de las Carreras"]
                    raise NoInputException("", missing_fields)
                premio_campeonato = float(entry5_1.get())
                premio_carreras = float(entry5_2.get())

                campeonato.logisticaPremios(premio_campeonato, premio_carreras)
                campeonato.organizarCarreras()

                jj = 1
                for carrera in campeonato.getListaCarreras():
                    tablaCalendarioCarreras.insert(parent='', index=tk.END, values=(carrera.nombre_circuito ,carrera.getFecha(),carrera.getPremioEfectivo()))
                    jj += 1

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, 2)
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 6
        def muerte_y_destruccion():
            self.planificar_calendario(frame_name)
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()

        # Cambiar al frame de la funcionalidad
        self.change_frame(frame_name)

        # Frame 1: Escoger Campeonato desbloqueados
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un campeonato desbloqueado",
                            "Elige un campeonato disponible para planificar su calendario", "src/img/car.png")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame
        listbox1 = tk.Listbox(frame1)

        # crear Tabla
        tablaCampeonatosDesbloqueados = ttk.Treeview(frame1, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaCampeonatosDesbloqueados.heading('OPCION', text='OPCION')
        tablaCampeonatosDesbloqueados.heading('NOMBRE', text='NOMBRE')
        tablaCampeonatosDesbloqueados.column('OPCION',  anchor='c')

        ii = 1

        campeonatos_desbloqueados = Campeonato.campeonatosDesbloqueados()
        for campeonato in campeonatos_desbloqueados:
            tablaCampeonatosDesbloqueados.insert(parent='', index=tk.END, values=(ii,campeonato.getNombre()))
            ii += 1
        tablaCampeonatosDesbloqueados.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
        entry1 = tk.Entry(frame1)
        entry1.grid(column=0, row=6, padx=20, pady=20)
        entry1.configure(justify="center")
        button1 = tk.Button(frame1, text="Elegir Campeonato", command=lambda: elegir_campeonato())
        button1.grid(column=0, row=7, padx=20, pady=20)
        button1.configure(justify="center")
        # Guardando el campeonato
        campeonato = None
        # circuitos ubicacion
        circuitos_ubicacion = []
        # ciudades disponibles
        ciudades_disponibles = []
        # directores de carera para elegir
        directores_para_elegir = []
        # cantidad de carreras
        cantidad_carreras = 0

        # Dificultades disponibles
        dificultades = ["Principiante", "Avanzado", "Experto"]

        # Frame 2: Escoger Director de Carrera
        frame2 = FieldFrame(self.frames[frame_name], None, "Elegir tu Director de Carrera",
                            "De los directores disponibles, elige el que mas te guste. ")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)

        # crear Tabla
        tablaDirectoresCarrera = ttk.Treeview(frame2, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaDirectoresCarrera.heading('OPCION', text='OPCION')
        tablaDirectoresCarrera.heading('NOMBRE', text='NOMBRE')
        tablaDirectoresCarrera.column('OPCION', anchor='c')

        tablaDirectoresCarrera.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry2 = tk.Entry(frame2)
        entry2.grid(column=0, row=6, padx=20, pady=20)
        entry2.configure(justify="center")
        button2 = tk.Button(frame2, text="Elegir Director", command=lambda: elegir_director())
        button2.grid(column=0, row=7, padx=20, pady=20)
        button2.configure(justify="center")
        # Director elegido
        director_elegido = None
        # circuitos vender
        circuitos_vender = []
        # ciudades disponibles
        ciudades_nombres = []
        # ciudad elegida
        ciudad_seleccionada = None
        ciudad_elegida = None
        # circuitos para elegir
        circuitos_para_elegir = []

        # Frame 3: Escoger Mes, Dificultad
        frame3 = FieldFrame(self.frames[frame_name], None, "Escoger Mes y la Dificultad",
                            "Estos son los meses y dificultades disponibles para la carrera.\nEscoge uno de cada uno!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        mes_seleccionado = tk.StringVar(frame3)
        mes_seleccionado.set(meses_disponibles[0])
        # Create Combobox for month selection
        label33 = tk.Label(frame3, text="Elige el numero del mes en el que quieres reservar el circuito:")
        label33.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        combobox_meses = ttk.Combobox(frame3, values=meses_disponibles)
        combobox_meses.grid(column=0, row=3, padx=20, pady=20)
        combobox_meses.bind("<<ComboboxSelected>>", elegir_mes)
        combobox_meses.configure(justify="center")

        # Create Combobox for difficulty selection
        label34 = tk.Label(frame3, text="Elige la dificultad de la carrera:")
        label34.grid(column=0, row=4, padx=20, pady=20, sticky="nsew")
        dificultad_seleccionada = tk.StringVar(frame3)
        # dificultad_seleccionada.set(dificultades[0])
        combobox_dificultad = ttk.Combobox(frame3, textvariable=dificultad_seleccionada, values=dificultades)
        combobox_dificultad.grid(column=0, row=5, padx=20, pady=20)
        combobox_dificultad.bind("<<ComboboxSelected>>", elegir_dificultad)
        combobox_dificultad.configure(justify="center")

        button3 = tk.Button(frame3, text="Elegir", command=lambda: elegir_mes_dificutad())
        button3.grid(column=0, row=7, padx=20, pady=20)
        button3.configure(justify="center")
        # Dificultad elegida
        dificultad_elegida = None
        # Mes elegido
        mes_elegido = None
        # Ciudad elegida
        ciudad_elegida = None

        # Frame 4: Escoger Circuito y Ciudad
        frame4 = FieldFrame(self.frames[frame_name], None, "Circuitos y Cuidades disponbles",
                            "Estos son los circuitos disponibles el mes que seleccioanste que puede pagar el director de carrera \n y ciudades que estan en el continente")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Comp4onentes del frame

        ciudad_seleccionada = tk.StringVar(frame4)
        ciudad_seleccionada.set(dificultades[0])
        label42 = tk.Label(frame4, text="Estas son las ciudades disponibles en el continente:")
        label42.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        combobox_ciudad = ttk.Combobox(frame4, values=dificultades)
        combobox_ciudad.grid(column=0, row=3, padx=20, pady=20)
        combobox_ciudad.bind("<<ComboboxSelected>>", elegir_ciudad)
        combobox_ciudad.configure(justify="center")

        label41 = tk.Label(frame4, text="Estos son los circuitos disponibles:")
        label41.grid(column=0, row=4, padx=20, pady=20, sticky="nsew")


        listbox4 = tk.Listbox(frame4)

        # crear Tabla
        tablaCiudadesDisponibles = ttk.Treeview(frame4, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaCiudadesDisponibles.heading('OPCION', text='OPCION')
        tablaCiudadesDisponibles.heading('NOMBRE', text='NOMBRE')
        tablaCiudadesDisponibles.column('OPCION', anchor='c')


        tablaCiudadesDisponibles.grid(column=0, row=5, rowspan=2, padx=20, pady=20, sticky="nsew")

        entry4 = tk.Entry(frame4)
        entry4.grid(column=0, row=9, padx=20, pady=20)
        entry4.configure(justify="center")

        button4 = tk.Button(frame4, text="Elegir Circuito", command=lambda: elegir_circuito())
        button4.grid(column=0, row=10, padx=20, pady=20)
        button4.configure(justify="center")

        # Ciudad elegida
        ciudad_elegida = None
        # circuito elegido
        circuito_elegido = None

        # Frame 5: Premios
        frame5 = FieldFrame(self.frames[frame_name], None, "Elige los premios ",
                            "Elige el valor del premio del ganador del campeonato y elige el premio en efectivo destinado para premiar todas las carreras")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label5_1 = tk.Label(frame5, text="Premio para el ganador del campeonato")
        label5_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        entry5_1 = tk.Entry(frame5)
        entry5_1.grid(column=0, row=4, padx=20, pady=20)
        entry5_1.configure(justify="center")

        label5_2 = tk.Label(frame5,
                            text="Premio en efectivo todas las carreras, este se va a usar para premiar todas las carreras de acuerdo a su dificultd")
        label5_2.grid(column=0, row=5, padx=20, pady=20, sticky="nsew")
        entry5_2 = tk.Entry(frame5)
        entry5_2.grid(column=0, row=6, padx=20, pady=20)
        entry5_2.configure(justify="center")

        button5_1 = tk.Button(frame5, text="Elegir", command=lambda: elegir_premios())
        button5_1.grid(column=0, row=7, padx=20, pady=20)
        button5_1.configure(justify="center")

        # Primer y Segundo piloto del equipo
        premio_campeonato = 0
        premio_carreras = 0

        # Frame 6: Mostrar Campeonato Preparado
        frame6 = FieldFrame(self.frames[frame_name], None, "Calendario de Carreras",
                            "Con todo lo que has organizado,\nfinalmente este es el calendario de carreas que has creado")
        frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label6 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
        label6.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")

        listbox6 = tk.Listbox(frame6)

        # crear Tabla
        tablaCalendarioCarreras = ttk.Treeview(frame6, columns=('CARRERA', 'FECHA','PREMIO'), show='headings' )
        # configurar los cabezales
        tablaCalendarioCarreras.heading('CARRERA', text='CARRERA')
        tablaCalendarioCarreras.heading('FECHA', text='FECHA')
        tablaCalendarioCarreras.heading('PREMIO', text='PREMIO')


        tablaCalendarioCarreras.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
        button6 = tk.Button(frame6, text="Volver a Preparar un Campeonato", command=lambda: muerte_y_destruccion())
        button6.grid(column=0, row=11, padx=20, pady=20)
        button6.configure(justify="center")


    # Funcionalidad 3: Tunear el Vehiculo de Carreras
    def personalizar_vehiculo(self, frame_name):
        global pilotos_desbloqueados, piloto_seleccionado, aleron_elegido, neumatico_elegdo, motor_elegido, vehiculo_seleccionado

        def elegir_piloto():
            global piloto_seleccionado, pilotos_desbloqueados, chasis_disponibles
            try:
                if entry1.get() == "":
                    missing_fields = ["Seleccion de Piloto"]
                    raise NoInputException("", missing_fields)
                piloto_seleccionado = pilotos_desbloqueados[int(entry1.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato.getNombre() + "\nEl campeonato tiene " + str(campeonato.getCantidadMaxCarreras()) + " carreras, debes planificarlas todas")
                chasis_disponibles = Chasis.chasis_disponibles(piloto_seleccionado)
                jj = 1

                for chasis in chasis_disponibles:
                    tablaChasis.insert(parent='', index=tk.END, values=(jj,chasis.marca,chasis.modelo,chasis.velocidad,chasis.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(pilotos_desbloqueados))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 2
        def elegir_chasis():
            # all variables used
            global chasis_seleccionado, chasis_disponibles, vehiculo_seleccionado, combinaciones, alerones_disponibles, piloto_seleccionado
            try:
                if entry2.get() == "":
                    missing_fields = ["Seleccion de Chasis"]
                    raise NoInputException("", missing_fields)
                chasis_seleccionado = chasis_disponibles[int(entry2.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + director_elegido.get_nombre())
                vehiculo_seleccionado = chasis_seleccionado.comprar(piloto_seleccionado)
                combinaciones = Pieza.combinaciones(vehiculo_seleccionado)
                alerones_disponibles = Pieza.filterAlerones(combinaciones)

                jj = 1
                for aleron in alerones_disponibles:
                    tablaAleron.insert(parent='', index=tk.END, values=(jj,aleron.nombre,aleron.maniobrabilidadAnadida,aleron.precio,aleron.velocidadAnadida))
                    jj += 1
                # Pasar al siguiente frame

                frame2.grid_remove()
                frame2.grid_forget()
                frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame3.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(chasis_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 3
        def elegir_aleron():
            global aleron_elegido, alerones_disponibles, combinaciones2, vehiculo_seleccionado, combinaciones, neumaticos_disponibles
            try:
                if entry3.get() == "":
                    missing_fields = ["Seleccion de Aleron"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                aleron_elegido = alerones_disponibles[int(entry3.get()) - 1]
                combinaciones2 = Pieza.combinacionesDisponibles(vehiculo_seleccionado, aleron_elegido, combinaciones)
                neumaticos_disponibles = Pieza.filterNeumaticos(combinaciones2)

                jj = 1
                for neumatico in neumaticos_disponibles:
                    tablaNeumaticos.insert(parent='', index=tk.END, values=(jj, neumatico.nombre,neumatico.maniobrabilidadAnadida,neumatico.velocidadAnadida,neumatico.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame3.grid_remove()
                frame3.grid_forget()
                frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame4.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(alerones_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 4
        def elegir_neumatico():
            global neumatico_elegido, neumaticos_disponibles, combinaciones3, vehiculo_seleccionado, combinaciones2, motores_disponibles
            try:
                if entry4.get() == "":
                    missing_fields = ["Seleccion de Neumatico"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                neumatico_elegido = neumaticos_disponibles[int(entry4.get()) - 1]
                combinaciones3 = Pieza.combinacionesDisponibles(vehiculo_seleccionado, neumatico_elegido, combinaciones2)
                motores_disponibles = Pieza.filterMotores(combinaciones3)

                jj = 1
                for neumatico in motores_disponibles:
                    tablaMotor.insert(parent='', index=tk.END, values=(jj,neumatico.nombre,neumatico.maniobrabilidadAnadida,neumatico.velocidadAnadida,neumatico.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame4.grid_remove()
                frame4.grid_forget()
                frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame5.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(neumaticos_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 5
        def elegir_motor():
            global motor_elegido, motores_disponibles, piezas_asignar, aleron_elegido, neumatico_elegido, motor_elegido, precio_total, equipo, descuento, porcentaje_descuento
            try:
                if entry5.get() == "":
                    missing_fields = ["Seleccion de Motor"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                motor_elegido = motores_disponibles[int(entry5.get()) - 1]
                piezas_asignar = [aleron_elegido, neumatico_elegido, motor_elegido]
                vehiculo_seleccionado.setPiezasComprar(piezas_asignar)

                precio_total = Pieza.precioTotal(piezas_asignar, vehiculo_seleccionado)
                equipo = vehiculo_seleccionado.piloto.contrato
                descuento = equipo.descuento(precio_total, vehiculo_seleccionado)



                if descuento:
                    porcentaje_descuento = equipo.calcular_descuento(precio_total, vehiculo_seleccionado)
                    label6_1.config(text="Has impresionado a los proveedores! \n\nTe han hecho un descuento de " + str(
                        round(porcentaje_descuento, 2)) + "% debido a tus habilidades y el dinero del equipo")
                else:
                    label6_1.config(text="No has impresionado a los proveedores, no te han hecho descuento")

                equipo.comprar_piezas(precio_total, vehiculo_seleccionado)

                label6_3.config(text=aleron_elegido.nombre)
                label6_4.config(text=neumatico_elegido.nombre)
                label6_5.config(text=motor_elegido.nombre)

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(motores_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 6
        def muerte_y_destruccion():
            self.personalizar_vehiculo(frame_name)
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()

        # Cambiar al frame de la funcionalidad
        self.change_frame(frame_name)

        # Frame 1: Escoger Piloto desbloqueados
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un piloto desbloqueado",
                            "Elige un piloto para personalizar su vehiculo de carreras", "src/img/car.png")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame
        listbox1 = tk.Listbox(frame1)
        tablaPilotoDesbloqueado = ttk.Treeview(frame1, columns=('OPCION', 'NOMBRE', 'CONTRATO'), show='headings')
        # configurar los cabezales
        tablaPilotoDesbloqueado.heading('OPCION', text='OPCION')
        tablaPilotoDesbloqueado.heading('NOMBRE', text='NOMBRE')
        tablaPilotoDesbloqueado.heading('CONTRATO', text='EQUIPO')

        ii = 1

        pilotos_desbloqueados = Piloto.pilotos_desbloqueados()

        for piloto in pilotos_desbloqueados:
            tablaPilotoDesbloqueado.insert(parent='', index=tk.END,
                                           values=(ii, piloto.nombre, piloto.contrato.nombre))
            ii += 1

        tablaPilotoDesbloqueado.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
        entry1 = tk.Entry(frame1)
        entry1.grid(column=0, row=6, padx=20, pady=20)
        entry1.configure(justify="center")
        button1 = tk.Button(frame1, text="Elegir Piloto", command=lambda: elegir_piloto())
        button1.grid(column=0, row=7, padx=20, pady=20)
        button1.configure(justify="center")
        # Variables
        vehiculo_seleccionado = None
        piloto_seleccionado = None
        chasis_disponibless = []

        # Frame 2: Elegr Chasis
        frame2 = FieldFrame(self.frames[frame_name], None, "Elige un chasis",
                            "Estos son los chasis disponibles para tu piloto de acuerdo a su presupuesto. Elige uno!")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)

        # crear Tabla
        tablaChasis = ttk.Treeview(frame2, columns=('OPCION', 'NOMBRE','MODELO','VELOCIDAD','PRECIO'), show='headings')
        # configurar los cabezales
        tablaChasis.heading('OPCION', text='OPCION')
        tablaChasis.heading('NOMBRE', text='MARCA')
        tablaChasis.heading('MODELO', text='MODELO')
        tablaChasis.heading('VELOCIDAD', text='VELOCIDAD')
        tablaChasis.heading('PRECIO', text='PRECIO')
        tablaChasis.column('OPCION', anchor='c')


        tablaChasis.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry2 = tk.Entry(frame2)
        entry2.grid(column=0, row=6, padx=20, pady=20)
        entry2.configure(justify="center")
        button2 = tk.Button(frame2, text="Elegir Chasis", command=lambda: elegir_chasis())
        button2.grid(column=0, row=7, padx=20, pady=20)
        button2.configure(justify="center")
        # Variables
        chasis_seleccionado = None
        alerones_disponibles = []
        combinaciones = []

        # Frame 3: Elegr Aleron
        frame3 = FieldFrame(self.frames[frame_name], None, "Elegir Aleron",
                            "Estos son los alerones disponibles para tu piloto de acuerdo a su presupuesto y de la marca de tu chasis. Elige uno!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox3 = tk.Listbox(frame3)


        tablaAleron = ttk.Treeview(frame3, columns=('OPCION', 'NOMBRE','MODELO','VELOCIDAD','PRECIO'), show='headings')
        # configurar los cabezales
        tablaAleron.heading('OPCION', text='OPCION')
        tablaAleron.heading('NOMBRE', text='MARCA')
        tablaAleron.heading('MODELO', text='MANIOBRABOLIDAD')
        tablaAleron.heading('VELOCIDAD', text='VELOCIDAD')
        tablaAleron.heading('PRECIO', text='PRECIO')
        tablaAleron.column('OPCION', anchor='c')

        tablaAleron.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry3 = tk.Entry(frame3)
        entry3.grid(column=0, row=6, padx=20, pady=20)
        entry3.configure(justify="center")
        button3 = tk.Button(frame3, text="Elegir Aleron", command=lambda: elegir_aleron())
        button3.grid(column=0, row=7, padx=20, pady=20)
        button3.configure(justify="center")
        # Variables
        aleron_elegido = None
        combinaciones2 = []
        neumaticos_disponibles = []

        # Frame 4: Escoger Neumatico
        frame4 = FieldFrame(self.frames[frame_name], None, "Elegir Neumatico",
                            "Estos son los neumaticos disponibles para tu piloto de acuerdo a su presupuesto y de la marca de tu chasis. Elige uno!")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox4 = tk.Listbox(frame4)

        tablaNeumaticos = ttk.Treeview(frame4, columns=('OPCION', 'NOMBRE','MODELO','VELOCIDAD','PRECIO'), show='headings')
        # configurar los cabezales
        tablaNeumaticos.heading('OPCION', text='OPCION')
        tablaNeumaticos.heading('NOMBRE', text='MARCA')
        tablaNeumaticos.heading('MODELO', text='MANIOBRABILIDAD')
        tablaNeumaticos.heading('VELOCIDAD', text='VELOCIDAD')
        tablaNeumaticos.heading('PRECIO', text='PRECIO')
        tablaNeumaticos.column('OPCION', anchor='c')

        tablaNeumaticos.grid(column=0, row=3, rowspan=2, padx=20, pady=20, sticky="nsew")

        entry4 = tk.Entry(frame4)
        entry4.grid(column=0, row=6, padx=20, pady=20)
        entry4.configure(justify="center")

        button4 = tk.Button(frame4, text="Elegir Neumatico", command=lambda: elegir_neumatico())
        button4.grid(column=0, row=7, padx=20, pady=20)
        button4.configure(justify="center")

        # Variables
        neumatico_elegido = None
        motores_disponibles = []
        combinaciones3 = []

        # Frame 5: Elegir Motor
        frame5 = FieldFrame(self.frames[frame_name], None, "Elegir Motor",
                            "Estos son los motores disponibles para tu piloto de acuerdo a su presupuesto y de la marca de tu chasis. Elige uno!")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox5 = tk.Listbox(frame5)


        tablaMotor = ttk.Treeview(frame5, columns=('OPCION', 'NOMBRE','MODELO','VELOCIDAD','PRECIO'), show='headings')
        # configurar los cabezales
        tablaMotor.heading('OPCION', text='OPCION')
        tablaMotor.heading('NOMBRE', text='MARCA')
        tablaMotor.heading('MODELO', text='MANIOBRABILIDAD')
        tablaMotor.heading('VELOCIDAD', text='VELOCIDAD')
        tablaMotor.heading('PRECIO', text='PRECIO')
        tablaMotor.column('OPCION', anchor='c')

        tablaMotor.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry5 = tk.Entry(frame5)
        entry5.grid(column=0, row=6, padx=20, pady=20)
        entry5.configure(justify="center")

        button5 = tk.Button(frame5, text="Elegir Motor", command=lambda: elegir_motor())
        button5.grid(column=0, row=7, padx=20, pady=20)
        button5.configure(justify="center")

        # Variables
        motor_elegido = None

        # Frame 6: Descuento
        frame6 = FieldFrame(self.frames[frame_name], None, "Vehiculo Personalizado",
                            "Con todo lo que has organizado,\nfinalmente este es el vehiculo que has creado")
        frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label6 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
        label6.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        label6_1 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
        label6_1.grid(column=0, row=4, padx=20, pady=20, sticky="nsew")

        label6_2 = tk.Label(frame6, text="Tu equipoo ha comprado:")
        label6_2.grid(column=0, row=6, padx=20, pady=20, sticky="nsew")
        label6_3 = tk.Label(frame6, text="aleron:")
        label6_3.grid(column=0, row=7, padx=20, pady=20, sticky="nsew")
        label6_4 = tk.Label(frame6, text="neumatico:")
        label6_4.grid(column=0, row=8, padx=20, pady=20, sticky="nsew")
        label6_5 = tk.Label(frame6, text="motor:")
        label6_5.grid(column=0, row=9, padx=20, pady=20, sticky="nsew")

        button6 = tk.Button(frame6, text="Volver a Personalizar el Vehiculo de Carreras ",
                            command=lambda: muerte_y_destruccion())
        button6.grid(column=0, row=11, padx=20, pady=20)
        button6.configure(justify="center")

    # Funcionalidad 4: Forjar una Alianza con el Maestro de Carreras
    def forjar_amistad(self, frame_name):
        global image4
        # Funciones para el funcionamiento de la funcionalidad
        def elegir_piloto():
            global piloto_seleccionado, pilotos_desbloqueados, campeonato_piloto, maestros_disponibles
            try:
                if entry1.get() == "":
                    missing_fields = ["Seleccion de Piloto"]
                    raise NoInputException("", missing_fields)
                pilotos_desbloqueados = Piloto.pilotos_desbloqueados()
                piloto_seleccionado = pilotos_desbloqueados[int(entry1.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato.getNombre() + "\nEl campeonato tiene " + str(campeonato.getCantidadMaxCarreras()) + " carreras, debes planificarlas todas")
                campeonato_piloto = Campeonato.campeonatoPiloto(piloto_seleccionado)
                maestros_disponibles = Campeonato.directoresCarrera(campeonato_piloto)
                jj = 1
                for maestro in maestros_disponibles:
                    tablaDirectores.insert(parent='', index=tk.END, values=(jj,maestro.get_nombre()))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(pilotos_desbloqueados))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 2
        def elegir_maestro_de_carreras():
            global piloto_seleccionado, campeonato_piloto, maestros_disponibles, maestro_elegido
            try:
                if entry2.get() == "":
                    missing_fields = ["Seleccion de Director de Carrera"]
                    raise NoInputException("", missing_fields)
                maestro_elegido = maestros_disponibles[int(entry2.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + director_elegido.get_nombre())
                # Pasar al siguiente frame
                label3.configure(text="(Tu equipo cuenta con ${})".format(piloto_seleccionado.contrato.get_plata()))

                frame2.grid_remove()
                frame2.grid_forget()
                frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame3.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(maestros_disponibles))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 3
        def sobornar():
            global piloto_seleccionado, campeonato_piloto, maestro_elegido, plata_ofrecida, carta_seleccionada, selecciones
            try:
                if entry3.get() == "":
                    missing_fields = ["Incentivo Monetario"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                plata_ofrecida = int(entry3.get())
                carta_seleccionada = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
                selecciones = []

                # Pasar al siguiente frame
                frame3.grid_remove()
                frame3.grid_forget()
                frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame4.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, 2)
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 4
        def elegir_destino(button_text):
            global piloto_seleccionado, campeonato_piloto, maestro_elegido, plata_ofrecida, selecciones, carta_seleccionada, plata_ganada, pilotos_maldecir
            try:
                if int(button_text) in selecciones:
                    raise RepeatedSelectionException(button_text)
                if len(selecciones) < 2:
                    entry4.configure(state="normal")
                    entry4.insert("end",button_text + ", ")
                    entry4.configure(state="disabled")
                    selecciones.append(int(button_text))

                else:
                    entry4.configure(state="normal")
                    entry4.insert("end",button_text)
                    selecciones.append(int(button_text))
                    entry4.configure(state="disabled")
                    tk.messagebox.showinfo("Eleccion realizada", "Has escogido las cartas: " + entry4.get())
                    if carta_seleccionada in selecciones:
                        plata_ganada = plata_ofrecida * 3
                    else:
                        plata_ganada = plata_ofrecida * 0.75

                    # Lista de pilotos desfavorecidos
                    pilotos_maldecir = maestro_elegido.pilotos_desfavorecidos(plata_ganada, piloto_seleccionado, campeonato_piloto)

                    jj = 1
                    for pilotico in pilotos_maldecir:
                        tablaPilotos.insert(parent='', index=tk.END, values=(jj,pilotico.get_nombre()))
                        jj += 1

                    # Borrar para volver hacer de nuevo
                    entry4.delete(0,"end")
                    selecciones.clear()

                    # Pasar al siguiente frame
                    frame4.grid_remove()
                    frame4.grid_forget()
                    frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                    frame5.tkraise()
            except RepeatedSelectionException:
                pass

        # Para frame 5
        def maldecir_piloto():
            global piloto_seleccionado, campeonato_piloto, maestro_elegido, plata_ganada, pilotos_maldecir, piloto_maldito, vehiculos_participar
            try:
                if entry5.get() == "":
                    missing_fields = ["'¿Acaso no quieres maldecir a nadie?'"]
                    raise NoInputException("", missing_fields)
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                piloto_maldito = pilotos_maldecir[int(entry5.get()) - 1]

                sanciones_before = piloto_seleccionado.getSanciones()
                vehiculos_participar = piloto_maldito.maldecir_piloto(plata_ganada,piloto_seleccionado,maestro_elegido,campeonato_piloto)
                for vehiculo in vehiculos_participar:
                    vehiculo.actualizar_velocidad_actual()

                if sanciones_before < piloto_seleccionado.getSanciones():
                    tk.messagebox.showinfo("Oh no!",
                                           "No has podido maldecir al piloto, al parecer tu dinero no ha sido lo suficientemente ~motivante~")
                else:
                    tk.messagebox.showinfo("MUAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJA",
                                           "El Maestro de Carrera te sonrie, y predice que el piloto y su vehiculo sufriran de una 'mala fortuna'")

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()
            except NoInputException:
                pass
            except RepeatedSelectionException:
                pass
            except IndexError:
                raise OutOfBoundsException(1, len(pilotos_maldecir))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 6
        def manipular_carrera(eleccion):
            global piloto_seleccionado, campeonato_piloto, maestro_elegido, plata_ganada, pilotos_maldecir, piloto_maldito, vehiculos_participar, vehiculos_malditos
            try:
                for vehiculo in vehiculos_participar:
                    vehiculo.actualizar_velocidad_actual()

                if eleccion == "Posiciones":
                    vehiculos_malditos = VehiculoCarrera.manipular_vehiculos(vehiculos_participar,pilotos_maldecir,piloto_maldito,piloto_seleccionado,plata_ganada,maestro_elegido,True)
                    label7.configure(text="El Maestro de Carrera te avisa que 'puede que comiences mas adelante, y los otros, mas atras'...")
                elif eleccion == "Componentes":
                    vehiculos_malditos = VehiculoCarrera.manipular_vehiculos(vehiculos_participar,pilotos_maldecir,piloto_maldito,piloto_seleccionado,plata_ganada,maestro_elegido,False)
                    label7.configure(text="El Maestro de Carrera te muestra un misterioso liquido que dice que le va a hacer bien a tu Vehiculo de Carrera.\n"
                                          + "Mientras, en su otra mano, sostiene un liquido diferente, y sugiere que quizas ese no le haga bien a los otros Vehiculos...")
                # Pasar al siguiente frame

                jj=1
                for vehiculo in vehiculos_malditos:
                    tablaMalditos.insert(parent='', index=tk.END, values=(jj,vehiculo.piloto.get_nombre(),vehiculo.velocidadTuneao,vehiculo.getDistanciaInicial()))
                    jj+=1

                frame6.grid_remove()
                frame6.grid_forget()
                frame7.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame7.tkraise()
            except AttributeError:
                raise NullPointerException("Vehiculo de Carrera")

        # Para frame 7
        def muerte_y_destruccion():
            self.forjar_amistad(frame_name)
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()
            frame7.destroy()

        # Cambiar al frame de la funcionalidad
        self.change_frame(frame_name)

        # Frame 1: Escoger Piloto desbloqueado
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un piloto desbloqueado",
                            "Elige un piloto para personificarlo mientras habla con un Director de Carreras",
                            "src/img/car.png")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame
        listbox1 = tk.Listbox(frame1)

        # crear Tabla
        tablaPilotos = ttk.Treeview(frame1, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPilotos.heading('OPCION', text='OPCION')
        tablaPilotos.heading('NOMBRE', text='NOMBRE')
        tablaPilotos.column('OPCION', anchor='c')

        ii = 1

        #Pilotos desbloqueados
        pilotos_desbloqueados = Piloto.pilotos_desbloqueados()

        for piloto in pilotos_desbloqueados:
            tablaPilotos.insert(parent='', index=tk.END, values=(ii,piloto.nombre,piloto.contrato.nombre))
            ii += 1

        tablaPilotos.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
        entry1 = tk.Entry(frame1)
        entry1.grid(column=0, row=6, padx=20, pady=20)
        entry1.configure(justify="center")
        button1 = tk.Button(frame1, text="Elegir Piloto", command=lambda: elegir_piloto())
        button1.grid(column=0, row=7, padx=20, pady=20)
        button1.configure(justify="center")
        # Important Variables
        piloto_seleccionado = None
        campeonato_piloto = None

        maestros_disponibles = []

        # Frame 2: Elegir Maestro de Carreras
        frame2 = FieldFrame(self.frames[frame_name], None, "Elige un Maestro de Carreras",
                            "En la distancia, puedes observar a los distintos Directores de Carrera que dirigen en el campeonato,\n"
                            "Elije alguno para acercarte")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)

        # crear Tabla
        tablaDirectores = ttk.Treeview(frame2, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaDirectores.heading('OPCION', text='OPCION')
        tablaDirectores.heading('NOMBRE', text='NOMBRE')
        tablaDirectores.column('OPCION', anchor='c')

        tablaDirectores.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry2 = tk.Entry(frame2)
        entry2.grid(column=0, row=6, padx=20, pady=20)
        entry2.configure(justify="center")
        button2 = tk.Button(frame2, text="Elegir Maestro de Carreras", command=lambda: elegir_maestro_de_carreras())
        button2.grid(column=0, row=7, padx=20, pady=20)
        button2.configure(justify="center")
        # Variables
        maestro_de_carrera = None


        # Frame 3: Soborno Inicial al Maestro de Carreras
        frame3 = FieldFrame(self.frames[frame_name], None, "Problemas economicos :,(",
                            "Mientras hablabas con el director de carrera" + ", te cuenta:\n" +
                            "'Hay ciertos problemas economicos que me preocupan'\nQuizas darle un 'incentivo' pueda lograr captar su atencion.~")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label3 = tk.Label(frame3)
        label3.grid(column=0, row=4, padx=20, pady=20)
        label3.configure(justify="center")
        entry3 = tk.Entry(frame3)
        entry3.grid(column=0, row=5, padx=20, pady=20)
        entry3.configure(justify="center")
        button3 = tk.Button(frame3, text="Dar Incentivo", command=lambda: sobornar())
        button3.grid(column=0, row=6, padx=20, pady=20)
        button3.configure(justify="center")

        # Variables
        plata_ofrecida = 0
        carta_seleccionada = None



        # Frame 4: Apuesta Ilegal con el Maestro de Carreras
        frame4 = FieldFrame(self.frames[frame_name], None, "Elige tu Destino",
                            "La 'conversacion' sigue de manera normal, y repentinamente, el Director te pide ir a 'un lugar mas tranquilo'\n" +
                            "...\n" +
                            "Llegan a una sala oscura, y no es sino parpadear, y enfrente tuyo encuentras un manojo de cartas organizado\n" +
                            "'Vamos, escoge tres cartas'\n"
                            "'La primera es tu pasado, la segunda, tu presente, y la ultima tu futuro'")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        # Cartas
        image_path = "src/img/card_deck.png"
        img = Image.open(image_path)
        img_width, img_height = 500, 500
        resized_image = img.resize((550, 502))

        image4 = ImageTk.PhotoImage(resized_image)

        extra_frame_4 = tk.Frame(frame4, width=500, height=500)
        extra_frame_4.grid(row=4, column=0, rowspan=3, padx=20, pady=20, sticky="nsew")

        img_label = tk.Label(extra_frame_4, image=image4)
        img_label.grid(row=0, column=0)

        # Set padding for the buttons within the extra_frame_4
        button_padding_x = 25
        button_padding_y = 88

        # Calculate the dimensions for evenly placing square buttons with padding
        button_width = 50
        button_height = 50

        # Create 21 buttons with numbers from 1 to 21 and place them evenly on top of the image with padding
        for i in range(1, 22):
            row = (i - 1) // 7
            col = (i - 1) % 7
            x_coordinate = col * (button_width + button_padding_x) + button_padding_x
            y_coordinate = row * (button_height + button_padding_y) + button_padding_y
            button = tk.Button(extra_frame_4, text=str(i), command=lambda j=i: elegir_destino(str(j)))
            button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_height)

        entry4 = tk.Entry(extra_frame_4)
        entry4.place(relx=0.8, rely=0.1, anchor=tk.CENTER)
        entry4.configure(justify="center", state="disabled", disabledbackground="black", disabledforeground="white")

        # Variables
        selecciones = []
        plata_ganada = 0
        pilotos_maldecir = []

        # Frame 5: Elegir Piloto para Castigar
        frame5 = FieldFrame(self.frames[frame_name], None, "Maldecir a un contrincante",
                            "El Maestro de Carreras saca una lista, y poco a poco, va tachando nombres.\n" +
                            "Pronto, te la entrega, parece ser que quiere que escojas alguien de ella")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox5 = tk.Listbox(frame5)

        # crear Tabla
        tablaPilotosMaldecir = ttk.Treeview(frame5, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPilotosMaldecir.heading('OPCION', text='OPCION')
        tablaPilotosMaldecir.heading('NOMBRE', text='NOMBRE')
        tablaPilotosMaldecir.column('OPCION', anchor='c')

        tablaPilotosMaldecir.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry5 = tk.Entry(frame5)
        entry5.grid(column=0, row=6, padx=20, pady=20)
        entry5.configure(justify="center")

        button5 = tk.Button(frame5, text="Marcar para maldecir", command=lambda: maldecir_piloto())
        button5.grid(column=0, row=7, padx=20, pady=20)
        button5.configure(justify="center")

        # Variables
        piloto_maldito = None
        vehiculos_participar = []

        # Frame 6: Elegir como manipular la carrera
        frame6 = FieldFrame(self.frames[frame_name], None, "Manipular la carrera",
                            "Luego de devolverle la lista, el Maestro de Carrera te da una ultima eleccion")
        frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        button6_1 = tk.Button(frame6, text="Manipular Posiciones", command=lambda: manipular_carrera("Posiciones"))
        button6_1.grid(column=0, row=7, padx=20, pady=20, sticky="w")
        button6_1.configure(justify="center")
        button6_2 = tk.Button(frame6, text="Manipular Vehiculos", command=lambda: manipular_carrera("Componentes"))
        button6_2.grid(column=0, row=7, padx=20, pady=20, sticky="e")
        button6_2.configure(justify="center")

        # Variables
        piloto_maldito = None
        vehiculos_malditos = []

        # Frame 7: Muajajajajaja, has hecho algo ilegal >:)
        frame7 = FieldFrame(self.frames[frame_name], None, "El trato se ha pactado",
                            "'Fue un placer jugar contigo'\n" +
                            "Se despide de ti el Maestro de Carrera, mientras te quedas ahi, en el medio de la calle...\n" +
                            "Vale esto realmente la pena?")
        frame7.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label7 = tk.Label(frame7)
        label7.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        listbox7 = tk.Listbox(frame7)


        tablaMalditos = ttk.Treeview(frame7, columns=('OPCION', 'NOMBRE','MODELO','VELOCIDAD'), show='headings')
        # configurar los cabezales
        tablaMalditos.heading('OPCION', text='OPCION')
        tablaMalditos.heading('NOMBRE', text='MARCA')
        tablaMalditos.heading('MODELO', text='VELOCIDAD')
        tablaMalditos.heading('VELOCIDAD', text='DISTANCIA')

        tablaMalditos.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")


        button7 = tk.Button(frame7, text="Mas... maldad?",
                            command=lambda: muerte_y_destruccion())
        button7.grid(column=0, row=11, padx=20, pady=20)
        button7.configure(justify="center")

    # Funcionalidad 5: GOTTA GO FAST
    def simulacion_campeonato(self, frame_name):
        global img3_0, img3_1, equipo_est_actual
        # Metodos importantes para la funcionalidad
        # Para frame 1
        def elegir_campeonato():
            global campeonato, carreras, cant_carreras, piloto_elegido, vehiculo_elegido
            try:
                if entry1.get() == "":
                    missing_fields = ["Seleccion de Campeonato"]
                    raise NoInputException("", missing_fields)
                campeonato = campeonatos_desbloqueados[int(entry1.get()) - 1]

                carreras = campeonato.getListaCarreras()
                cant_carreras = 0
                piloto_elegido = campeonato.pilotoCampeonato()
                vehiculo_elegido = VehiculoCarrera.vehiculos_piloto(piloto_elegido)[0]
                label2.configure(text="El piloto elegido para el campeonato es: " + piloto_elegido.get_nombre())
                jj = 1

                for carrerita in carreras:
                    tablaCarreras.insert(parent='', index=tk.END, values=(jj,carrerita.getNombreCircuito()))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            except TypeError:
                raise NullPointerException("Vehiculo de Carrera")
            except AttributeError:
                raise NullPointerException("Vehiculo de Carrera")
            except IndexError:
                raise OutOfBoundsException(1, len(campeonatos_desbloqueados))
            except ValueError:
                raise IncorrectTypeException("número")

        # Para frame 2
        def comenzar_carreras():
            global campeonato, carreras, cant_carreras, carrera_actual, piloto_elegido, vehiculo_elegido
            carrera_actual = carreras[0]
            director_carrera = carrera_actual.getDirectorCarrera()
            if director_carrera.posicionesCorruptas:
                carrera_actual.setPosiciones(director_carrera.posicionesCorruptas)
            else:
                lista_posiciones = []
                for vehiculo in VehiculoCarrera.listaVehiculos:
                    if vehiculo.piloto in campeonato.getListaPilotos():
                        lista_posiciones.append(vehiculo)
                carrera_actual.setPosiciones(lista_posiciones)

            for vehiculito in carrera_actual.getPosiciones():
                vehiculito.setTerminado(False)
                vehiculito.setMorido(False)
                vehiculito.setDistanciaRecorrida(vehiculito.getDistanciaInicial())
                vehiculito.setTiempo(0)
                vehiculito.setVelocidadCircumstancias(0)
                vehiculito.actualizar_velocidad_actual()

            # RESETEAR LAS COSAS SI NO ES LA PRIMERA CARRERA
            if cant_carreras > 0:
                vehiculo_elegido.llenar_gasolina()
                label3_1.configure(
                    text="Distancia Recorrida:".format(str(vehiculo_elegido.getDistanciaRecorrida()),
                                                             str(carrera_actual.getDistancia())))
                label3_2.configure(text="Tiempo Transcurrido: {} s.".format(str(vehiculo_elegido.getTiempo())))
                label3_3.configure(text="Gasolina del vehiculo: {}/100".format(str(vehiculo_elegido.getGasolina())))
                listbox3.delete(0,"end")
                button3_0.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


            # Pasar al siguiente frame
            frame2.grid_remove()
            frame2.grid_forget()
            frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame3.tkraise()

        # Para frame 3
        def correr_carrera():
            global campeonato, carreras, cant_carreras, carrera_actual, piloto_elegido, vehiculo_elegido
            button3_0.place_forget()
            terminar = False
            if not carrera_actual.actualizarTerminado():
                cant_iteraciones = random.randint(2,8)
                for i in range(cant_iteraciones):
                    carrera_actual.actualizarPosiciones()
                    if not vehiculo_elegido.morido and not vehiculo_elegido.terminado:
                        carrera_actual.actualizarGasolina(piloto_elegido,carrera_actual)
                if (vehiculo_elegido.isMorido()):
                    messagebox.showerror("¡¡¡KABOOM!!!","Te has chocado! La carrera finalizara automaticamente.")
                    while True:
                        if carrera_actual.actualizarTerminado():
                            break
                        carrera_actual.actualizarPosiciones()
                    terminar = True
                    img_label.place_forget()
                    img_label_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                    button3.place(relx=0.8, rely=0.8)
                elif (vehiculo_elegido.isTerminado()):
                    messagebox.showinfo("KACHOW!","Has terminado! La carrera finalizara pronto.")
                    while True:
                        if carrera_actual.actualizarTerminado():
                            break
                        carrera_actual.actualizarPosiciones()
                    terminar = True
                    button3.place(relx=0.8, rely=0.8)
                if not terminar:
                    # TODO: ACTUALIZAR STATS DEL CARRO
                    label3_1.configure(text="Distancia Recorrida: {}/{}".format(str(vehiculo_elegido.getDistanciaRecorrida()), str(carrera_actual.getDistancia())))
                    label3_2.configure(text="Tiempo Transcurrido: {} s.".format(str(vehiculo_elegido.getTiempo())))
                    label3_3.configure(text="Gasolina del vehiculo: {}/100".format(str(vehiculo_elegido.getGasolina())))
                    # TODO: ACTUALIZAR POSICIONES EN LA TABLA

                    tablaPociciones = ttk.Treeview(mini_frame3, columns=('OPCION', 'NOMBRE', 'VELOCIDAD'),
                                                   show='headings')
                    # configurar los cabezales
                    tablaPociciones.heading('OPCION', text='POSICION')
                    tablaPociciones.heading('NOMBRE', text='PILOTO')
                    tablaPociciones.heading('VELOCIDAD', text='VELOCIDAD')
                    tablaPociciones.column('OPCION', anchor='c')

                    tablaPociciones.place(relx=0.33, rely=0.77, anchor=tk.CENTER)
                    jj = 1
                    for vehiculo in carrera_actual.posiciones:
                        if vehiculo != vehiculo_elegido:
                            vehiculo.decision_piloto_random()
                        if not vehiculo.isTerminado():
                            tablaPociciones.insert(parent='', index=tk.END, values=(jj,vehiculo.piloto.get_nombre(),vehiculo.getDistanciaRecorrida()))
                        else:
                            tablaPociciones.insert(parent='', index=tk.END, values=(jj,vehiculo.piloto.get_nombre(),"TERMINADO"))
                        jj+=1
                    # OPCIONES

                    lista_opciones = carrera_actual.actualizarOpciones()
                    if lista_opciones[0]:
                        button3_1.place(relx=0.8, rely=0.3)
                    if lista_opciones[1]:
                        button3_2.place(relx=0.8, rely=0.4)
                    if lista_opciones[2]:
                        button3_3.place(relx=0.8, rely=0.5)
                    if lista_opciones[3]:
                        button3_4.place(relx=0.8, rely=0.6)
                    if lista_opciones[4]:
                        button3_5.place(relx=0.8, rely=0.7)
                    if vehiculo_elegido.velocidadActual < 200:
                        button3_6.place(relx=0.8, rely=0.8)

        def aprovechar_drs():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            vehiculo_elegido.aprovechar_drs()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        def frenar():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            vehiculo_elegido.frenar()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        def hacer_maniobra():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            vehiculo_elegido.hacer_maniobra()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        def defender_la_posicion():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            vehiculo_elegido.defender()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        def derrapar():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            vehiculo_elegido.derrapar()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        def pit_stop():
            global vehiculo_elegido
            button3_1.place_forget()
            button3_2.place_forget()
            button3_3.place_forget()
            button3_4.place_forget()
            button3_5.place_forget()
            button3_6.place_forget()
            button3_6_1.place(relx=0.8, rely=0.4)
            button3_6_2.place(relx=0.8, rely=0.5)
            button3_6_3.place(relx=0.8, rely=0.6)
        def rellenar_gasolina():
            global vehiculo_elegido
            button3_6_1.place_forget()
            vehiculo_elegido.llenar_gasolina()
        def reparar():
            global vehiculo_elegido
            button3_6_2.place_forget()
            vehiculo_elegido.reparar_vehiculo()

        def salir_pit_stop():
            button3_6_1.place_forget()
            button3_6_2.place_forget()
            button3_6_3.place_forget()
            button3_0.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

        def premiacion_carrera():
            global campeonato, carreras, cant_carreras, carrera_actual, piloto_elegido, vehiculo_elegido
            img_label_2.place_forget()
            button3.place_forget()
            img_label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

            jj=1
            carrera_actual.organizarVehiculosTiempos()
            for vehiculo in carrera_actual.terminados:
                tablaPremiacion.insert(parent='', index=tk.END, values=(jj,vehiculo.piloto.get_nombre(),vehiculo.tiempo))
                jj+=1
            Equipo.puntuarEquipos(carrera_actual.getTerminados(),carrera_actual.getPremioEfectivo(),campeonato)


            # Pasar al siguiente frame
            frame3.grid_remove()
            frame3.grid_forget()
            frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame4.tkraise()

        # Para frame 4
        def continuar():
            global campeonato, carreras, cant_carreras, carrera_actual, piloto_elegido, vehiculo_elegido, equipo_est_actual
            # Pasar al siguiente frame dependiendo de lo que este pasando
            if cant_carreras <= len(carreras)-1:
                frame4.grid_remove()
                frame4.grid_forget()
                carreras.pop(0)

                cant_carreras +=1

                # Eliminar las cosas de las listbox
                listbox2.delete(0)
                listbox4.delete(0,"end")

                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()
            else:
                # TODO: ORGANIZAR LOS CAMPEONES
                equipos_organizados = Equipo.organizar_equipos_puntos(campeonato)
                campeonato.premiarCampeones(equipos_organizados)

                jj = 1
                for equipo in campeonato._listaEquipos:
                    tablaEquiposPuntos.insert(parent='', index=tk.END, values=(jj,equipo.nombre,equipo.puntos))
                    jj+=1

                campeonato._jugado = True
                equipo_ganador = campeonato._listaEquipos[0]
                piloto_ganador_1 = None
                piloto_ganador_2 = None
                for piloto in campeonato._listaPilotos:
                    if piloto.contrato == equipo_ganador and piloto_ganador_1 is not None:
                        piloto_ganador_2 = piloto
                    elif piloto.contrato == equipo_ganador:
                        piloto_ganador_1 = piloto
                label5_2.configure(text="El equipo ganador ha sido: {}".format(equipo_ganador.get_nombre()))
                label5_3.configure(text="Los pilotos ganadores han sido: {} y {}".format(piloto_ganador_1.get_nombre(),piloto_ganador_2.get_nombre()))
                label5_4.configure(text=("Actualmente viendo las estadisticas del equipo: {}\n".format(equipo_ganador.get_nombre()) +
                                                  "El equipo obtuvo {} puntos.\n".format(str(equipo_ganador.puntos)) +
                                                  "Y los pilotos {} y {} obtuvieron los tiempos:").format(piloto_ganador_1.get_nombre(),piloto_ganador_2.get_nombre()))

                jj=1
                for tiempo in piloto_ganador_1.tiemposCarreras:
                    listbox5_1.insert(jj,"{}. | {} s".format(str(jj),str(tiempo)))
                    jj+=1

                jj=1
                for tiempo in piloto_ganador_2.tiemposCarreras:
                    listbox5_2.insert(jj,"{}. | {} s".format(str(jj),str(tiempo)))
                    jj+=1

                frame4.grid_remove()
                frame4.grid_forget()
                frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame5.tkraise()


        # Para frame 6
        def estadisticas_siguiente_equipo():
            global campeonato, equipo_est_actual
            equipo_est_actual = equipo_est_actual
            if equipo_est_actual == len(campeonato._listaEquipos)-1:
                equipo_est_actual = 0
            else:
                equipo_est_actual += 1
            equipo_est = campeonato._listaEquipos[equipo_est_actual]
            piloto_1 = None
            piloto_2 = None
            for piloto in campeonato._listaPilotos:
                if piloto.contrato == equipo_est and piloto_1 is not None:
                    piloto_2 = piloto
                elif piloto.contrato == equipo_est:
                    piloto_1 = piloto
            label5_4.configure(
                text=("Actualmente viendo las estadisticas del equipo: {}\n".format(equipo_est.get_nombre()) +
                      "El equipo obtuvo {} puntos.\n".format(str(equipo_est.puntos)) +
                      "Y los pilotos {} y {} obtuvieron los tiempos:").format(piloto_1.get_nombre(),
                                                                              piloto_2.get_nombre()))
            listbox5_1.delete(0,"end")
            jj = 1
            for tiempo in piloto_1.tiemposCarreras:
                listbox5_1.insert(jj, "{}. | {} s".format(str(jj), str(tiempo)))
                jj += 1
            listbox5_2.delete(0,"end")
            jj = 1
            for tiempo in piloto_2.tiemposCarreras:
                listbox5_2.insert(jj, "{}. | {} s".format(str(jj), str(tiempo)))
                jj += 1

        def muerte_y_destruccion():
            self.simulacion_campeonato(frame_name)
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()

        # Cambiar al frame de la funcionalidad
        self.change_frame(frame_name)

        # Frame 1: Escoger Campeonato desbloqueado
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un campeonato desbloqueado",
                            "¡Elige un campeonato disponible para comenzar a divertirse!", "src/img/car.png")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame
        listbox1 = tk.Listbox(frame1)

        # crear Tabla
        tablaCampeonato = ttk.Treeview(frame1, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaCampeonato.heading('OPCION', text='OPCION')
        tablaCampeonato.heading('NOMBRE', text='NOMBRE')
        tablaCampeonato.column('OPCION', anchor='c')

        ii = 1

        campeonatos_desbloqueados = Campeonato.campeonatosDesbloqueados()
        for campeonato in campeonatos_desbloqueados:
            tablaCampeonato.insert(parent='', index=tk.END, values=(ii,campeonato.getNombre()))
            ii += 1
        tablaCampeonato.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
        entry1 = tk.Entry(frame1)
        entry1.grid(column=0, row=6, padx=20, pady=20)
        entry1.configure(justify="center")
        button1 = tk.Button(frame1, text="Elegir Campeonato", command=lambda: elegir_campeonato())
        button1.grid(column=0, row=7, padx=20, pady=20)
        button1.configure(justify="center")
        # Guardando el campeonato
        campeonato = None
        # Carreras
        carreras = []
        # Cantidad de carreras
        cant_carreras = 0
        # Piloto elegido
        piloto_elegido = None
        # Carro elegido
        vehiculo_elegido = None

        # Frame 2: Comenzar Carreras
        frame2 = FieldFrame(self.frames[frame_name], None, "Carreras en el campeonato",
                            "Este será el orden en el que se correran las carreras del campeonato.")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)

        # crear Tabla
        tablaCarreras = ttk.Treeview(frame2, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaCarreras.heading('OPCION', text='OPCION')
        tablaCarreras.heading('NOMBRE', text='NOMBRE')
        tablaCarreras.column('OPCION', anchor='c')

        tablaCarreras.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        label2 = tk.Label(frame2)
        label2.grid(column=0, row=7, padx=20, pady=20)
        button2 = tk.Button(frame2, text="¡Comenzar a manejar!", command=lambda: comenzar_carreras())
        button2.grid(column=0, row=8, padx=20, pady=20)
        button2.configure(justify="center")
        # Carrera Actual
        carrera_actual = None

        # Frame 3: Frame de la carrera
        frame3 = FieldFrame(self.frames[frame_name], None, "Simulando la carrera...",
                            "¡Pon atencion! \n"
                            "¡Tienes que tomar las decisiones correctas para poder ganar!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        mini_frame3 = tk.Frame(frame3,height=int(720*0.75)+7, width=int(1280*0.75)+7)
        mini_frame3.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        mini_frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=2)
        action_font = ("Segoe UI",9,"italic")
        # Background Image
        image_path = "src/img/car_view.gif"
        img3_0 = Image.open(image_path)
        resized_frames = []
        for frame in ImageSequence.Iterator(img3_0):
            resized_frame = frame.resize((int(1280*0.75),int(720*0.75)))
            resized_frames.append(ImageTk.PhotoImage(resized_frame))
        img_label = tk.Label(mini_frame3)
        img_label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        def update_label_1(frame_idx=0):
            img_label.configure(image=resized_frames[frame_idx])
            frame3.after(50, update_label_1, (frame_idx+1) % len(resized_frames))
        update_label_1()
        # Crashed Image
        image_path_2 = "src/img/explosion.gif"
        img3_1 = Image.open(image_path_2)
        resized_frames_2 = []
        for frame in ImageSequence.Iterator(img3_1):
            resized_frame = frame.resize((int(1280*0.75),int(720*0.75)))
            resized_frames_2.append(ImageTk.PhotoImage(resized_frame))
        img_label_2 = tk.Label(mini_frame3)
        def update_label_2(frame_idx=0):
            img_label_2.configure(image=resized_frames_2[frame_idx])
            frame3.after(50, update_label_2, (frame_idx+1) % len(resized_frames_2))
        update_label_2()

        # TODO: TABLA DE LAS POSICIONES
        listbox3 = tk.Listbox(mini_frame3,width=50, height=15)

        # crear Tabla
        tablaPociciones = ttk.Treeview(mini_frame3, columns=('OPCION', 'NOMBRE','VELOCIDAD'), show='headings')
        tablaPociciones.tag_configure('TreeviewFont', font=('Segoe UI', 9))
        # configurar los cabezales
        tablaPociciones.heading('OPCION', text='POSICION')
        tablaPociciones.heading('NOMBRE', text='PILOTO')
        tablaPociciones.heading('VELOCIDAD', text='VELOCIDAD')
        tablaPociciones.column('OPCION', anchor='c')


        tablaPociciones.place(relx=0.33, rely=0.77, anchor=tk.CENTER)
        # TODO: TABLA CONFIGURACION DEL VEHICULO
        label3_1 = tk.Label(mini_frame3,text="Distancia Recorrida: {}/{}".format("0","0"), width=46)
        label3_1.place(relx=0.19,rely=0.1, anchor=tk.CENTER)
        label3_1.configure(justify="center")
        label3_2 = tk.Label(mini_frame3,text="Tiempo Transcurrido: {} s.".format("0"), width=46)
        label3_2.place(relx=0.19,rely=0.2, anchor=tk.CENTER)
        label3_2.configure(justify="center")
        label3_3 = tk.Label(mini_frame3,text="Gasolina del vehiculo: {}/100".format("100"), width=46)
        label3_3.place(relx=0.19,rely=0.3, anchor=tk.CENTER)
        label3_3.configure(justify="center")
        # Boton para correr la carrera
        button3_0 = tk.Button(mini_frame3, text="¡CORRER!", command=lambda: correr_carrera())
        button3_0.place(relx=0.5,rely=0.4, anchor=tk.CENTER)
        button3_0.configure(justify="center")
        # Botones para las selecciones de las acciones
        button3_1 = tk.Button(mini_frame3, text="Aprovechar DRS (FIAOO)", command=lambda: aprovechar_drs())
        button3_1.configure(justify="center")
        button3_2 = tk.Button(mini_frame3, text="Frenar!", command=lambda: frenar())
        button3_2.configure(justify="center")
        button3_3 = tk.Button(mini_frame3, text="Hacer Maniobra (KACHOW)", command=lambda: hacer_maniobra())
        button3_3.configure(justify="center")
        button3_4 = tk.Button(mini_frame3, text="Defender la posicion", command=lambda: defender_la_posicion())
        button3_4.configure(justify="center")
        button3_5 = tk.Button(mini_frame3, text="Derrapar", command=lambda: derrapar())
        button3_5.configure(justify="center")
        button3_6 = tk.Button(mini_frame3, text="Entrar a la Pit Stop", command=lambda: pit_stop())
        button3_6.configure(justify="center")
        button3_6_1 = tk.Button(mini_frame3, text="Rellenar la Gasolina", command=lambda: rellenar_gasolina())
        button3_6_1.configure(justify="center")
        button3_6_2 = tk.Button(mini_frame3, text="Reparar el Vehiculo", command=lambda: reparar())
        button3_6_2.configure(justify="center")
        button3_6_3 = tk.Button(mini_frame3, text="Salir de la Pit Stop", command=lambda: salir_pit_stop())
        button3_6_3.configure(justify="center")

        # Boton para terminar la carrera
        button3 = tk.Button(mini_frame3, text="Terminar la carrera", command=lambda: premiacion_carrera())
        button3.configure(justify="center")


        # Frame 4: Frame de la premiacion de la carrera
        frame4 = FieldFrame(self.frames[frame_name], None, "Premiacion de la Carrera",
                            "Estos son los resultados de la carrera!")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label4 = tk.Label(frame4, text="Posiciones en la carrera")
        label4.grid(column=0, row=4, padx=20, pady=20, sticky="nsew")
        listbox4 = tk.Listbox(frame4)

        # crear Tabla
        tablaPremiacion = ttk.Treeview(frame4, columns=('OPCION', 'NOMBRE','PUNTOS'), show='headings')
        # configurar los cabezales
        tablaPremiacion.heading('OPCION', text='POSICION')
        tablaPremiacion.heading('NOMBRE', text='NOMBRE')
        tablaPremiacion.heading('PUNTOS', text='TIEMPO')
        tablaPremiacion.column('OPCION', anchor='c')

        tablaPremiacion.grid(column=0, row=5, rowspan=2, padx=20, pady=20, sticky="nsew")

        # Boton para continuar
        button4 = tk.Button(frame4, text="Continuar", command=lambda: continuar())
        button4.grid(column=0, row=10, padx=20, pady=20)
        button4.configure(justify="center")

        # Frame 5: Frame de la premiacion del campeonato
        frame5 = FieldFrame(self.frames[frame_name], None, "El campeonato ha terminado",
                            "A continuacion, los resultados en general de los equipos participantes", "src/img/podio.png")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label5_1 = tk.Label(frame5, text="Asi quedaron los equipos en orden de puntaje")
        label5_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        listbox5 = tk.Listbox(frame5)

        # crear Tabla
        tablaEquiposPuntos = ttk.Treeview(frame5, columns=('OPCION', 'NOMBRE','PUNTOS'), show='headings')
        # configurar los cabezales
        tablaEquiposPuntos.heading('OPCION', text='POSICION')
        tablaEquiposPuntos.heading('NOMBRE', text='EQUIPO')
        tablaEquiposPuntos.heading('PUNTOS', text='PUNTOS')
        tablaEquiposPuntos.column('OPCION', anchor='c')

        tablaEquiposPuntos.grid(column=0, row=4, rowspan=2, padx=20, pady=20, sticky="nsew")
        tablaEquiposPuntos.configure(height=5)

        label5_2 = tk.Label(frame5, text="El equipo ganador ha sido: ")
        label5_2.grid(column=0, row=6, padx=20, pady=20, sticky="nsew")
        label5_3 = tk.Label(frame5, text="Los pilotos ganadores han sido:")
        label5_3.grid(column=0, row=7, padx=20, pady=20, sticky="nsew")
        label5_4 = tk.Label(frame5, text=("Actualmente viendo las estadisticas del equipo: \n" +
                                          "El equipo puntuo  puntos.\n" +
                                          "Y los pilotos  y  obtuvieron los tiempos:"))
        label5_4.grid(column=0, row=8, padx=20, pady=20, sticky="nsew")
        listbox5_1 = tk.Listbox(frame5,width=50)
        listbox5_1.grid(column=0, row=9, rowspan=2, padx=20, pady=20, sticky="nsw")
        listbox5_1.configure(height=2)
        listbox5_2 = tk.Listbox(frame5,width=50)
        listbox5_2.grid(column=0, row=9, rowspan=2, padx=20, pady=20, sticky="nse")
        listbox5_2.configure(height=2)

        button5_1 = tk.Button(frame5, text="Ver estadisticas de otro equipo", command=lambda: estadisticas_siguiente_equipo())
        button5_1.grid(column=0, row=10, padx=20, pady=20)
        button5_1.configure(justify="center")
        button5_2 = tk.Button(frame5, text="Correr Otro Campeonato", command=lambda: muerte_y_destruccion())
        button5_2.grid(column=0, row=11, padx=20, pady=20)
        button5_2.configure(justify="center")
        #Variables
        equipo_est_actual = 0

    def acerca_de(self, frame_name):
        self.change_frame(frame_name)
        frame_acerca = FieldFrame(self.frames[frame_name], None, "¡Bienvenido al Proyecto FIA!")
        frame_acerca.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame_acerca.grid(column=0, row=0, padx=20, pady=20, sticky="nsew")
        global logo_path, logo_img1
        # add image
        logo_path = "src/img/gp_racing.png"
        img = Image.open(logo_path)
        #resized_image = img.resize((500, 500))

        # Load the logo image
        logo_img1 = ImageTk.PhotoImage(img)

        # Create a label for the logo and place it in the right top corner
        logo_label1 = tk.Label(frame_acerca, image=logo_img1)
        logo_label1.grid(row=1, column=0, sticky="nsew")
        logo_label1.configure(justify="center")


        mensaje_final = """
                 Nuestra aplicación te permite gestionar todo lo relacionado con un emocionante campeonato de carreras automovilísticas. Desde planificar las carreras hasta personalizar los vehículos, todo está al alcance de tus manos.
                 Todo está diseñado de forma sencilla y modular para que disfrutes de una experiencia completa y emocionante.

                 ¡Prepárate para la emoción de la pista!

                 Autores:
                 Santiago Lopez Ayala, David Toro Arboleda, Juan Andrés Jiménez Vélez, Mariana Valencia Cubillos y Samuel Mira Álvarez
                 """

        # Etiqueta para mostrar el texto informativo

        info_label3 = tk.Label(frame_acerca, text=mensaje_final, justify="center", wraplength=500, padx=20, pady=20)
        info_label3.grid(column=0, row=2, sticky="nsew")

        frame_acerca.tkraise()


if __name__ == "__main__":
    def pasar_a_ventana_principal():
        ventana.iconify()
        root.deiconify()
        root.tkraise()
        app = MenuApp(root)

    # Initial Root
    root = tk.Tk()
    root.minsize()
    root.iconbitmap("src/img/f1.ico")
    root.title("GP Racing: The one and only!")
    # Ventana Inicial
    ventana = tk.Toplevel(root, height=800, width=1280)
    ventana.iconbitmap("src/img/f1.ico")

    frameP1 = tk.Frame(ventana)
    frameP1.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="e")

    frameP2 = tk.Frame(ventana)
    frameP2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="w")

    frameP3 = tk.Frame(frameP1)
    frameP3.place(relx=0.5, rely=0.3, relwidth=0.98, relheight=0.29, anchor="s")

    frameP4 = tk.Frame(frameP1)
    frameP4.place(relx=0.5, rely=0.31, relwidth=0.98, relheight=0.68, anchor="n")

    frameP5 = tk.Frame(frameP2)
    frameP5.place(relx=0.5, rely=0.3, relwidth=0.98, relheight=0.29, anchor="s")

    frameP6 = tk.Frame(frameP2)
    frameP6.place(relx=0.5, rely=0.31, relwidth=0.98, relheight=0.68, anchor="n")

    def salirApp():
        root.destroy()

    def descripcion():
        messagebox.showinfo("Descripcion de la aplicacion",
                            "El " "Proyecto de la Fédération Internationale de l'Automobile" "es una aplicación desarrollada bajo el paradigma de Programación Orientada a Objetos que se enfoca en la gestión integral de un campeonato de carreras automovilísticas.")

    # menu
    menu = tk.Menu(ventana, tearoff=0)
    ventana.config(menu=menu)

    menuInicio = tk.Menu(menu)
    menu.add_cascade(label="Inicio", menu=menuInicio)

    menuInicio.add_command(label="Salir", command=salirApp)
    menuInicio.add_command(label="Descripción", command=descripcion)

    mensaje = ("¡Bienvenido a nuestro simulador de carreras de la\n Fédération Internationale de l'Automobile,\n"
               "donde podrás experimentar la emoción de competir en carreras \n"
               "de Fórmula 1 como nunca antes!")

    # mesaje bienvenida
    mensaje1 = tk.Label(frameP3,
                        text=mensaje,
                        justify=tk.CENTER,
                        font=("Helvetica", 16),
                        relief="solid",
                        bd=2.5
                        )
    mensaje1.place(relx=0.5, rely=0.5, relwidth=0.98, relheight=0.98, anchor="center")

    # Fotos proyecto
    fotoCarro0 = Image.open("src/fotosInicio//carrof1.png")
    fotoCarro = ImageTk.PhotoImage(fotoCarro0)
    fotoBanderas0 = Image.open("src/fotosInicio//banderas.png")
    fotoBanderas = ImageTk.PhotoImage(fotoBanderas0)
    fotoLogo0 = Image.open("src/fotosInicio//logo.png")
    fotoLogo = ImageTk.PhotoImage(fotoLogo0)
    fotoPiloto0 = Image.open("src/fotosInicio//piloto.png")
    fotoPiloto = ImageTk.PhotoImage(fotoPiloto0)
    fotoCircuito0 = Image.open("src/fotosInicio//circuito.png")
    fotoCircuito = ImageTk.PhotoImage(fotoCircuito0)
    # Fotos Mariana
    fotoMariana1p = Image.open("src/fotosInicio//Mariana1.png")
    fotoMariana1 = ImageTk.PhotoImage(fotoMariana1p)
    fotoMariana2p = Image.open("src/fotosInicio//Mariana2.png")
    fotoMariana2 = ImageTk.PhotoImage(fotoMariana2p)
    fotoMariana3p = Image.open("src/fotosInicio//Mariana3.png")
    fotoMariana3 = ImageTk.PhotoImage(fotoMariana3p)
    fotoMariana4p = Image.open("src/fotosInicio//Mariana4.png")
    fotoMariana4 = ImageTk.PhotoImage(fotoMariana4p)
    # Fotos David
    fotoDavid1p = Image.open("src/fotosInicio//David1.png")
    fotoDavid1 = ImageTk.PhotoImage(fotoDavid1p)
    fotoDavid2p = Image.open("src/fotosInicio//David2.png")
    fotoDavid2 = ImageTk.PhotoImage(fotoDavid2p)
    fotoDavid3p = Image.open("src/fotosInicio//David3.png")
    fotoDavid3 = ImageTk.PhotoImage(fotoDavid3p)
    fotoDavid4p = Image.open("src/fotosInicio//David4.png")
    fotoDavid4 = ImageTk.PhotoImage(fotoDavid4p)
    # Fotos Samuel
    fotoSamuel1p = Image.open("src/fotosInicio//Samuel1.png")
    fotoSamuel1 = ImageTk.PhotoImage(fotoSamuel1p)
    fotoSamuel2p = Image.open("src/fotosInicio//Samuel2.png")
    fotoSamuel2 = ImageTk.PhotoImage(fotoSamuel2p)
    fotoSamuel3p = Image.open("src/fotosInicio//Samuel3.png")
    fotoSamuel3 = ImageTk.PhotoImage(fotoSamuel3p)
    fotoSamuel4p = Image.open("src/fotosInicio//Samuel4.png")
    fotoSamuel4 = ImageTk.PhotoImage(fotoSamuel4p)
    # Fotos Juan
    fotoJuan1p = Image.open("src/fotosInicio//Juan1.png")
    fotoJuan1 = ImageTk.PhotoImage(fotoJuan1p)
    fotoJuan2p = Image.open("src/fotosInicio//Juan2.png")
    fotoJuan2 = ImageTk.PhotoImage(fotoJuan2p)
    fotoJuan3p = Image.open("src/fotosInicio//Juan3.png")
    fotoJuan3 = ImageTk.PhotoImage(fotoJuan3p)
    fotoJuan4p = Image.open("src/fotosInicio//Juan4.png")
    fotoJuan4 = ImageTk.PhotoImage(fotoJuan4p)
    # Fotos Santiago
    fotoSantiago1p = Image.open("src/fotosInicio//Santiago1.png")
    fotoSantiago1 = ImageTk.PhotoImage(fotoSantiago1p)
    fotoSantiago2p = Image.open("src/fotosInicio//Santiago2.png")
    fotoSantiago2 = ImageTk.PhotoImage(fotoSantiago2p)
    fotoSantiago3p = Image.open("src/fotosInicio//Santiago3.png")
    fotoSantiago3 = ImageTk.PhotoImage(fotoSantiago3p)
    fotoSantiago4p = Image.open("src/fotosInicio//Santiago4.png")
    fotoSantiago4 = ImageTk.PhotoImage(fotoSantiago4p)
    def cambiarFoto(event):
        if BotonP4["text"] == "1":
            BotonP4.config(image=fotoBanderas, text="2")
        elif BotonP4["text"] == "2":
            BotonP4.config(image=fotoCarro, text="3")
        elif BotonP4["text"] == "3":
            BotonP4.config(image=fotoPiloto, text="4")
        elif BotonP4["text"] == "4":
            BotonP4.config(image=fotoLogo, text="5")
        elif BotonP4["text"] == "5":
            BotonP4.config(image=fotoCircuito, text="1")

    # imagenes cambiantes con acercar el mouse
    BotonP4 = tk.Button(frameP4, image=fotoLogo, text="1", relief="solid", bd=2.5)
    BotonP4.bind("<Enter>", cambiarFoto)
    BotonP4.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.75, anchor="s")
    # boton ingresar
    botonIngresar = tk.Button(frameP4, text="Ingresar",  width=30, height=2, relief="solid", bd=2.,
                              command=pasar_a_ventana_principal)
    botonIngresar.pack(side='bottom', pady=10)

    # hojas de vida
    david = """Soy David Toro, estudiante de Ingeniería de Sistemas, con conocimientos en lenguajes como Python y Java. Apasionado por el desarrollo web y de videojuegos, estoy enfocado en ampliar mi experiencia en estas áreas.
        \nclic para cambiar"""

    david = '\n'.join(david[i:i + 81] for i in range(0, len(david), 81))

    samuel = """Soy Samuel Mira,"I love you, this world, and everyone in it!" Programador novicio, prospecto en Java y Python. Estudiante de Ciencias de la Computación, siempre maravillado con todo lo que hay por descubrir. Todos los dias son buenos dias para aprender
        """

    samuel = '\n'.join(samuel[i:i + 81] for i in range(0, len(samuel), 81))

    mariana = """Soy Mariana Valencia Cubillos, estudiante de Ciencias de la Computación y apasionada por la inteligencia artificial. Con amplia experiencia en programación (Java, Python, Scala, HTML) y enfoque en Power Apps, Power BI y SSIS como freelancer, mi interés se centra en la automatización de procesos. Encuentro satisfacción en la innovación y la aplicación creativa de la tecnología para resolver problemas cotidianos.
        \nclic para cambiar"""

    # Agregar salto de línea cada 81 caracteres
    mariana = '\n'.join(mariana[i:i + 81] for i in range(0, len(mariana), 81))

    santiago = """Soy Santiago López Ayala, estudiante de Ingeniería de Sistemas, entusiasta de la tecnología y todo lo relacionado con el espacio. Poseo conocimientos sólidos en Java y Python, y estoy comprometido con el constante aprendizaje y desarrollo en el campo de la ingeniería informática.
        \nclic para cambiar"""

    santiago = '\n'.join(santiago[i:i + 81] for i in range(0, len(santiago), 81))

    juan = """Soy Juan Andrés Jiménez Vélez, estudiante de Ingeniería de Sistemas e Informática y técnico en electricidad y electrónica. Tengo conocimientos de programación con los lenguajes Python y Java, y del desarrollo de aplicaciones web con Angular. Mi experiencia abarca el trabajo en instalaciones eléctricas residenciales. Me considero una persona con una gran capacidad para aprender y resolver problemas de manera eficiente.
        \nclic para cambiar"""

    juan = '\n'.join(juan[i:i + 81] for i in range(0, len(juan), 81))

    def cambiarTexto():
        if hojasDeVida["text"] == david:
            inner_frame_David.pack_forget()
            inner_frame_Samuel.pack()
            hojasDeVida.config(text=samuel)

        elif hojasDeVida["text"] == samuel:
            inner_frame_Samuel.pack_forget()
            inner_frame_Mariana.pack()
            hojasDeVida.config(text=mariana)

        elif hojasDeVida["text"] == mariana:
            inner_frame_Mariana.pack_forget()
            inner_frame_Juan.pack()

            hojasDeVida.config(text=juan)

        elif hojasDeVida["text"] == juan:

            inner_frame_Juan.pack_forget()
            inner_frame_Santiago.pack()

            hojasDeVida.config(text=santiago)

        elif hojasDeVida["text"] == santiago:
            inner_frame_Santiago.pack_forget()
            inner_frame_David.pack()

            hojasDeVida.config(text=david)

    # hojas de vida
    tituloHojasDeVida = tk.Label(frameP5, text="Breve hoja de vida", relief="solid", bd=2.5)
    tituloHojasDeVida.place(relx=0.5, rely=0.21, relwidth=0.98, relheight=0.2, anchor="s")

    hojasDeVida = tk.Button(frameP5, width=50, height=2, text=david, relief="solid", bd=2.5,
                            command=cambiarTexto)
    hojasDeVida.place(relx=0.5, rely=0.1899, relwidth=0.98, relheight=0.8, anchor="n")

    # fotos

    # crear los arreglos de las fotos 4x4
    def create_inner_frame_David(parent_frame):

        inner_frame = tk.Frame(parent_frame)

        imagenes = [fotoDavid1, fotoDavid2, fotoDavid3, fotoDavid4]

        for i in range(2):
            for j in range(2):
                imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230,
                                        relief="solid",
                                        bd=2.5)
                imagen_label.grid(row=i, column=j, padx=5, pady=5)

        return inner_frame

    def create_inner_frame_Mariana(parent_frame):
        inner_frame = tk.Frame(parent_frame)

        imagenes = [fotoMariana1, fotoMariana2, fotoMariana4, fotoMariana3]

        for i in range(2):
            for j in range(2):
                imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230,
                                        relief="solid",
                                        bd=2.5)
                imagen_label.grid(row=i, column=j, padx=5, pady=5)

        return inner_frame

    def create_inner_frame_Samuel(parent_frame):
        inner_frame = tk.Frame(parent_frame)

        imagenes = [fotoSamuel1, fotoSamuel2, fotoSamuel3, fotoSamuel4]

        for i in range(2):
            for j in range(2):
                imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230,
                                        relief="solid",
                                        bd=2.5)
                imagen_label.grid(row=i, column=j, padx=5, pady=5)

        return inner_frame

    def create_inner_frame_Juan(parent_frame):
        inner_frame = tk.Frame(parent_frame)

        imagenes = [fotoJuan1, fotoJuan2, fotoJuan3, fotoJuan4]

        for i in range(2):
            for j in range(2):
                imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230,
                                        relief="solid",
                                        bd=2.5)
                imagen_label.grid(row=i, column=j, padx=5, pady=5)

        return inner_frame

    def create_inner_frame_Santiago(parent_frame):
        inner_frame = tk.Frame(parent_frame)

        imagenes = [fotoSantiago1, fotoSantiago2, fotoSantiago3, fotoSantiago4]

        for i in range(2):
            for j in range(2):
                imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230,
                                        relief="solid",
                                        bd=2.5)
                imagen_label.grid(row=i, column=j, padx=5, pady=5)

        return inner_frame

    # crea Frames con fotos
    inner_frame_David = create_inner_frame_David(frameP6)
    # ubicar primer Frame
    inner_frame_David.pack()

    inner_frame_Mariana = create_inner_frame_Mariana(frameP6)
    inner_frame_Samuel = create_inner_frame_Samuel(frameP6)
    inner_frame_Juan = create_inner_frame_Juan(frameP6)
    inner_frame_Santiago = create_inner_frame_Santiago(frameP6)

    # DATA MANAGEMENT
    # Serializado.crearObjetos()
    Deserializado.deserializar()

    # Window States
    root.iconify()
    ventana.deiconify()
    ventana.tkraise()

    sk.set_theme("dark")
    root.mainloop()
