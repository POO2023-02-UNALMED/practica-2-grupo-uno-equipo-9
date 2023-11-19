from tkinter import messagebox

from src.excepciones.ExceptionTypeB import ExceptionTypeB


class NullPointerException(ExceptionTypeB):
    def __init__(self, obj_type):
        super().__init__("No se ha encontrado un objeto del tipo '{}'".format(obj_type))
        self.obj_type = obj_type

        messagebox.showerror("Error en el proceso",
                             "No se ha encontrado un objeto del tipo '{}'.".format(
                                 self.obj_type))