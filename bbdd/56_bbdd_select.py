# Bases de datos
# SQLite
# Ejectuar en consola aparte (REPL): CTRL-ALT-B
# Ejecutar en consola integrada: CTRL-B

import sqlite3

# Crear BD y conexión
miConexion = sqlite3.connect("PrimeraBase")  # Crea un fichero vacío (0 KB)

miCursor = miConexion.cursor()
# Ejecutar el CREATE TABLE solo una vez, la siguiente dará error
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")
'''
variosProductos = [
	("Camiseta", 10, "Deportes"),
	("Jarrón", 90, "Cerámica"),
	("Camión", 20, "Juguetería")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
'''
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()  # Devuelve una lista con todos los registros: Cada fila en una tupla
#print(variosProductos)
for producto in variosProductos:
	#print(producto)
	#print(producto[0])
	print("Nombre artículo:", producto[0], "Precio:", producto[1], "Sección:", producto[2])

miConexion.commit()

# Cerrar conexión
miConexion.close()
