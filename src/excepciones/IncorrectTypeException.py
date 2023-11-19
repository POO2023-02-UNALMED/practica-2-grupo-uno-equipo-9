from tkinter import messagebox

from src.excepciones.ExceptionTypeA import ExceptionTypeA


class IncorrectTypeException(ExceptionTypeA):
    def __init__(self, desired_type):
        super().__init__("Se ha ingresado un tipo de dato no deseado. Se esperaba un {}".format(str(desired_type)))
        self.desired_type = desired_type

        messagebox.showerror("Error de Tipos",
                             "Tipo de dato ingresado incorrecto.\nPor favor, ingrese un {}.".format(self.desired_type))


