from tkinter import messagebox

from src.excepciones.ExceptionTypeB import ExceptionTypeB


class NoInputException(ExceptionTypeB):
    def __init__(self, text, missing_fields):
        super().__init__("Hay campos de entrada vacios.")
        self.missing_fields_string = ""
        for field in missing_fields:
            self.missing_fields_string += "\n*{}".format(field)
        self.mensaje = ("Hay campos de seleccion por llenar.\nPor favor, llena los siguientes campos: "
                        + self.missing_fields_string)
        messagebox.showerror("Error en los Campos de Seleccion",
                             self.mensaje)
