# Bases de datos: CRUD (Create, Read, Update, Delete)
# SQLite
# Ejectuar en consola aparte (REPL): CTRL-ALT-B
# Ejecutar en consola integrada: CTRL-B

import sqlite3

# Crear BD y conexión
miConexion = sqlite3.connect("GestionProductosUnique")  # Crea un fichero vacío (0 KB)

miCursor = miConexion.cursor()

# Read
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")
productos = miCursor.fetchall()
print(productos)

# Update
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=99 WHERE NOMBRE_ARTICULO='pelota'")

# Delete
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()
