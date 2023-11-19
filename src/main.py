import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

import sv_ttk as sk

# Imports de las clases
from src.base_datos.Serializado import Serializado
from src.gestor_aplicacion.campeonato.Carrera import Carrera
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



        description_label = tk.Label(self, text=descripcion, anchor="center")

        #inner_frame = tk.Frame(self, padx=5, pady=5, bg=color)
        #inner_frame.grid(row=0, column=0, columnspan=2, pady=5)

        # Create labels for the title and description
        title_label = tk.Label(self, text=nombre_proceso, font=("Helvetica", 16), anchor="center")
        self.configure(padx=20, pady=20)
        #self.grid(row=0, column=0, sticky="nsew")

        # Use grid to make labels span the same width as the window
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        title_label.configure(justify="center")
        description_label.grid(row=1, column=0, padx=20, sticky="nsew")
        description_label.configure(justify="center")

        if logo_path == "random":
            img_paths = ["img/car.png", "img/polo.png", "img/chaqueta-de-carreras.png", "img/f1.png"]
            logo_path = random.choice(img_paths)

        self.img = (Image.open(logo_path))
        resized_image = self.img.resize((30, 30))
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

        # # Adjust column weights to allocate space for the new column
        # self.grid_rowconfigure("all", weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=0)  # Adjust the weight for the new column
        # # adjust the height of the new column to small
        # self.grid_columnconfigure(2, weight=1)


