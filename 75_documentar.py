# Documentación

def areaCuadrado(lado):
	"""Calcula el área de un cuadrado
	elevando al cuadrado el lado pasado por parámetro"""

	return "El área del cuadrado es: " + str(lado*lado)

def areaTriangulo(base, altura):
	"""Calcula el área de un triángulo
	utilizando los parámetros base y altura"""

	return "El área del triángulo es: " + str((base*altura)/2)

print(areaCuadrado(2))
print(areaTriangulo(2,7))

# Esto imprime la documentación
print(areaCuadrado.__doc__)
print(areaTriangulo.__doc__)
help(areaCuadrado)
help(areaTriangulo)


# En una clase
class Areas:
	"""Esta clase calcula las áreas de diferentes figuras geómétricas"""

	def areaCuadrado(lado):
		"""Calcula el área de un cuadrado
		elevando al cuadrado el lado pasado por parámetro"""

		return "El área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):
		"""Calcula el área de un triángulo
		utilizando los parámetros base y altura"""

		return "El área del triángulo es: " + str((base*altura)/2)

# Esto imprime la documentación. Primero poner el nombre de la clase
print(Areas.areaCuadrado.__doc__)
print(Areas.areaTriangulo.__doc__)
help(Areas.areaCuadrado)
help(Areas.areaTriangulo)
# Ayuda de toda la clase
help(Areas)


# Sacar la documentación de un módulo
from _34_modulos import funciones_matematicas
help(funciones_matematicas)
