# Bases de datos: UNIQUE
# SQLite
# Ejectuar en consola aparte (REPL): CTRL-ALT-B
# Ejecutar en consola integrada: CTRL-B

import sqlite3

# Crear BD y conexión
miConexion = sqlite3.connect("GestionProductosUnique")  # Crea un fichero vacío (0 KB)

miCursor = miConexion.cursor()

# Create table con campo unique
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos = [
	("pelota", 20, "juguetería"),
	("pantalón", 15, "confección"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica"),
	#("pantalón", 35, "confección")
	("pantalones", 35, "confección")
]

# Donde va la secuencia poner NULL en vez de ?
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()


miConexion.close()
