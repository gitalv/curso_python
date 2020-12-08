# Decoradores: Son 3 funciones:
#  1- La primera función es la decoradora.
#  2- La segunda función se pasa como parámetro a la decoradora.
#  3- La tercera función se retorna en la decoradora, es la total.
# Util cuando se quiere añadir un mismo comportamiento a muchas funciones,
# sin cambiarlas.
# Ejemplo: Decorar una función que ejecuta un SQL para que abra conexión y la cierre.
# Para usarla se usa un hint con @


def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo: ")

		funcion_parametro()

		# Acciones adicionales que decoran
		print("Hemos terminado el cálculo")

	return funcion_interior


@funcion_decoradora
def suma():
	print(15+20)

@funcion_decoradora
def resta():
	print(30-10)

suma()
resta()
