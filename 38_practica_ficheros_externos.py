# Ficheros: Leer fichero con puntero

from io import open

# Leer un fichero todo de una vez a un string
archivo_texto = open("archivo.txt", "r")
print(archivo_texto.read())  # Lee todo el fichero
print(archivo_texto.read())  # Ya no lee nada, porque el puntero está al final
archivo_texto.close()


archivo_texto = open("archivo.txt", "r")
print(archivo_texto.read())  # Lee todo el fichero
archivo_texto.seek(0)  # Mueve el puntero al principio
print(archivo_texto.read())  # Lee todo el fichero
archivo_texto.close()

archivo_texto = open("archivo.txt", "r")
print(archivo_texto.read())  # Lee todo el fichero
archivo_texto.seek(11)  # Mueve el puntero a la posición 11
print(archivo_texto.read())  # Lee todo el fichero desde el puntero
archivo_texto.close()

archivo_texto = open("archivo.txt", "r")
print(archivo_texto.read(11))  # Lee los primeros 11 bytes del fichero
print(archivo_texto.read())  # Lee resto del fichero
archivo_texto.close()

archivo_texto = open("archivo.txt", "r")
archivo_texto.seek(len(archivo_texto.read()) / 2)  # Ir a la mita del fichero
print(archivo_texto.read())  # Leer de la mitad del fichero al final
archivo_texto.close()

archivo_texto = open("archivo.txt", "r")
archivo_texto.seek(len(archivo_texto.readline()))  # Ir al final de la primera línea
print(archivo_texto.read())  # Leer de la segunda línea del fichero al final
archivo_texto.close()

archivo_texto = open("archivo.txt", "r+") # Lectura y escritura
archivo_texto.write("Comienzo del texto") # Reemplaza lo que hubiera al principio del fichero
archivo_texto.close()

archivo_texto = open("archivo.txt", "r+")
lista_texto = archivo_texto.readlines()
print(lista_texto)
lista_texto[1] = "Esta línea ha sido incluida desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)  # Escribo al fichero, cambiado la línea 1 (empezando por 0)
archivo_texto.close()
