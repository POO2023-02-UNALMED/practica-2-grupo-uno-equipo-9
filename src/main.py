import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import sv_ttk as sk

# Imports de las clases
from src.base_datos.Serializado import Serializado
from src.gestor_aplicacion.campeonato.DirectorCarrera import DirectorCarrera
from src.gestor_aplicacion.campeonato.Campeonato import Campeonato
from src.gestor_aplicacion.campeonato.Equipo import Equipo
from src.gestor_aplicacion.paddock.Circuito import Circuito
from src.gestor_aplicacion.paddock.Patrocinador import Patrocinador
from src.gestor_aplicacion.paddock.Piloto import Piloto
from src.gestor_aplicacion.ubicaciones.Ciudad import Ciudad
from src.gestor_aplicacion.ubicaciones.Continente import Continente


class FieldFrame(tk.Frame):

    def __init__(self, parent, color, nombre_proceso="", descripcion="", logo_path="random"):
        super().__init__(parent)
        self.nombre_proceso = nombre_proceso
        self.descripcion = descripcion

        # Create labels for the title and description
        title_label = tk.Label(self, text=nombre_proceso, font=("Helvetica", 16), anchor="center")
        description_label = tk.Label(self, text=descripcion, anchor="center")

        # Use grid to make labels span the same width as the window
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        title_label.configure(justify="center")
        description_label.grid(row=1, column=0, padx=20, sticky="nsew")
        description_label.configure(justify="center")

        if logo_path == "random":
            img_paths = ["img/car.png", "img/polo.png", "img/chaqueta-de-carreras.png", "img/f1.png"]
            logo_path = random.choice(img_paths)

        self.img = (Image.open(logo_path))
        resized_image = self.img.resize((40, 40))
        # Load the logo image
        self.logo_img = ImageTk.PhotoImage(resized_image)

        # Create a label for the logo and place it in the right top corner
        logo_label = tk.Label(self, image=self.logo_img)
        logo_label.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="ne")

        # Adjust column weights to allocate space for the new column
        self.grid_rowconfigure("all", weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)  # Adjust the weight for the new column
        # adjust the height of the new column to small
        self.grid_columnconfigure(2, weight=1)


