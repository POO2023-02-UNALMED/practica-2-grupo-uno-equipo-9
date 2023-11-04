import tkinter as tk
from tkinter import ttk

import sv_ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')


# This is where the magic happens
sv_ttk.set_theme("dark")


# menu
menu = tk.Menu(window)

# sub menu
archivo = tk.Menu(menu, tearoff = False)
archivo.add_command(label ='Aplicacion', command = lambda: print('Aplicacion'))
archivo.add_command(label ='Salir', command = lambda: print('Salir'))
menu.add_cascade(label = 'Archivo', menu = archivo)

procesos_consultas = tk.Menu(menu, tearoff = False)
procesos_consultas.add_command(label = 'Preparar Nuevo Campeonaro', command = lambda: print('Aplicacion'))
procesos_consultas.add_command(label = 'Crear de Campeonato', command = lambda: print('Salir'))
procesos_consultas.add_separator()
procesos_consultas.add_command(label = 'Personalizar Vehiculo de Carreras', command = lambda: print('Salir'))
procesos_consultas.add_command(label = 'Forjar Alianza con el Maestro de Carreras', command = lambda: print('Salir'))
procesos_consultas.add_command(label = 'Poner a Prueba tus Habilidades en la Pista', command = lambda: print('Salir'))

menu.add_cascade(label = 'Procesos y Consultas', menu = procesos_consultas)

ayuda = tk.Menu(menu, tearoff = False)
ayuda.add_command(label = 'Acerca de', command = lambda: print('Aplicacion'))

menu.add_cascade(label = 'Ayuda', menu = ayuda)

window.configure(menu = menu)



# run
window.mainloop()