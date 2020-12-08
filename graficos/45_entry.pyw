# Entries: Aplica lo mismo que para los labels
# Método grid() para colocar componentes

from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()


# NOMBRE
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=5, pady=5)
#nombreLabel.place(x=100, y=100)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
#cuadroNombre.place(x=100, y=100)
cuadroNombre.config(fg="red", justify="center")


# PASS
passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=5, pady=5)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=5, pady=5)
cuadroPass.config(show="*")  # Show "*" instead of the password


# APELLIDO
apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=5, pady=5)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=5, pady=5)


# DIRECCION
direccionLabel = Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=5, pady=5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=5, pady=5)


root.mainloop()
