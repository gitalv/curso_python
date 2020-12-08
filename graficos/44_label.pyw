# Labels

from tkinter import *

# RAIZ
root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miLabel = Label(miFrame, text="Hola Python", fg="red", font=("Comic Sans MS", 18))
#miLabel.pack()  # Con pack() el frame encoge hasta el label, mejor usar place()
miLabel.place(x=100, y=50)

miImagen = PhotoImage(file="mouse.gif")
miLabel2 = Label(miFrame, image=miImagen)
miLabel2.place(x=100, y=200)

root.mainloop()
