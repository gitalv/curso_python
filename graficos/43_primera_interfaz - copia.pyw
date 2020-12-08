# Frames

from tkinter import *

# RAIZ
raiz = Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(False, False) # width, height: No se puede redimensionar ni el ancho, ni el alto
raiz.iconbitmap("gato.ico")  # Icono que aparece arriba a la izquierda en la ventana
raiz.geometry("700x400")  # Size
raiz.config(bg="blue")

raiz.config(bd=25)  # Ancho del borde
raiz.config(relief="groove")  # Tipo del borde
raiz.config(cursor="hand2")


# FRAME
miFrame = Frame()
#miFrame.pack(side="right")  # pack() mete el frame en la raiz. side() indica a que lado de la raíz se ancla el frame (por defecto top)
#miFrame.pack(side="left", anchor="n")  # Se ancla arriba (north) y a la izquierda
#miFrame.pack(fill="x")  # El frame se expande en horizontal
#miFrame.pack(fill="y", expand=True)  # El frame se expande en vertical
#miFrame.pack(fill="both", expand=True)  # El frame se expande en horizontal y vertical
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width=650, height=350)  # Size. Si no se pone tamaño a la raíz, se adapta al frame

# Borde
miFrame.config(bd=35)  # Ancho del borde
#miFrame.config(relief="groove")  # Tipo del borde
miFrame.config(relief="sunken")  # Tipo del borde

# Puntero del ratón
#miFrame.config(cursor="hand2")  # Tipo del cursor
miFrame.config(cursor="pirate")


raiz.mainloop()
