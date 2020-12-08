# Interfaces gráficas: Usaremos la libería tkinter, que usa TCL/TK
# Extensión del fichero: pyw para que al ejecutar el fichero en Windows no habra una consola, sino que sólo se abra la ventana.

# Raíz

from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(False, False) # width, height: No se puede redimensionar ni el ancho, ni el alto
raiz.iconbitmap("gato.ico")  # Icono que aparece arriba a la izquierda en la ventana
raiz.geometry("650x350")  # Size
raiz.config(bg="blue")
raiz.mainloop()
