# Bases de datos
# SQLite
# Ejectuar en consola aparte (REPL): CTRL-ALT-B
# Ejecutar en consola integrada: CTRL-B

import sqlite3

# Crear BD y conexión
miConexion = sqlite3.connect("PrimeraBase")  # Crea un fichero vacío (0 KB)

miCursor = miConexion.cursor()
# Ejecutar esto solo una vez, la siguiente dará error
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")

miConexion.commit()

# Cerrar conexión
miConexion.close()
