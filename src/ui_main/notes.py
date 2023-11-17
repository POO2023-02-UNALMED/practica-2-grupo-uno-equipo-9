def planificar_calendario(self, frame_name):
    # Metodos importantes para la funcionalidad
    # Para frame 1

    def elegir_campeonato():
        global circuitos_para_elegir, campeonato_elegido, directores_para_elegir, cantidad_carreras
        campeonato_elegido = campeonatos_desbloqueados[int(entry1.get()) - 1]
        print(campeonato_elegido.getNombre())
        tk.messagebox.showinfo("Eleccion realizada", "Has escogido el campeonato " + campeonato_elegido.getNombre())
        cantidad_carreras = campeonato_elegido.getCantidadMaxCarreras()
        circuitos_para_elegir = Circuito.circuitos_ubicacion(campeonato_elegido)
        directores_para_elegir = DirectorCarrera.dc_disponibles()

        # Coloca los directores disponibles
        jj = 1
        for dir in directores_para_elegir:
            listbox2.insert(jj, str(jj) + " | " + dir.getNombre())
            jj += 1

        Ciudad.ciudades_continente(campeonato.getContinente())

        # Pasar al siguiente frame
        frame1.grid_remove()
        frame1.grid_forget()
        frame2.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        frame2.tkraise()

    # Para frame 2
    def elegir_director():
        global circuitos_presupuesto, circuitos_para_elegir, directores_para_elegir, director_elegido, meses_disponibles, dificultad
        director_elegido = directores_para_elegir[int(entry1.get()) - 1]
        print(director_elegido.getNombre())
        tk.messagebox.showinfo("Eleccion realizada", "Has escogido el director " + campeonato_elegido.getNombre())

        circuitos_presupuesto = Circuito.circuitos_vender(circuitos_para_elegir, director_elegido)

        # Pasar al siguiente frame
        frame2.grid_remove()
        frame2.grid_forget()
        frame3.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        frame3.tkraise()

    # Para frame 3
    def elegir_mes(value):
        global mes_seleccionado, meses_disponibles, mes_elegido
        mes_elegido = int(value)

    def elegir_dificultad(value):
        global dificultad_seleccionada, dificultad_elegida
        dificultades_dict = {1: "Facil", 2: "Medio", 3: "Dificil"}
        dificultad_elegida = dificultades_dict[int(value)]

    def elegir_ciudad(value):
        global ciudad_seleccionada, ciudad_elegida
        ciudad_nombre = value
        ciudad_elegida = [ciudad for ciudad in ciudades_disponibles if ciudad.get_nombre() == ciudad_nombre][0]

    def elegir_mes_dificultad():
        global dificultad_elegida, mes_elegido, circuitos_carrera, circuitos_presupuesto, circuitos_para_elegir, meses_disponibles, dificultad, ciudad_elegida
        meses_disponibles.remove(mes_elegido)
        tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de dificultad y mes")

        circuitos_carrera = Circuito.circuitos_disponibles(mes_elegido, circuitos_presupuesto)
        jj = 1
        for circuito in circuitos_carrera:
            listbox5.insert(jj, str(jj) + " | " + circuito.get_nombre())
            jj += 1

        # Pasar al siguiente frame
        frame4.grid_remove()
        frame4.grid_forget()
        frame5.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        frame5.tkraise()

    # Para frame 4
    def confirmar_equipos():
        global campeonato_elegido, equipo_elegido, participantes, pilotos_equipo
        tk.messagebox.showinfo("Eleccion realizada", "Has confirmado la seleccion de equipos")
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
        tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos pilotos de tu equipo")
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
        tk.messagebox.showinfo("Eleccion realizada", "Has elegido a ambos patrocinadores de tu equipo")

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

    # Frame 1: Escoger Campeonato
    frame1 = FieldFrame(self.frames[frame_name], None, "Elegir un Campeonato de los disponibles",
                        "Primero, elige el campeonato que quieres planificar")
    frame1.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)
    frame1.grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
    # Componentes del frame
    listbox1 = tk.Listbox(frame1)
    ii = 1
    campeonatos_desbloqueados = Campeonato.campeonatosDesbloqueados()
    print(campeonatos_desbloqueados)

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
    # Guardando el continente
    campeonato = None
    # Circuitos para elegir
    circuitos_para_elegir = []
    cantidad_carreras = 0
    # Ciudades disponibles
    print(campeonato.getContinente())
    ciudades_disponibles = None
    print(cantidad_carreras)

    carreras = []

    # Frame 2: Escoger Director de Carrera
    frame2 = FieldFrame(self.frames[frame_name], None, "Elige un Director de Carrera",
                        "De los directores disponibles, elige uno para que dirija las carrera que estas preparando")
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
    # Campeonato elegido
    director_elegido = None
    # Circuitos disponibles para el director
    circuitos_presupuesto = []
    # Meses Carreras
    meses_carreras = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # Dificultad
    dificultades = ["Principiante", "Intermedio", "Experto"]

    # Frame 3: Escoger Mes y dificultad
    frame3 = FieldFrame(self.frames[frame_name], None, "Escoge la dificultad y el mes de la carrera",
                        "Estos son los meses en los que puedes correr.\nEscoge uno y la dificultad de la carrera")
    frame3.configure(highlightbackground="GRAY", highlightcolor="WHITE", highlightthickness=1)

    # Componentes del frame
    mes_seleccionado = tk.StringVar(frame3)
    mes_seleccionado.set(meses_carreras[0])
    mes_elegido = None
    dropdown_meses = tk.OptionMenu(frame3, mes_seleccionado, *meses_carreras, command=elegir_mes())
    dropdown_meses.grid(column=0, row=3, rowspan=3, padx=20, pady=20, sticky="nsew")
    dropdown_meses.configure(justify="center")
    dificultad_elegida = 1
    dificultad_seleccionada = tk.StringVar(frame3)
    dificultad_seleccionada.set(dificultades[0])
    dropdown_dificultad = tk.OptionMenu(frame3, dificultad_seleccionada, *dificultades, command=elegir_dificultad())
    dropdown_dificultad.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
    dropdown_dificultad.configure(justify="center")
    ciudad_elegida = None
    ciudades_nombres = [ciudad.get_nombre() for ciudad in ciudades_disponibles]
    ciudad_seleccionada = tk.StringVar(frame3)
    ciudad_seleccionada.set(ciudades_nombres[0])
    dropdown_ciudad = tk.OptionMenu(frame3, ciudad_seleccionada, *ciudades_nombres,
                                    command=elegir_ciudad())
    dropdown_ciudad.grid(column=0, row=4, rowspan=3, padx=20, pady=20, sticky="nsew")
    dropdown_ciudad.configure(justify="center")

    button3 = tk.Button(frame3, text="Elegir", command=lambda: elegir_mes_dificultad())
    button3.grid(column=0, row=7, padx=20, pady=20)
    button3.configure(justify="center")
    # El equipo que elige el usuario
    equipo_elegido = None
    # Equipos totales
    participantes = []
    # Pilotos del equipo
    pilotos_equipo = []

    # Frame 4: Escoger Circuito
    frame4 = FieldFrame(self.frames[frame_name], None, "Elegir Circuito",
                        "Estos son los circuitos disponibles en el mes que elegiste y con el presupuesto que tiene el director seleccionado.\nEscoge uno!")
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

