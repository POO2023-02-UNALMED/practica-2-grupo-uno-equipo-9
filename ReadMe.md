
# Project Structure of the Fédération Internationale de l'Automobile 

## Instalar

Primero abran el cmd y ecriben esto:

1. python -m venv poo
2. poo\Scripts\activate
3. pip install sv_ttk

## Nombre de variables

Certainly! Here's a quick cheat sheet for Python naming conventions:

**Variable:**
- `variable_name`
- Format: snake_case

**Function:**
- `function_name`
- Format: snake_case

**Constant:**
- `CONSTANT_NAME`
- Format: UPPERCASE_WITH_UNDERSCORES

**Module:**
- `module_name`
- Format: lowercase

**Class:**
- `ClassName`
- Format: CamelCase

**Method:**
- `method_name`
- Format: snake_case

**Private Variable:**
- `_private_var`
- Starts with a single underscore

**Protected Variable:**
- `_protected_var`
- Starts with a single underscore

**Private Method:**
- `_private_method`
- Starts with a single underscore

**Protected Method:**
- `_protected_method`
- Starts with a single underscore

**Package:**
- `package_name`
- Format: lowercase


Remember to make your names descriptive and meaningful to enhance code readability and maintainability. For more detailed guidance, you can refer to PEP 8, the official Python style guide.


## Tkinter Cheatsheet

### Tkinter Cheat Sheet


```python
import tkinter as tk
from tkinter import messagebox as messagebox
from tkinter import filedialog as filedialog
from tkinter import colorchooser as colordialog
```

### Create a root window
```python
root = tk.Tk()
```

### Create a Label
```python
label = tk.Label(root, text="Hello, Tkinter")
```
### Place widgets using grid
```python
label.grid(row=0, column=0)
```
### Create a Button
```python
button = tk.Button(root, text="Click Me")
```
### Place widgets using pack
```python
button.pack()
```
### Create an Entry widget
```python
entry = tk.Entry(root)
```
### Get and set text in Entry
```python
text = entry.get()
entry.insert(0, "Default Text")
```
### Create a Frame
```python
frame = tk.Frame(root)
```
### Create a Canvas
```python
canvas = tk.Canvas(root, width=200, height=100)
```
### Create a Checkbutton
```python
checkbutton = tk.Checkbutton(root, text="Check me")
```
### Create a Radiobutton
```python
radiobutton = tk.Radiobutton(root, text="Option 1")
```
### Create a Scale
```python
scale = tk.Scale(root, from_=0, to=10, orient="horizontal")
```
### Create a Listbox
```python
listbox = tk.Listbox(root)
```
### Insert items into Listbox
```python
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
```
### Create a Menu
```python
menu = tk.Menu(root)
```
### Add items to Menu
```python
menu.add_command(label="File")
menu.add_command(label="Edit")
```
### Create a Text widget
```python
text_widget = tk.Text(root, width=30, height=10)
```
### Insert text into Text widget
```python
text_widget.insert(tk.END, "Hello, Tkinter!")
```
### Create a Scrollbar
```python
scrollbar = tk.Scrollbar(root)
```
### Link the Scrollbar to the Text widget
```python
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)
```
### Create a Toplevel window
```python
top_window = tk.Toplevel(root)
```
### Create a Message Box
```python
messagebox.showinfo("Info", "This is an info message")
```
### Create an Image
```python
photo = tk.PhotoImage(file="image.gif")
```
### Create a Label with an image
```python
image_label = tk.Label(root, image=photo)
```
### Create a File Dialog
```python
filedialog.askopenfilename()
```
### Create a Color Dialog
```python
colordialog.askcolor()
```
### Bind a function to an event
```python
def on_button_click(event):
    print("Button clicked!")
```
button.bind("<Button-1>", on_button_click)

### Start the main loop
```python
root.mainloop()
```