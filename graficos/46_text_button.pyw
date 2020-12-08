# Texts: Large input area
# Scrollbars
# Buttons

from tkinter import *


root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()


# NOMBRE
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=5, pady=5)
#nombreLabel.place(x=100, y=100)

miNombre = StringVar()  # Cadena de caracteres. No se puede crear un StringVar() antes de crear el root

cuadroNombre = Entry(miFrame, textvariable=miNombre)  # Asocio este Entry con la variable miNombre
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
#cuadroNombre.place(x=100, y=100)
cuadroNombre.config(fg="red", justify="center")


# PASSWORD
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
direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=5, pady=5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=5, pady=5)


# COMENTARIOS
comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=5, pady=5)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, pady=5)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=1, pady=5, sticky="nse")  # El sticky en este caso es para adaptar el scrollbar al text

textoComentario.config(yscrollcommand=scrollVert.set)  # Para que la barra del scrollbar funcione bien



def codigoBoton():
	miNombre.set("Juan")  # Esta variable está asociada al Entry cuadroNombre


# BOTON
botonEnvio = Button(root, text="Enviar", command=codigoBoton)  # Llama al método codigoBoton()
botonEnvio.pack()

root.mainloop()
