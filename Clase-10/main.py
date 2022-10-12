import tkinter
import pprint

#LABEL
window = tkinter.Tk()
label_saludo = tkinter.Label(window, text="hola", bg="yellow", fg="blue").pack(ipadx=30, ipady=30, fill='x', side="left")

label_adios = tkinter.Label(window, text="adios", bg="purple", fg="white")
label_adios.pack(ipadx=30, ipady=30, fill='y', expand=True, side='right')

label3 = tkinter.Label(window, text="label3", bg="blue", fg="white")
label3.pack(ipadx=50, ipady=15)

label4 = tkinter.Label(window, text="label4", bg="red", fg="white")
label4.pack(ipadx=15, ipady=15, side='left')

window.mainloop()


#GRID
from tkinter import ttk

window1 = tkinter.Tk()
window1.columnconfigure(0, weight=1)
window1.columnconfigure(1, weight=3)

username_label = ttk.Label(window1, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window1)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

password_label = ttk.Label(window1, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window1, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window1, text="Log In")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window1.mainloop()

#PLACE
window2 = tkinter.Tk()
#posicionamiento absoluto
label6 = tkinter.Label(window2, text="Posicionamiento Absoluto", bg="blue", fg="white")
label6.place(x=10, y=50)

#posicionamiento relativo
label7 = tkinter.Label(window2, text="Otro mas", bg="red", fg="yellow")
label7.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')

window2.mainloop()

#FRAMES: se usan para agrupar cosas
window3 = tkinter.Tk()

window3.columnconfigure(0, weight=1)
window3.columnconfigure(1, weight=3)

frame = ttk.Frame(window3)
frame.grid(column=0, row=0, sticky=tkinter.W)

label8 = ttk.Label(frame, text="hola")
label8.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)


window3.mainloop()

#LIST BOX
window4 = tkinter.Tk()
selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window4, text="si", value="1", variable=selected)
r2 = ttk.Radiobutton(window4, text="no", value="2", variable=selected)
r3 = ttk.Radiobutton(window4, text="quiza", value="3", variable=selected)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)

window4.mainloop()

#CHECK

window5 = tkinter.Tk()

window5.columnconfigure(0, weight=1)
window5.columnconfigure(1, weight=3)

def mifuncion():
    print("clicado")

selected1 = tkinter.StringVar()

checkbox = ttk.Checkbutton(window5, text="acepto condiciones", variable=selected1, command=mifuncion)
checkbox.grid(column=0, row=0)

window5.mainloop()

# EVENTOS

window6 = tkinter.Tk()


def saludar(event):
    print("han hecho clic en saludar")

def saludardobleclick(event):
    print("han hecho doble clic en saludar")

def salir(event):
    print("Adios")
    window.quit()

boton = tkinter.Button(window6, text="haz clic")
boton.pack()
boton.bind("<Button-1>", saludar)
boton.bind("<Double-1>", saludardobleclick)

boton_salir = tkinter.Button(window6, text="salir")
boton_salir.pack()
boton_salir.bind("<Button-1>", salir)

window6.mainloop()

#MOTION

master = Tk()
texto = "demo de texto para ver movimiento de raton"
msg = Message(master, text=texto)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.bind("<Motion>", motion)
msg.pack()
mainloop()

window7 = tkinter.Tk()
filename = filedialog.askopenfilename()
window7.mainloop()