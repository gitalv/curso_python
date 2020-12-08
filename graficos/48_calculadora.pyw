# Aplicación calculadora

from tkinter import *


root = Tk()

miFrame = Frame(root)
miFrame.pack()

# ------------- PANTALLA ---------------------------
numeroPantalla = StringVar()
numeroPantalla.set("0")

pantalla = Entry(miFrame, text="0", textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  # columnspan es porque los botones crean 4 columnas, y la pantalla quiero que abarque esas 4 columnas
pantalla.config(background="black", fg="#03f943", justify="right")

# ------------- PULSACIONES TECLADO ---------------
def numeroPulsado(num):
	current = numeroPantalla.get()
	if current == "0" and num == "0":  # No concatenar varios 0 a la izquierda
		return
	numeroPantalla.set(numeroPantalla.get() + num)

# ------------- FILA 1 ---------------------------
boton7 = Button(miFrame, text="7", width=5, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=5, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=5, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=5)
botonDiv.grid(row=2, column=4)

# ------------- FILA 2 ---------------------------
boton4 = Button(miFrame, text="4", width=5, command=lambda:numeroPulsado("4"))  # Si no se pone lambda, se ejecuta la funcion al llegar aquí, y sólo esa vez
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=5, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=5, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=5)
botonMult.grid(row=3, column=4)

# ------------- FILA 3 ---------------------------
boton1 = Button(miFrame, text="1", width=5, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=5, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=5, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=5)
botonRest.grid(row=4, column=4)

# ------------- FILA 4 ---------------------------
boton0 = Button(miFrame, text="0", width=5, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=5, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=5)
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=5)
botonSum.grid(row=5, column=4)


root.mainloop()
