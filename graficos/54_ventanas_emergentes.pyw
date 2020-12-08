# Ventanas emergentes de abrir, grabar, etc.
# Importar la librería filedialog

from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Ventanas emergentes")

def abreFichero():
	fichero = filedialog.askopenfilename(title="Abrir", initialdir="c:",
		filetypes=(("Ficheros de Excel","*.xlsx"),
				   ("Ficheros de Texto","*.txt"),
				   ("Todos los ficheros","*.*")))
	print(fichero)


Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
