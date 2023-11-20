import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk as sk
ventana = tk.Tk()
ventana.title("Ventana de inicio")
ventana.geometry("1280x800")

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
    ventana.destroy()

def descripcion():
    messagebox.showinfo("Descripcion de la aplicacion","El " "Proyecto de la Fédération Internationale de l'Automobile" "es una aplicación desarrollada bajo el paradigma de Programación Orientada a Objetos que se enfoca en la gestión integral de un campeonato de carreras automovilísticas.")


#menu
menu = tk.Menu(ventana,tearoff=0)
ventana.config(menu= menu)

menuInicio = tk.Menu(menu)
menu.add_cascade(label="Inicio", menu= menuInicio)


menuInicio.add_command(label = "Salir", command= salirApp)
menuInicio.add_command(label = "Descripción", command= descripcion)



mensaje = ("¡Bienvenido a nuestro simulador de carreras de la\n Fédération Internationale de l'Automobile,\n"
           "donde podrás experimentar la emoción de competir en carreras \n"
           "de Fórmula 1 como nunca antes!")

# mesaje bienvenida
mensaje1 = tk.Label(frameP3,
                    text=mensaje,
                    justify=tk.CENTER,
                    font='Times 15',
                    relief="solid",
                    bd=2.5
                    )
mensaje1.place(relx=0.5, rely=0.5, relwidth=0.98, relheight=0.98, anchor="center")





#Fotos proyecto
fotoCarro = tk.PhotoImage(file="fotosInicio/carrof1.png")
fotoBanderas = tk.PhotoImage(file= "fotosInicio/banderas.png")
fotoLogo = tk.PhotoImage(file= "fotosInicio/logo.png")
fotoPiloto = tk.PhotoImage(file= "fotosInicio/piloto.png")
fotoCircuito = tk.PhotoImage(file= "fotosInicio/circuito.png")
#Fotos Mariana
fotoMariana1 = tk.PhotoImage(file="fotosInicio/Mariana1.png")
fotoMariana2 = tk.PhotoImage(file="fotosInicio/Mariana2.png")
fotoMariana3 = tk.PhotoImage(file="fotosInicio/Mariana3.png")
fotoMariana4 = tk.PhotoImage(file="fotosInicio/Mariana4.png")
#Fotos David
fotoDavid1 = tk.PhotoImage(file="fotosInicio/David1.png")
fotoDavid2 = tk.PhotoImage(file="fotosInicio/David2.png")
fotoDavid3 = tk.PhotoImage(file="fotosInicio/David3.png")
fotoDavid4 = tk.PhotoImage(file="fotosInicio/David4.png")
#Fotos Samuel
fotoSamuel1 = tk.PhotoImage(file="fotosInicio/Samuel1.png")
fotoSamuel2 = tk.PhotoImage(file="fotosInicio/Samuel2.png")
fotoSamuel3 = tk.PhotoImage(file="fotosInicio/Samuel3.png")
fotoSamuel4 = tk.PhotoImage(file="fotosInicio/Samuel4.png")
#Fotos Juan
fotoJuan1 = tk.PhotoImage(file="fotosInicio/Juan1.png")
fotoJuan2 = tk.PhotoImage(file="fotosInicio/Juan2.png")
fotoJuan3 = tk.PhotoImage(file="fotosInicio/Juan3.png")
fotoJuan4 = tk.PhotoImage(file="fotosInicio/Juan4.png")
#Fotos Santiago
fotoSantiago1 = tk.PhotoImage(file="fotosInicio/Santiago1.png")
fotoSantiago2 = tk.PhotoImage(file="fotosInicio/Santiago2.png")
fotoSantiago3 = tk.PhotoImage(file="fotosInicio/Santiago3.png")
fotoSantiago4 = tk.PhotoImage(file="fotosInicio/Santiago4.png")




def cambiarFoto(event):
    if BotonP4["text"]== "1":
        BotonP4.config(image= fotoBanderas, text="2")
    elif BotonP4["text"]== "2":
        BotonP4.config(image= fotoCarro, text="3")
    elif BotonP4["text"]== "3":
        BotonP4.config(image= fotoPiloto, text="4")
    elif BotonP4["text"]== "4":
        BotonP4.config(image= fotoLogo, text="5")
    elif BotonP4["text"]== "5":
        BotonP4.config(image= fotoCircuito, text="1")

#imagenes cambiantes con acercar el mouse
BotonP4 = tk.Button(frameP4, image=fotoLogo,text="1",relief="solid", bd=2.5)
BotonP4.bind("<Enter>",cambiarFoto)
BotonP4.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.75, anchor="s")
#boton ingresar
botonIngresar = tk.Button(frameP4, text="Ingresar", font='Times 15', width=30, height=2,relief="solid", bd=2.5)
botonIngresar.pack(side='bottom', pady=10)

#hojas de vida
david = """Soy David Toro, estudiante de Ingeniería de Sistemas, con conocimientos en lenguajes como Python y Java. Apasionado por el desarrollo web y de videojuegos, estoy enfocado en ampliar mi experiencia en estas áreas.
\nclic para cambiar"""

david = '\n'.join(david[i:i+81] for i in range(0, len(david), 81))


samuel= """Soy Samuel Mira,"I love you, this world, and everyone in it!" Programador novicio, prospecto en Java y Python. Estudiante de Ciencias de la Computación, siempre maravillado con todo lo que hay por descubrir. Todos los dias son buenos dias para aprender
"""

samuel = '\n'.join(samuel[i:i+81] for i in range(0, len(samuel), 81))