class MenuApp:
    def __init__(self, root):
        self.menu_bar = None
        self.root = root
        self.root.title("GP Racing: The one and only!")
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
            lista_continentes = [c for c in Continente]
            continente = lista_continentes[int(entry1.get()) - 1]
            # continente = Ciudad.convertir_continente(int(entry1.get()))
            #tk.messagebox.showinfo("Eleccion realizada", "Has escogido el continente " + continente.value)

            campeonatos_disponibles = Campeonato.campeonatosDisponibles()
            campeonatos_continente = Campeonato.campeonatosContinente(continente)
            campeonatos_para_elegir = []
            for campeonato in campeonatos_disponibles:
                if campeonato.getContinente() == continente:
                    campeonatos_para_elegir.append(campeonato)
            jj = 1

            for campeonatico in campeonatos_para_elegir:
                tablaCampeonatos.insert(parent='', index=tk.END, values=(jj,campeonatico.getNombre()))
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
                tablaEquipos.insert(parent='', index=tk.END, values=(jj,equipo.get_nombre()))
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
                tablaParticipantes.insert(parent='', index=tk.END, values=(jj,equipo.get_nombre()))
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
                tablaPilotos.insert(parent='', index=tk.END, values=(jj,piloto.get_nombre()))
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
                tablaPatrocinadores1.insert(parent='', index=tk.END, values=(jj,patrocinador.get_nombre()))
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
                tablaPatrocinadores2.insert(parent='', index=tk.END, values=(jj,patrocinador.get_nombre()))
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

            # listbox7_1.insert(0, "Nombre del campeonato: " + campeonato_elegido.getNombre())
            # listbox7_1.insert(1, "Continente: " + continente.value)
            # listbox7_1.insert(2, "Cantidad de carreras:" + str(campeonato_elegido.getCantidadMaxCarreras()))

            tablaCampeonatoResultante.insert(parent='', index=tk.END, values=("Nombre del campeonato:",campeonato_elegido.getNombre()))
            tablaCampeonatoResultante.insert(parent='', index=tk.END,values=("Continente: " , continente.value))
            tablaCampeonatoResultante.insert(parent='', index=tk.END,values=("Cantidad de carreras:",str(campeonato_elegido.getCantidadMaxCarreras())))
            tablaCampeonatoResultante.configure(height=1)

            jj = 1
            for piloto in pilotos_participar:
                tablaPilotosParticipantes.insert(parent='', index=tk.END, values=(jj,piloto.get_nombre()))
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
        label7_1 = tk.Label(frame7, text="Los detalles de tu campeonato")
        label7_1.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        listbox7_1 = tk.Listbox(frame7)

        #crear Tabla
        tablaCampeonatoResultante = ttk.Treeview(frame7, columns= ('1','2'), show="")




        tablaCampeonatoResultante.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        label7_2 = tk.Label(frame7, text="Los pilotos participantes")
        label7_2.grid(column=0, row=7, padx=20, pady=20, sticky="nsew")
        listbox7_2 = tk.Listbox(frame7)

        # crear Tabla
        tablaPilotosParticipantes = ttk.Treeview(frame7, columns=('OPCION', 'NOMBRE'), show='headings')
        # configurar los cabezales
        tablaPilotosParticipantes.heading('OPCION', text='POSICION')
        tablaPilotosParticipantes.heading('NOMBRE', text='NOMBRE')
        tablaPilotosParticipantes.column('OPCION', width=30, anchor='c')

        tablaPilotosParticipantes.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")

        button7 = tk.Button(frame7, text="Volver a Crear un Campeonato", command=lambda: muerte_y_destruccion())
        button7.grid(column=0, row=11, padx=20, pady=20)
        button7.configure(justify="center")

        frame1.tkraise()

    # Funcionalidad 2: Planificar Calendario de Carreras
    def planificar_calendario(self, frame_name):
        global carreras_listo, meses_disponibles, mes_seleccionado, campeonato
        carreras_listo = 0
        meses_disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
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
            combobox_meses['values'] = meses_disponibles
            mes_seleccionado.set(meses_disponibles[0])
            # Pasar al siguiente frame
            frame2.grid_remove()
            frame2.grid_forget()
            frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame3.tkraise()

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
            global circuitos_para_elegir, mes_elegido, circuitos_vender, ciudades_nombres, ciudades_disponibles
            #tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
            circuitos_para_elegir = Circuito.circuitos_disponibles(int(mes_elegido), circuitos_vender)
            jj = 1
            for circuito in circuitos_para_elegir:
                listbox4.insert(jj, str(jj) + " | " + circuito.get_nombre())
                jj += 1

            ciudades_nombres = [ciudad.get_nombre() for ciudad in ciudades_disponibles]
            combobox_ciudad['values'] = ciudades_nombres
            # Pasar al siguiente frame
            frame3.grid_remove()
            frame3.grid_forget()
            frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame4.tkraise()

        # Para frame 4

        def elegir_ciudad(event):
            global ciudad_seleccionada, ciudad_elegida, ciudades_disponibles
            ciudad_seleccionada = combobox_ciudad.get()
            ciudad_elegida = [ciudad for ciudad in ciudades_disponibles if ciudad.get_nombre() == ciudad_seleccionada][0]

        def elegir_circuito():
            global circuito_elegido, circuitos_para_elegir, carrera_creada, ciudad_elegida, dificultad_elegida, dificultad_elegida, circuito_elegido, mes_elegido, director_elegido, campeonato, carreras_listo, meses_disponibles
            circuito_elegido = circuitos_para_elegir[int(entry4.get()) - 1]
            #tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
            carrera_creada = Carrera(ciudad_elegida, dificultad_elegida, dificultad_elegida, circuito_elegido, int(mes_elegido), director_elegido)
            carreras_listo += 1
            combobox_meses.set('')
            campeonato.agregarCarrera(carrera_creada)
            meses_disponibles.remove(mes_elegido)

            if carreras_listo == campeonato.getCantidadMaxCarreras():
                # Pasar al siguiente frame
                frame4.grid_remove()
                frame4.grid_forget()
                frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame5.tkraise()
            else: # volver al frame 2
                frame4.grid_remove()
                frame4.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()



        # Para frame 5
        def elegir_premios():
            global premio_campeonato, premio_carreras, campeonato
            premio_campeonato = float(entry5_1.get())
            premio_carreras = float(entry5_2.get())

            campeonato.logisticaPremios(premio_campeonato, premio_carreras)
            campeonato.organizarCarreras()

            jj = 1
            for carrera in campeonato.getListaCarreras():
                listbox6.insert(jj, str(jj) + " | " + carrera.nombre_circuito+ " | " + carrera.getFecha() + " | " + str(carrera.getPremioEfectivo()))
                jj += 1

            # Pasar al siguiente frame
            frame5.grid_remove()
            frame5.grid_forget()
            frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            frame6.tkraise()

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

        # meses disponibles
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


        # Frame 3: Escoger Mes, Dificultad
        frame3 = FieldFrame(self.frames[frame_name], None, "Escoger Mes, Dificultad y Ciudad",
                            "Estos son los meses, dificultades y ciudades disponibles para correr.\nEscoge uno de cada uno!")
        frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        mes_seleccionado = tk.StringVar(frame3)
        mes_seleccionado.set(meses_disponibles[0])
        # Create Combobox for month selection
        combobox_meses = ttk.Combobox(frame3, values=meses_disponibles)
        combobox_meses.grid(column=0, row=3, padx=20, pady=20)
        combobox_meses.bind("<<ComboboxSelected>>", elegir_mes)
        combobox_meses.configure(justify="center")

        # Create Combobox for difficulty selection
        dificultad_seleccionada = tk.StringVar(frame3)
        dificultad_seleccionada.set(dificultades[0])
        combobox_dificultad = ttk.Combobox(frame3, textvariable=dificultad_seleccionada, values=dificultades)
        combobox_dificultad.grid(column=0, row=4, padx=20, pady=20)
        combobox_dificultad.bind("<<ComboboxSelected>>", elegir_dificultad)
        combobox_dificultad.configure(justify="center")

        ciudad_elegida = None

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
        frame4 = FieldFrame(self.frames[frame_name], None, "Circuitos Disponibles",
                            "Estos son los circuitos disponibles el mes que seleccioanste que puede pagar el director de carrera \ny que estan en el continente")
        frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Comp4onentes del frame

        ciudad_seleccionada = tk.StringVar(frame4)
        ciudad_seleccionada.set(dificultades[0])
        combobox_ciudad = ttk.Combobox(frame4, values=dificultades)
        combobox_ciudad.grid(column=0, row=2, padx=20, pady=20)
        combobox_ciudad.bind("<<ComboboxSelected>>", elegir_ciudad)
        combobox_ciudad.configure(justify="center")

        listbox4 = tk.Listbox(frame4)
        listbox4.grid(column=0, row=3, rowspan=2, padx=20, pady=20, sticky="nsew")

        entry4 = tk.Entry(frame4)
        entry4.grid(column=0, row=6, padx=20, pady=20)
        entry4.configure(justify="center")

        button4 = tk.Button(frame4, text="Elegir Circuito", command=lambda: elegir_circuito())
        button4.grid(column=0, row=7, padx=20, pady=20)
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

        label5_2 = tk.Label(frame5, text="Premio en efectivo todas las carreras")
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
        frame6 = FieldFrame(self.frames[frame_name], None, "Campeonato Preparado",
                            "Con todo lo que has organizado,\nfinalmente este es el campeonato que has creado")
        frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        # Componentes del frame
        label6 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
        label6.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")

        listbox6 = tk.Listbox(frame6)
        listbox6.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
        button6 = tk.Button(frame6, text="Volver a Preparar un Campeonato", command=lambda: muerte_y_destruccion())
        button6.grid(column=0, row=11, padx=20, pady=20)
        button6.configure(justify="center")

        # Funcionalidad 3: Personaliazar Veheiculo de Carrera
        def personalizar_vehiculo(self, frame_name):
            global pilotos_desbloqueados

            def elegir_piloto():
                global piloto_seleccionado, pilotos_desbloqueados, chasis_disponibles
                piloto_seleccionado = pilotos_desbloqueados[int(entry1.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato.getNombre() + "\nEl campeonato tiene " + str(campeonato.getCantidadMaxCarreras()) + " carreras, debes planificarlas todas")
                chasis_disponibles = Chasis.chasis_disponibles(piloto_seleccionado)
                jj = 1

                for chasis in chasis_disponibles:
                    listbox2.insert(jj, str(jj) + " | " + chasis.marca + " | " + chasis.modelo + " | " + str(
                        chasis.velocidad) + " | " + str(chasis.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame1.grid_remove()
                frame1.grid_forget()
                frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame2.tkraise()

            # Para frame 2
            def elegir_chasis():
                # all variables used
                global chasis_seleccionado, chasis_disponibles, vehiculo_seleccionado, combinaciones, alerones_disponibles
                chasis_seleccionado = chasis_disponibles[int(entry2.get()) - 1]
                # tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + director_elegido.get_nombre())
                vehiculo_seleccionado = chasis_seleccionado.comprar(piloto_seleccionado)
                combinaciones = Pieza.combinaciones(vehiculo_seleccionado)
                alerones_disponibles = Pieza.filterAlerones(combinaciones)

                jj = 1
                for aleron in alerones_disponibles:
                    listbox3.insert(jj, str(jj) + " | " + aleron.marca + " | " + aleron.modelo + " | " + str(
                        aleron.velocidad) + " | " + str(aleron.precio))
                    jj += 1
                # Pasar al siguiente frame

                frame2.grid_remove()
                frame2.grid_forget()
                frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame3.tkraise()

            # Para frame 3
            def elegir_aleron():
                global aleron_seleccionado, alerones_disponibles, combinaciones2, vehiculo_seleccionado, combinaciones, neumaticos_disponibles
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                aleron_seleccionado = alerones_disponibles[int(entry3.get()) - 1]
                combinaciones2 = Pieza.combinacionesDisponibles(vehiculo_seleccionado, aleron_seleccionado,
                                                                combinaciones)
                neumaticos_disponibles = Pieza.filterNeumaticos(combinaciones2)

                jj = 1
                for neumatico in neumaticos_disponibles:
                    listbox4.insert(jj, str(jj) + " | " + neumatico.marca + " | " + neumatico.modelo + " | " + str(
                        neumatico.velocidad) + " | " + str(neumatico.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame3.grid_remove()
                frame3.grid_forget()
                frame4.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame4.tkraise()

            # Para frame 4
            def elegir_neumatico():
                global neumaticos_disponibles
                # tk.messagebox.showinfo("Eleccion realizada", "\nHas escogido el mes " + mes_elegido + "\nHas escogido la dificultad " + dificultad_elegida + "\nHas escogido la ciudad " + ciudad_elegida.get_nombre())
                neumatico_seleccionado = neumaticos_disponibles[int(entry4.get()) - 1]
                combinaciones3 = Pieza.combinacionesDisponibles(vehiculo_seleccionado, neumatico_seleccionado,
                                                                combinaciones2)
                motores_disponibles = Pieza.filterMotores(combinaciones3)

                jj = 1
                for motor in motores_disponibles:
                    listbox5.insert(jj, str(jj) + " | " + motor.marca + " | " + motor.modelo + " | " + str(
                        motor.velocidad) + " | " + str(motor.precio))
                    jj += 1

                # Pasar al siguiente frame
                frame4.grid_remove()
                frame4.grid_forget()
                frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame5.tkraise()

            # Para frame 5
            def descuento():
                global premio_campeonato, premio_carreras, campeonato
                premio_campeonato = float(entry5_1.get())
                premio_carreras = float(entry5_2.get())
                print(campeonato.getListaCarreras())  # Para debuggear
                campeonato.logisticaPremios(premio_campeonato, premio_carreras)
                print(campeonato.getListaCarreras())  # Para debuggear
                campeonato.organizarCarreras()
                print(campeonato.getListaCarreras())  # Para debuggear

                jj = 1
                for carrera in campeonato.getListaCarreras():
                    listbox6.insert(jj,
                                    str(jj) + " | " + carrera.getNombreCircuito() + " | " + carrera.getFecha() + " | " + str(
                                        carrera.getPremioEfectivo()))
                    jj += 1

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()

            # Para frame 6
            def entrega():
                global premio_campeonato, premio_carreras, campeonato
                premio_campeonato = float(entry5_1.get())
                premio_carreras = float(entry5_2.get())
                print(campeonato.getListaCarreras())  # Para debuggear
                campeonato.logisticaPremios(premio_campeonato, premio_carreras)
                print(campeonato.getListaCarreras())  # Para debuggear
                campeonato.organizarCarreras()
                print(campeonato.getListaCarreras())  # Para debuggear

                jj = 1
                for carrera in campeonato.getListaCarreras():
                    listbox6.insert(jj,
                                    str(jj) + " | " + carrera.getNombreCircuito() + " | " + carrera.getFecha() + " | " + str(
                                        carrera.getPremioEfectivo()))
                    jj += 1

                # Pasar al siguiente frame
                frame5.grid_remove()
                frame5.grid_forget()
                frame6.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
                frame6.tkraise()

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

            # Frame 1: Escoger Piloto desbloqueados
            frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un piloto desbloqueado",
                                "Elige un piloto para personalizar su vehiculo de carreras", "img/car.png")
            frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
            # Componentes del frame
            listbox1 = tk.Listbox(frame1)
            ii = 1

            pilotos_desbloqueados = Piloto.pilotos_desbloqueados()

            for piloto in pilotos_desbloqueados:
                listbox1.insert(ii, str(ii) + " | " + piloto.nombre + " | " + piloto.contrato.nombre)
                ii += 1

            listbox1.grid(column=0, row=3, rowspan=3, padx=20, pady=20)
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
            frame2 = FieldFrame(self.frames[frame_name], None, "Elige un chasis para el vehiculo de carreras",
                                "Estos son los alerones disponibles para tu piloto de acuerdo a su presupuesto y de la marca de tu chasis")
            frame2.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            listbox2 = tk.Listbox(frame2)
            listbox2.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
            entry2 = tk.Entry(frame2)
            entry2.grid(column=0, row=6, padx=20, pady=20)
            entry2.configure(justify="center")
            button2 = tk.Button(frame2, text="Elegir Director", command=lambda: elegir_chasis())
            button2.grid(column=0, row=7, padx=20, pady=20)
            button2.configure(justify="center")
            # Variables
            chasis_seleccionado = None
            alerones_disponibles = []
            combinaciones = []

            # Frame 3: Elegr Aleron
            frame3 = FieldFrame(self.frames[frame_name], None, "Escoger Mes, Dificultad y Ciudad",
                                "Estos son los meses, dificultades y ciudades disponibles para correr.\nEscoge uno de cada uno!")
            frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            listbox3 = tk.Listbox(frame3)
            listbox3.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
            entry3 = tk.Entry(frame3)
            entry3.grid(column=0, row=6, padx=20, pady=20)
            entry3.configure(justify="center")
            button3 = tk.Button(frame3, text="Elegir", command=lambda: elegir_aleron())
            button3.grid(column=0, row=7, padx=20, pady=20)
            button3.configure(justify="center")
            # Variables
            aleron_seleccionado = None
            combinaciones2 = []
            neumaticos_disponibles = []

            # Frame 4: Escoger Neumatico
            frame4 = FieldFrame(self.frames[frame_name], None, "Circuitos Disponibles",
                                "Estos son los circuitos disponibles el mes que seleccioanste que puede pagar el director de carrera \ny que estan en el continente")
            frame4.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            listbox4 = tk.Listbox(frame4)
            listbox4.grid(column=0, row=3, rowspan=2, padx=20, pady=20, sticky="nsew")

            entry4 = tk.Entry(frame4)
            entry4.grid(column=0, row=6, padx=20, pady=20)
            entry4.configure(justify="center")

            button4 = tk.Button(frame4, text="Elegir Circuito", command=lambda: elegir_neumatico())
            button4.grid(column=0, row=7, padx=20, pady=20)
            button4.configure(justify="center")

            # Variables
            neumatico_elegido = None
            motores_disponibles = []
            combinaciones3 = []

            # Frame 5: Elegr Motor
            frame5 = FieldFrame(self.frames[frame_name], None, "Elige los premios ",
                                "Elige el valor del premio del ganador del campeonato y elige el premio en efectivo destinado para premiar todas las carreras")
            frame5.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            listbox5 = tk.Listbox(frame5)
            listbox5.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
            entry5 = tk.Entry(frame5)
            entry5.grid(column=0, row=4, padx=20, pady=20)
            entry5.configure(justify="center")

            button5 = tk.Button(frame5, text="Elegir", command=lambda: elegir_premios())
            button5.grid(column=0, row=7, padx=20, pady=20)
            button5.configure(justify="center")

            # Primer y Segundo piloto del equipo
            premio_campeonato = 0
            premio_carreras = 0

            # Frame 6: Descuento
            frame6 = FieldFrame(self.frames[frame_name], None, "Campeonato Preparado",
                                "Con todo lo que has organizado,\nfinalmente este es el campeonato que has creado")
            frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            label6 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
            label6.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")

            listbox6 = tk.Listbox(frame6)
            listbox6.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
            button6 = tk.Button(frame6, text="Volver a Preparar un Campeonato", command=lambda: muerte_y_destruccion())
            button6.grid(column=0, row=11, padx=20, pady=20)
            button6.configure(justify="center")

            # Frame 7: Entrega
            frame6 = FieldFrame(self.frames[frame_name], None, "Campeonato Preparado",
                                "Con todo lo que has organizado,\nfinalmente este es el campeonato que has creado")
            frame6.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
            # Componentes del frame
            label6 = tk.Label(frame6, text="Este es el calendario de carreras del campeonato")
            label6.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")

            listbox6 = tk.Listbox(frame6)
            listbox6.grid(column=0, row=8, rowspan=3, padx=20, pady=20, sticky="nsew")
            button6 = tk.Button(frame6, text="Volver a Preparar un Campeonato", command=lambda: muerte_y_destruccion())
            button6.grid(column=0, row=11, padx=20, pady=20)
            button6.configure(justify="center")

    def acerca_de(self, frame_name):
        self.change_frame(frame_name)
        frame_acerca = FieldFrame(self.frames[frame_name], None, "¡Bienvenido al Proyecto FIA!")
        frame_acerca.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
        frame_acerca.grid(column=0, row=0, padx=20, pady=20, sticky="nsew")

        info_text = """
                 Nuestra aplicación te permite gestionar todo lo relacionado con un emocionante campeonato de carreras automovilísticas. Desde planificar las carreras hasta personalizar los vehículos, todo está al alcance de tus manos.

                 ¿Qué puedes hacer?
                 """

        funcionalidades = """
                 1. Preparar el Campeonato: 
                 Elige el campeonato que más te guste y planifica las carreras.

                 2. Seleccionar Directores de Carrera:
                 Escoge a los directores de carrera que liderarán cada evento.

                 3. Escoger Mes, Dificultad y Ciudad: 
                 Elige el momento perfecto, la dificultad adecuada y la ciudad ideal para cada carrera.

                 4. Elegir Circuitos y Ciudades: 
                 Explora los circuitos disponibles y decide en qué ciudad se llevará a cabo cada carrera.

                 5. Definir Premios: 
                 Personaliza los premios para los campeonatos y carreras.
         """
        mensaje_final = """
         Todo está diseñado de forma sencilla y modular para que disfrutes de una experiencia completa y emocionante.

         ¡Prepárate para la emoción de la pista!"""
        # Etiqueta para mostrar el texto informativo
        info_label = tk.Label(frame_acerca, text=info_text, justify="center", wraplength=500, padx=20, pady=20)
        info_label.grid(column=0, row=2, rowspan=2, padx=20, pady=20, sticky="nsew")
        info_label2 = tk.Label(frame_acerca, text=funcionalidades, justify="left", wraplength=500, padx=20, pady=20)
        info_label2.grid(column=0, row=5, rowspan=4, padx=20, pady=20, sticky="nsew")
        info_label3 = tk.Label(frame_acerca, text=mensaje_final, justify="center", wraplength=500, padx=20, pady=20)
        info_label3.grid(column=0, row=10, rowspan=2, padx=20, pady=20, sticky="nsew")

        frame_acerca.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize()
    root.iconbitmap("img/f1.ico")
    app = MenuApp(root)

    # COMIENZO PRUEBA
    Serializado.crearObjetos()
    # FIN PRUEBA

    sk.set_theme("dark")
    root.mainloop()
