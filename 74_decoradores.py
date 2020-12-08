# Decoradores con parámetros

def funcion_decoradora(funcion_parametro):
	# *args: Número indeterminado de parámetros
	# **kwargs: Número indeterminado de parámetros en formato clave, valor
	def funcion_interior(*args, **kwargs):
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo: ")

		funcion_parametro(*args, **kwargs)

		# Acciones adicionales que decoran
		print("Hemos terminado el cálculo")
		print()

	return funcion_interior


@funcion_decoradora
def suma(num1, num2):
	print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def suma3(num1, num2, num3):
	print(num1+num2+num3)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))

suma(7,5)
resta(12,10)
suma3(7,5,8)
potencia(2,3)
potencia(base=2, exponente=3)
