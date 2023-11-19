from tkinter import messagebox

from src.excepciones.ExceptionTypeA import ExceptionTypeA


class RepeatedSelectionException(ExceptionTypeA):
    def __init__(self, selected):
        super().__init__("Ya se ha hecho la seleccion: {}".format(str(selected)))
        self.selected = selected

        messagebox.showerror("Error en la Seleccion",
                             "Ya has hecho la seleccion: {}.\nPor favor, elige otra opcion.".format(self.selected))
