#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

from tkinter import *
from tkinter import ttk

root = Tk()
opcion = StringVar().set(None)

Label(root, text="Esta es la lista de elementos:").pack()
r1 = ttk.Radiobutton(root, text="Boton 1", variable=opcion, value="1").pack()
r2 = ttk.Radiobutton(root, text="Boton 2", variable=opcion, value="2").pack()
r3 = ttk.Radiobutton(root, text="Boton 3", variable=opcion, value="3").pack()

root.mainloop()

#otra forma:

from tkinter import *

master = Tk()
elemento = StringVar()

listbox = Listbox(master)

for item in ["Pepe", "María", "Ernesto", "Ruben", "Carlos", "Laura", "Ana", "Lorena"]:
 listbox.insert(END, item)

listbox.pack()

label = Label(text="Lista de nombres de personas")
label.pack()

master.mainloop()