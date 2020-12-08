# Ficheros: escritura y lectura
# https://docs.python.org/3.8
# https://docs.python.org/3.8/library/io.html

from io import open

# Crear y escribir a un fichero
archivo_texto = open("archivo.txt", "w")
frase = "Estupendo día para estudiar Python\nel miércoles"
archivo_texto.write(frase)
archivo_texto.close()

# Leer un fichero todo de una vez a un string
archivo_texto = open("archivo.txt", "r")
texto = archivo_texto.read()  # Lee todo el fichero
archivo_texto.close()
print(texto)

# Leer un fichero todo de una vez a una lista con las líneas
archivo_texto = open("archivo.txt", "r")
lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])


# Añadir a un fichero
archivo_texto = open("archivo.txt", "a")
archivo_texto.write("\nsiempre es una buena ocasión para estudiar Python")
archivo_texto.close()
