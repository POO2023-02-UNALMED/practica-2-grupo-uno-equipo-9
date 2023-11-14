import tkinter as tk
import sv_ttk as sk


class FieldFrame(tk.Frame):

    def __init__(self, parent, color, nombre_proceso="", descripcion=""):
        super().__init__(parent)
        self.config(bg=None, width=1200, height=600)
        self.nombre_proceso = nombre_proceso
        self.descripcion = descripcion

        # Create labels for the title and description
        title_label = tk.Label(self, text=nombre_proceso, font=("Helvetica", 16), anchor="center")
        description_label = tk.Label(self, text=descripcion, anchor="center")

        # Use grid to make labels span the same width as the window
        title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        description_label.grid(row=1, column=0, columnspan=2, padx=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class MenuApp:
    def __init__(self, root):
        self.menu_bar = None
        self.root = root
        self.root.title("Menu App")
        self.root.geometry("1200x600")
        sk.set_theme("dark")
        self.frames = {}  # Dictionary to store frames

        self.create_frames()
        self.create_menu()

    def create_frames(self):
        self.frames["app"] = FieldFrame(self.root, None, "Aplicacion", "Bienvenido a la aplicacion de GP Racing")
        self.frames["preparar_campeonato"] = FieldFrame(self.root, None)
        self.frames["crear_campeonato"] = FieldFrame(self.root, None)
        self.frames["personalizar_vehiculo"] = FieldFrame(self.root, None)
        self.frames["forjar_alianza"] = FieldFrame(self.root, None)
        self.frames["gp_racing"] = FieldFrame(self.root, None)
        self.frames["acerca_de"] = FieldFrame(self.root, None)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # sub menu archivo
        archivo = tk.Menu(self.menu_bar, tearoff=0)
        archivo.add_command(label='Aplicacion', command=lambda: self.change_frame('app'))
        archivo.add_command(label='Salir', command=self.root.quit)
        self.menu_bar.add_cascade(label='Archivo', menu=archivo)

        # sub menu procesos y consultas
        procesos_consultas = tk.Menu(self.menu_bar, tearoff=False)
        procesos_consultas.add_command(label='Preparar Nuevo Campeonaro',
                                       command=lambda: self.change_frame('preparar_campeonato'))
        procesos_consultas.add_command(label='Crear de Campeonato',
                                       command=lambda: self.change_frame('crear_campeonato'))
        procesos_consultas.add_separator()
        procesos_consultas.add_command(label='Personalizar Vehiculo de Carreras',
                                       command=lambda: self.change_frame('personalizar_vehiculo'))
        procesos_consultas.add_command(label='Forjar Alianza con el Maestro de Carreras',
                                       command=lambda: self.change_frame('forjar_alianza'))
        procesos_consultas.add_command(label='GP Racing',
                                       command=lambda: self.change_frame('gp_racing'))
        self.menu_bar.add_cascade(label='Procesos y Consultas', menu=procesos_consultas)

        # sub menu ayuda
        ayuda = tk.Menu(self.menu_bar, tearoff=False)
        ayuda.add_command(label='Acerca de', command=lambda: self.change_frame('acerca_de'))
        self.menu_bar.add_cascade(label='Ayuda', menu=ayuda)

    def change_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
    sk.set_theme("dark")

