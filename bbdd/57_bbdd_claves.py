# Bases de datos: PRIMARY KEY
# SQLite
# Ejectuar en consola aparte (REPL): CTRL-ALT-B
# Ejecutar en consola integrada: CTRL-B

import sqlite3

# Crear BD y conexión
miConexion = sqlite3.connect("GestionProductos")  # Crea un fichero vacío (0 KB)

miCursor = miConexion.cursor()

"""
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos = [
	("AR01", "pelota", 20, "juguetería"),
	("AR02", "pantalón", 15, "confección"),
	("AR03", "destornillador", 25, "ferretería"),
	("AR04", "jarrón", 45, "cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)
"""

# Si se intenta insertar la misma PK da error:
# sqlite3.IntegrityError: UNIQUE constraint failed: PRODUCTOS.CODIGO_ARTICULO
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'juguetería')")

miConexion.commit()


miConexion.close()