mariana ="""Soy Mariana Valencia Cubillos, estudiante de Ciencias de la Computación y apasionada por la inteligencia artificial. Con amplia experiencia en programación (Java, Python, Scala, HTML) y enfoque en Power Apps, Power BI y SSIS como freelancer, mi interés se centra en la automatización de procesos. Encuentro satisfacción en la innovación y la aplicación creativa de la tecnología para resolver problemas cotidianos.
\nclic para cambiar"""

# Agregar salto de línea cada 81 caracteres
mariana = '\n'.join(mariana[i:i+81] for i in range(0, len(mariana), 81))


santiago = """Soy Santiago López Ayala, estudiante de Ingeniería de Sistemas, entusiasta de la tecnología y todo lo relacionado con el espacio. Poseo conocimientos sólidos en Java y Python, y estoy comprometido con el constante aprendizaje y desarrollo en el campo de la ingeniería informática.
\nclic para cambiar"""

santiago = '\n'.join(santiago[i:i+81] for i in range(0, len(santiago), 81))

juan = """Soy Juan Andrés Jiménez Vélez, estudiante de Ingeniería de Sistemas e Informática y técnico en electricidad y electrónica. Tengo conocimientos de programación con los lenguajes Python y Java, y del desarrollo de aplicaciones web con Angular. Mi experiencia abarca el trabajo en instalaciones eléctricas residenciales. Me considero una persona con una gran capacidad para aprender y resolver problemas de manera eficiente.
\nclic para cambiar"""

juan = '\n'.join(juan[i:i+81] for i in range(0, len(juan), 81))


def cambiarTexto():
    if hojasDeVida["text"]== david:
        inner_frame_David.pack_forget()
        inner_frame_Samuel.pack()
        hojasDeVida.config (text= samuel)

    elif hojasDeVida["text"]== samuel:
        inner_frame_Samuel.pack_forget()
        inner_frame_Mariana.pack()
        hojasDeVida.config (text= mariana)

    elif hojasDeVida["text"]== mariana:
        inner_frame_Mariana.pack_forget()
        inner_frame_Juan.pack()

        hojasDeVida.config (text= juan)

    elif hojasDeVida["text"] == juan:

        inner_frame_Juan.pack_forget()
        inner_frame_Santiago.pack()

        hojasDeVida.config(text=santiago)

    elif hojasDeVida["text"] == santiago:
        inner_frame_Santiago.pack_forget()
        inner_frame_David.pack()

        hojasDeVida.config(text=david)



# hojas de vida
tituloHojasDeVida = tk.Label(frameP5, text="Breve hoja de vida", font='Times 13', relief="solid", bd=2.5)
tituloHojasDeVida.place (relx=0.5, rely=0.21, relwidth=0.98, relheight=0.2, anchor="s")

hojasDeVida = tk.Button(frameP5, width=50, height=2, text=david, font='Times 13', relief="solid", bd=2.5, command=cambiarTexto)
hojasDeVida.place(relx=0.5, rely=0.1899, relwidth=0.98, relheight=0.8, anchor="n")




# fotos


#crear los arreglos de las fotos 4x4
def create_inner_frame_David(parent_frame):

    inner_frame = tk.Frame(parent_frame)

    imagenes = [fotoDavid1,fotoDavid2,fotoDavid3,fotoDavid4]

    for i in range (2):
        for j in range (2):
            imagen_label = tk.Label(inner_frame, image= imagenes[i*2 + j], width= 230, height=230,relief="solid", bd=2.5)
            imagen_label.grid(row = i, column = j , padx = 5, pady =5)

    return inner_frame



def create_inner_frame_Mariana(parent_frame):
    inner_frame = tk.Frame(parent_frame)

    imagenes = [fotoMariana1, fotoMariana2, fotoMariana4, fotoMariana3]

    for i in range(2):
        for j in range(2):
            imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230, relief="solid",
                                    bd=2.5)
            imagen_label.grid(row=i, column=j, padx=5, pady=5)

    return inner_frame

def create_inner_frame_Samuel(parent_frame):
    inner_frame = tk.Frame(parent_frame)

    imagenes = [fotoSamuel1,fotoSamuel2,fotoSamuel3,fotoSamuel4]

    for i in range(2):
        for j in range(2):
            imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230, relief="solid",
                                    bd=2.5)
            imagen_label.grid(row=i, column=j, padx=5, pady=5)

    return inner_frame

def create_inner_frame_Juan(parent_frame):
    inner_frame = tk.Frame(parent_frame)

    imagenes = [fotoJuan1,fotoJuan2,fotoJuan3,fotoJuan4]

    for i in range(2):
        for j in range(2):
            imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230, relief="solid",
                                    bd=2.5)
            imagen_label.grid(row=i, column=j, padx=5, pady=5)

    return inner_frame

def create_inner_frame_Santiago(parent_frame):
    inner_frame = tk.Frame(parent_frame)

    imagenes = [fotoSantiago1,fotoSantiago2,fotoSantiago3,fotoSantiago4]

    for i in range(2):
        for j in range(2):
            imagen_label = tk.Label(inner_frame, image=imagenes[i * 2 + j], width=230, height=230, relief="solid",
                                    bd=2.5)
            imagen_label.grid(row=i, column=j, padx=5, pady=5)

    return inner_frame


#crea Frames con fotos
inner_frame_David = create_inner_frame_David(frameP6)
#ubicar primer Frame
inner_frame_David.pack()

inner_frame_Mariana = create_inner_frame_Mariana(frameP6)
inner_frame_Samuel = create_inner_frame_Samuel(frameP6)
inner_frame_Juan = create_inner_frame_Juan(frameP6)
inner_frame_Santiago =create_inner_frame_Santiago(frameP6)




sk.set_theme("dark")

ventana.mainloop()
