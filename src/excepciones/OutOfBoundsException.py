from tkinter import messagebox

from src.excepciones.ExceptionTypeA import ExceptionTypeA


class OutOfBoundsException(ExceptionTypeA):
    def __init__(self, lim_inf, lim_sup, *args):
        super().__init__("Se ha ingresado un dato por fuera de los limites [{},{}]".format(str(lim_inf), str(lim_sup)))
        self.lim_inf = str(lim_inf)
        self.lim_sup = str(lim_sup)

        messagebox.showerror("Error en la Seleccion",
                             "Valor fuera del rango de seleccion.\nPor favor, ingresa un entero entre {} y {}.".format(
                                 self.lim_inf, self.lim_sup))


