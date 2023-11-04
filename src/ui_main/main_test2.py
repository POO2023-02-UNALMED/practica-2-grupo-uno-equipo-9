import tkinter as tk
from tkinter import ttk

import sv_ttk

root = tk.Tk()

sv_ttk.set_theme("dark")

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')


menu = tk.Menu(window)


file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label="New", compound = tk.LEFT, accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open",  compound = tk.LEFT,  accelerator="Ctrl+O", underline=0)

for menu_item in window:
    menu_item.config(background=menu.c_bg, foreground=menu.c_fg,
                     activebackground=menu.c_sb, activeforeground=menu.c_fg,
                     selectcolor=menu.c_fg, relief=tk.FLAT, bd=0, font=menu.font)


root.mainloop()