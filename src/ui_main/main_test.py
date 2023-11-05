import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def create_option_frame(container, label_text):
    frame = tk.Frame(container)
    label = tk.Label(frame, text=label_text)
    label.pack()
    return frame

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

# This is where the magic happens
# sk.set_theme("dark")  # You can enable the theme if you have it

# Create a main frame
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a menu
menu = tk.Menu(window)

# Submenu frames
submenu_frames = {}

def select_option(option):
    for frame_name, frame in submenu_frames.items():
        if frame_name == option:
            show_frame(frame)

# Sub menu
archivo = tk.Menu(menu, tearoff=False)
archivo.add_command(label='Aplicacion', command=lambda: select_option('Aplicacion'))
archivo.add_command(label='Salir', command=lambda: select_option('Salir'))
menu.add_cascade(label='Archivo', menu=archivo)

# Procesos y Consultas
procesos_consultas = tk.Menu(menu, tearoff=False)
procesos_consultas.add_command(label='Preparar Nuevo Campeonato', command=lambda: select_option('Preparar Nuevo Campeonato'))
procesos_consultas.add_command(label='Crear Campeonato', command=lambda: select_option('Crear Campeonato'))
procesos_consultas.add_separator()
procesos_consultas.add_command(label='Personalizar Vehículo de Carreras', command=lambda: select_option('Personalizar Vehículo de Carreras'))
procesos_consultas.add_command(label='Forjar Alianza con el Maestro de Carreras', command=lambda: select_option('Forjar Alianza con el Maestro de Carreras'))
procesos_consultas.add_command(label='Poner a Prueba tus Habilidades en la Pista', command=lambda: select_option('Poner a Prueba tus Habilidades en la Pista'))
menu.add_cascade(label='Procesos y Consultas', menu=procesos_consultas)

# Ayuda
ayuda = tk.Menu(menu, tearoff=False)
ayuda.add_command(label='Acerca de', command=lambda: select_option('Acerca de'))
menu.add_cascade(label='Ayuda', menu=ayuda)

window.configure(menu=menu)

# Create frames for each submenu option
for option in ['Aplicacion', 'Salir', 'Preparar Nuevo Campeonato', 'Crear Campeonato', 'Personalizar Vehículo de Carreras', 'Forjar Alianza con el Maestro de Carreras', 'Poner a Prueba tus Habilidades en la Pista', 'Acerca de']:
    submenu_frames[option] = create_option_frame(main_frame, option)

# Show the initial frame (Aplicacion)
show_frame(submenu_frames['Aplicacion'])

# Run the application
window.mainloop()
