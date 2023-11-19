# Imports de paquetes
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

import sv_ttk as sk

# Imports de las clases
from src.gestor_aplicacion.campeonato import Campeonato
from src.gestor_aplicacion.paddock.Circuito import Circuito
from src.gestor_aplicacion.ubicaciones.Continente import Continente
from src.excepciones.ExceptionTypeB import ExceptionTypeB
from src.excepciones.IncorrectTypeException import IncorrectTypeException
from src.excepciones.NoInputException import NoInputException
from src.excepciones.NullPointerException import NullPointerException
from src.excepciones.OutOfBoundsException import OutOfBoundsException

class ExampleClass():
    def __init__(self):
        pass


def get_entry():
    try:
        data = entry.get()
        if data == "" or selection1 is None or selection2 is None:
            missing_fields = []
            if data == "":
                missing_fields += ["Numero"]
            if selection1 is None:
                missing_fields += ["Seleccion de Numero"]
            if selection2 is None:
                missing_fields += ["Seleccion de Color"]
                raise NoInputException("", missing_fields)
        print(int(data) / 2)
        print(list3[int(data)])
        print(selection1)
        print(selection2)
    except NoInputException:
        pass
    except IndexError:
        raise OutOfBoundsException(0, len(list3)-1)
    except ValueError:
        raise IncorrectTypeException("numero")


def choose1(E):
    global selection1
    selection1 = combobox1.get()


def choose2(E):
    global selection2
    selection2 = combobox2.get()


root = tk.Tk()
entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
button = tk.Button(root, text="Send", command=get_entry)
button.grid(row=4, column=0, padx=5, pady=5)
list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
selection1 = None
list2 = ["Green", "Blue", "Red", "Porpol"]
selection2 = None
sk.set_theme("dark")
list3 = ["Triangle", "Square"]

seleccion1 = tk.StringVar(root)
seleccion2 = tk.StringVar(root)
# Create Combobox for month selection
combobox1 = ttk.Combobox(root, values=list1)
combobox1.grid(column=0, row=2, padx=20, pady=20)
combobox1.bind("<<ComboboxSelected>>", choose1)
combobox1.configure(justify="center")
combobox2 = ttk.Combobox(root, values=list2)
combobox2.grid(column=0, row=3, padx=20, pady=20)
combobox2.bind("<<ComboboxSelected>>", choose2)
combobox2.configure(justify="center")

try:
    example = None
    print(example.number())
except AttributeError:
    raise NullPointerException("ExampleClass")


root.mainloop()