class MenuApp:
    def __init__(self, root):
        self.menu_bar = None
        self.root = root
        self.root.title("Menu App")
        # self.root.geometry("1200x600")
        sk.set_theme("dark")
        self.frames = {}  # Dictionary to store frames

        self.create_frames()
        self.create_menu()

    def create_frames(self):
        self.frames["app"] = FieldFrame(self.root, None, "Aplicacion", "Bienvenido a la aplicacion de GP Racing")
        self.frames["preparar_campeonato"] = FieldFrame(self.root, None, "Preparar Un Nuevo Campeonato",
                                                        "Aqui puedes preparar un nuevo campeonato desde cero!")
        self.frames["planificar_calendario"] = FieldFrame(self.root, None, "Planificar Calendario de Carreras",
                                                          "Aqui puedes planificar el calendario de carreras de un campeonato")
        self.frames["personalizar_vehiculo"] = FieldFrame(self.root, None, "Personalizar Vehiculo de Carreras")
        self.frames["forjar_alianza"] = FieldFrame(self.root, None, "Forjar Alianza con el Maestro de Carreras")
        self.frames["gp_racing"] = FieldFrame(self.root, None, "GP Racing")
        self.frames["acerca_de"] = FieldFrame(self.root, None)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # sub menu archivo
        archivo = tk.Menu(self.menu_bar, tearoff=0)
        archivo.add_command(label='Aplicacion', command=lambda: self.change_frame('app'))
        archivo.add_command(label='Salir', command=self.root.quit)
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
        ayuda.add_command(label='Acerca de', command=lambda: self.change_frame('acerca_de'))
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
            continente = Ciudad.convertir_continente(int(entry1.get()))
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el continente " + continente.value)

            campeonatos_disponibles = Campeonato.campeonatosDisponibles()
            campeonatos_continente = Campeonato.campeonatosContinente(continente)
            campeonatos_para_elegir = []
            for campeonato in campeonatos_disponibles:
                if campeonato in campeonatos_continente:
                    campeonatos_para_elegir.append(campeonato)
            jj = 1

            for campeonatico in campeonatos_para_elegir:
                listbox2.insert(jj, str(jj) + " | " + campeonatico.getNombre())
                jj += 1

            # Pasar al siguiente frame
            frame1.grid_remove()
            frame1.grid_forget()
            frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame2.tkraise()

        # Para frame 2
        def elegir_campeonato():
            global continente, campeonato_elegido, campeonatos_para_elegir, equipos_disponibles
            campeonato_elegido = campeonatos_para_elegir[int(entry2.get()) - 1]
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato_elegido.getNombre())

            equipos_continente = Equipo.equipos_continente(continente)
            equipos_disponibles = Equipo.equipos_disponibles(equipos_continente)
            # Colocar los equipos disponibles
            jj = 1
            for equipo in equipos_disponibles:
                listbox3.insert(jj, str(jj) + " | " + equipo.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame2.grid_remove()
            frame2.grid_forget()
            frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame3.tkraise()

        # Para frame 3
        def elegir_equipo():
            global equipo_elegido, campeonato_elegido, equipos_disponibles, participantes
            equipo_elegido = equipos_disponibles[int(entry3.get()) - 1]
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el equipo " + equipo_elegido.get_nombre())
            participantes = Equipo.elegir_contrincantes(equipo_elegido, campeonato_elegido, equipos_disponibles)
            jj = 1
            for equipo in participantes:
                listbox4.insert(jj, str(jj) + " | " + equipo.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame3.grid_remove()
            frame3.grid_forget()
            frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame4.tkraise()

        # Para frame 4
        def confirmar_equipos():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo
            #tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
            pilotos_disponibles = Piloto.pilotos_disponibles()
            pilotos_equipo = Piloto.pilotos_equipo(equipo_elegido, pilotos_disponibles)
            jj = 1
            for piloto in pilotos_equipo:
                listbox5.insert(jj, str(jj) + " | " + piloto.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame4.grid_remove()
            frame4.grid_forget()
            frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame5.tkraise()

        # Para frame 5.1
        def elegir_primer_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, pilotos_participar
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

        # Para frame 5.2
        def elegir_segundo_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, piloto_2, pilotos_participar, patrocinadores_disponibles, patrocinadores_piloto_1
            piloto_2 = pilotos_equipo[int(entry5_2.get()) - 1]
            pilotos_participar.append(piloto_2)
            #tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos pilotos de tu equipo")
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
                listbox6_1.insert(jj, str(jj) + " | " + patrocinador.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame5.grid_remove()
            frame5.grid_forget()
            frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame6.tkraise()

        # Para frame 6.1
        def elegir_primer_patrocinador():
            global campeonato_elegido, equipo_elegido, participantes, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1
            patrocinador_1 = patrocinadores_piloto_1[int(entry6_1.get()) - 1]
            patrocinador_1.pensarNegocio(piloto_1)

            # Patrocinadores segundo piloto
            patrocinadores_piloto_2 = Patrocinador.patrocinadorPiloto(piloto_2, patrocinadores_disponibles)
            jj = 1
            for patrocinador in patrocinadores_piloto_2:
                listbox6_2.insert(jj, str(jj) + " | " + patrocinador.get_nombre())
                jj += 1
            # Quitar label y boton
            entry6_1.destroy()
            button6_1.destroy()
            listbox6_1.destroy()
            # Colocar nuevo boton
            button6_2.configure(text="Elegir Segundo Patrocinador")

        # Para frame 6.2
        def elegir_segundo_patrocinador():
            global continente, campeonato_elegido, equipo_elegido, participantes, pilotos_participar, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1, patrocinador_2
            patrocinador_2 = patrocinadores_piloto_2[int(entry6_2.get()) - 1]
            patrocinador_2.pensarNegocio(piloto_2)
            #tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos patrocinadores de tu equipo")

            # Campeonato is now unlocked
            campeonato_elegido.setDesbloqueado(True)

            listbox7_1.insert(0, "Nombre del campeonato: " + campeonato_elegido.getNombre())
            listbox7_1.insert(1, "Continente: " + continente.value)
            listbox7_1.insert(2, "Cantidad de carreras:" + str(campeonato_elegido.getCantidadMaxCarreras()))
            jj = 1
            for piloto in pilotos_participar:
                listbox7_2.insert(jj, str(jj) + ". " + piloto.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame6.grid_remove()
            frame6.grid_forget()
            frame7.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame7.tkraise()

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
        ii = 1
        for continentico in Continente:
            listbox1.insert(ii, str(ii) + " | " + continentico.value)
            ii += 1
        listbox1.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
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
        listbox2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        listbox3.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        listbox4.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        button4 = tk.Button(frame4, text="Confirmar Equipos", command=lambda: confirmar_equipos())
        button4.grid(column=0, row=7, padx=20, pady=20)
        button4.configure(justify="center")

        # Frame 5: Escoger Equipo
        frame5 = FieldFrame(self.frames[frame_name], None, "Escoger Pilotos para Correr",
                            "Estos son los pilotos pertenecientes al equipo que elegiste.\nEscoge los dos que mas te llamen la atencion")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox5 = tk.Listbox(frame5)
        listbox5.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        listbox6_2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        listbox6_1 = tk.Listbox(frame6)
        listbox6_1.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        label7_1 = tk.Label(frame7, text="Los detalles de tu campeonato")
        label7_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        listbox7_1 = tk.Listbox(frame7)
        listbox7_1.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        label7_2 = tk.Label(frame7, text="Los pilotos participantes")
        label7_2.grid(column=0, row=7, padx=20, pady=20, sticky="nsew")
        listbox7_2 = tk.Listbox(frame7)
        listbox7_2.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
        button7 = tk.Button(frame7, text="Volver a Crear un Campeonato", command=lambda: muerte_y_destruccion())
        button7.grid(column=0, row=11, padx=20, pady=20)
        button7.configure(justify="center")

        frame1.tkraise()

    # Funcionalidad 2: Planificar Calendario de Carreras
    def planificar_calendario(self, frame_name):
        # Metodos importantes para la funcionalidad
        # Para frame 1
        def elegir_campeonato():
            global campeonato, cantidad_carreras, circuitos_ubicacion, directores_para_elegir, ciudades_disponibles, meses_disponibles, dificultades
            print(entry1.get()) # Para debuggear
            campeonato = campeonatos_desbloqueados[int(entry1.get()) - 1]
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato.getNombre() + "\nEl campeonato tiene " + str(campeonato.getCantidadMaxCarreras()) + " carreras, debes planificarlas todas")
            cantidad_carreras = campeonato.getCantidadMaxCarreras()
            print(cantidad_carreras) # Para debuggear
            circuitos_ubicacion = Circuito.circuitos_ubicacion(campeonato)
            print(circuitos_ubicacion)
            ciudades_disponibles = Ciudad.ciudades_continente(campeonato.getContinente())
            print(ciudades_disponibles)

            directores_para_elegir = DirectorCarrera.dc_disponibles()
            jj = 1

            for director in directores_para_elegir:
                listbox2.insert(jj, str(jj) + " | " + director.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame1.grid_remove()
            frame1.grid_forget()
            frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame2.tkraise()

        # Para frame 2
        def elegir_director():
            # all variables used
            global directores_para_elegir, director_elegido, circuitos_ubicacion,ciudades_nombres, circuitos_vender, ciudades_disponibles, ciudad_seleccionada, ciudad_elegida, circuitos_para_elegir, meses_disponibles, mes_seleccionado, mes_elegido, dificultades, dificultad_seleccionada, dificultad_elegida
            print(entry2.get()) # Para debuggear
            print(directores_para_elegir) # Para debuggear
            director_elegido = directores_para_elegir[int(entry2.get()) - 1]
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + director_elegido.get_nombre())
            print(director_elegido) # Para debuggear
            print(circuitos_ubicacion) # Para debuggear
            circuitos_vender = Circuito.circuitos_vender(director_elegido, circuitos_ubicacion)
            print(circuitos_vender) # Para debuggear
            print(ciudades_disponibles) # Para debuggear
            ciudades_nombres = [ciudad.get_nombre() for ciudad in ciudades_disponibles]
            print(ciudades_nombres) # Para debuggear
            ciudad_seleccionada = tk.StringVar(frame3)
            ciudad_seleccionada.set(ciudades_nombres[0])

            dropdown_ciudad = tk.OptionMenu(frame3, ciudad_seleccionada, *ciudades_nombres)
            dropdown_ciudad.bind("<Configure>", elegir_ciudad)
            dropdown_ciudad.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
            dropdown_ciudad.configure(justify="center")

            # Pasar al siguiente frame
            frame2.grid_remove()
            frame2.grid_forget()
            dropdown_ciudad.grid_remove()
            frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame3.tkraise()

        # Para frame 3
        def elegir_mes(event):
            global mes_seleccionado, meses_disponibles, mes_elegido
            mes_elegido = int(mes_seleccionado.get())

        def elegir_dificultad(event):
            global dificultad_seleccionada, dificultad_elegida, dificultades
            dif = dificultad_seleccionada.get()
            dificultades_dict = {"Principiante": 1, "Avanzado": 2, "Experto": 3}
            dificultad_elegida = dificultades_dict.get(dif)

        def elegir_ciudad(event):
            global ciudad_seleccionada, ciudad_elegida
            ciudad_nombre = ciudad_seleccionada.get()
            ciudad_elegida = [ciudad for ciudad in ciudades_disponibles if ciudad.get_nombre() == ciudad_nombre][0]

        def elegir_mes_dificutad_ciudad():
            global mes_seleccionado, meses_disponibles, mes_elegido, dificultad_seleccionada, dificultad_elegida, dificultades, ciudad_seleccionada, ciudad_elegida, circuitos_para_elegir
            meses_disponibles.remove(mes_elegido)
            #tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
            circuitos_para_elegir = Circuito.circuitos_disponibles(mes_elegido, circuitos_vender)
            jj = 1
            for circuito in circuitos_para_elegir:
                listbox4.insert(jj, str(jj) + " | " + circuito.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame3.grid_remove()
            frame3.grid_forget()
            frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame4.tkraise()

        # Para frame 4
        def elegir_circuito():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo
            #tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
            pilotos_disponibles = Piloto.pilotos_disponibles()
            pilotos_equipo = Piloto.pilotos_equipo(equipo_elegido, pilotos_disponibles)
            jj = 1
            for piloto in pilotos_equipo:
                listbox5.insert(jj, str(jj) + " | " + piloto.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame4.grid_remove()
            frame4.grid_forget()
            frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame5.tkraise()

        # Para frame 5.1
        def elegir_primer_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, pilotos_participar
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

        # Para frame 5.2
        def elegir_segundo_piloto():
            global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo, piloto_1, piloto_2, pilotos_participar, patrocinadores_disponibles, patrocinadores_piloto_1
            piloto_2 = pilotos_equipo[int(entry5_2.get()) - 1]
            pilotos_participar.append(piloto_2)
            #tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos pilotos de tu equipo")
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
                listbox6_1.insert(jj, str(jj) + " | " + patrocinador.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame5.grid_remove()
            frame5.grid_forget()
            frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame6.tkraise()

        # Para frame 6.1
        def elegir_primer_patrocinador():
            global campeonato_elegido, equipo_elegido, participantes, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1
            patrocinador_1 = patrocinadores_piloto_1[int(entry6_1.get()) - 1]
            patrocinador_1.pensarNegocio(piloto_1)

            # Patrocinadores segundo piloto
            patrocinadores_piloto_2 = Patrocinador.patrocinadorPiloto(piloto_2, patrocinadores_disponibles)
            jj = 1
            for patrocinador in patrocinadores_piloto_2:
                listbox6_2.insert(jj, str(jj) + " | " + patrocinador.get_nombre())
                jj += 1
            # Quitar label y boton
            entry6_1.destroy()
            button6_1.destroy()
            listbox6_1.destroy()
            # Colocar nuevo boton
            button6_2.configure(text="Elegir Segundo Patrocinador")

        # Para frame 6.2
        def elegir_segundo_patrocinador():
            global continente, campeonato_elegido, equipo_elegido, participantes, pilotos_participar, piloto_1, piloto_2, patrocinadores_disponibles, patrocinadores_piloto_1, patrocinadores_piloto_2, patrocinador_1, patrocinador_2
            patrocinador_2 = patrocinadores_piloto_2[int(entry6_2.get()) - 1]
            patrocinador_2.pensarNegocio(piloto_2)
            #tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos patrocinadores de tu equipo")

            # Campeonato is now unlocked
            campeonato_elegido.setDesbloqueado(True)

            listbox7_1.insert(0, "Nombre del campeonato: " + campeonato_elegido.getNombre())
            listbox7_1.insert(1, "Continente: " + continente.value)
            listbox7_1.insert(2, "Cantidad de carreras:" + str(campeonato_elegido.getCantidadMaxCarreras()))
            jj = 1
            for piloto in pilotos_participar:
                listbox7_2.insert(jj, str(jj) + ". " + piloto.get_nombre())
                jj += 1

            # Pasar al siguiente frame
            frame6.grid_remove()
            frame6.grid_forget()
            frame7.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame7.tkraise()

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

        # Frame 1: Escoger Campeonato desbloqueados
        frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un campeonato desbloqueado",
                            "Elige un campeonato disponible para planificar su calendario", "img/car.png")
        frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        # Componentes del frame
        listbox1 = tk.Listbox(frame1)
        ii = 1

        campeonatos_desbloqueados = Campeonato.campeonatosDesbloqueados()
        for campeonato in campeonatos_desbloqueados:
            listbox1.insert(ii, str(ii) + " | " + campeonato.getNombre())
            ii += 1
        listbox1.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
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
        carreras_listo = 0
        # meses disponibles
        meses_disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        dificultades = ["Principiante", "Avanzado", "Experto"]

        # Frame 2: Escoger Director de Carrera
        frame2 = FieldFrame(self.frames[frame_name], None, "Elegir tu Director de Carrera",
                            "De los directores disponibles, elige el que mas te guste. ")
        frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox2 = tk.Listbox(frame2)
        listbox2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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


        # Frame 3: Escoger Mes, Dificultad y Ciudad
        frame3 = FieldFrame(self.frames[frame_name], None, "Escoger Mes, Dificultad y Ciudad",
                            "Estos son los meses, dificultades y ciudades disponibles para correr.\nEscoge uno de cada uno!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        mes_seleccionado = tk.StringVar(frame3)
        mes_seleccionado.set(meses_disponibles[0])
        mes_elegido = None
        dropdown_meses = tk.OptionMenu(frame3, mes_seleccionado, *meses_disponibles)
        dropdown_meses.bind("<Configure>", elegir_mes)

        dropdown_meses.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        dropdown_meses.configure(justify="center")
        dificultad_elegida = 1
        dificultad_seleccionada = tk.StringVar(frame3)
        dificultad_seleccionada.set(dificultades[0])
        dropdown_dificultad = tk.OptionMenu(frame3, dificultad_seleccionada, *dificultades)
        dropdown_dificultad.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        dropdown_dificultad.bind("<Configure>", elegir_dificultad)
        dropdown_dificultad.configure(justify="center")
        ciudad_elegida = None
        ciudades_nombres = [ciudad.get_nombre() for ciudad in ciudades_disponibles]

        listbox3 = tk.Listbox(frame3)
        listbox3.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        entry3 = tk.Entry(frame3)
        entry3.grid(column=0, row=6, padx=20, pady=20)
        entry3.configure(justify="center")
        button3 = tk.Button(frame3, text="Elegir", command=lambda: elegir_mes_dificutad_ciudad())
        button3.grid(column=0, row=7, padx=20, pady=20)
        button3.configure(justify="center")
        # Dificultad elegida
        dificultad_elegida = None
        # Mes elegido
        mes_elegido = None
        # Ciudad elegida
        ciudad_elegida = None
        # El equipo que elige el usuario
        equipo_elegido = None
        # Equipos totales
        participantes = []
        # Pilotos del equipo
        pilotos_equipo = []
        # circuitos para elegir
        circuitos_para_elegir = []

        # Frame 4: Escoger Circuito
        frame4 = FieldFrame(self.frames[frame_name], None, "Circuitos Disponibles",
                            "Estos son los circuitos disponibles el mes que seleccioanste que puede pagar el director de carrera \ny que estan en el continente")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Comp4onentes del frame
        listbox4 = tk.Listbox(frame4)
        listbox4.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        button4 = tk.Button(frame4, text="Elegir Circuito", command=lambda: elegir_circuito())
        button4.grid(column=0, row=7, padx=20, pady=20)
        button4.configure(justify="center")

        # Frame 5: Escoger Equipo
        frame5 = FieldFrame(self.frames[frame_name], None, "Escoger Pilotos para Correr",
                            "Estos son los pilotos pertenecientes al equipo que elegiste.\nEscoge los dos que mas te llamen la atencion")
        frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        listbox5 = tk.Listbox(frame5)
        listbox5.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        listbox6_2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
        listbox6_1 = tk.Listbox(frame6)
        listbox6_1.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
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
        label7_1 = tk.Label(frame7, text="Los detalles de tu campeonato")
        label7_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        listbox7_1 = tk.Listbox(frame7)
        listbox7_1.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        label7_2 = tk.Label(frame7, text="Los pilotos participantes")
        label7_2.grid(column=0, row=7, padx=20, pady=20, sticky="nsew")
        listbox7_2 = tk.Listbox(frame7)
        listbox7_2.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
        button7 = tk.Button(frame7, text="Volver a Crear un Campeonato", command=lambda: muerte_y_destruccion())
        button7.grid(column=0, row=11, padx=20, pady=20)
        button7.configure(justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)

    # COMIENZO PRUEBA
    Serializado.crearObjetos()
    # FIN PRUEBA

    sk.set_theme("dark")
    root.mainloop()
