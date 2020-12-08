# Documentación que incluye pruebas unitarias
# En una prueba dentro de la documentación puedo poner variables, bucles, etc.
# Para tabular tengo que usar "..." en vez de ">>>"
# En la respuesta esperado puedo usar "..." como comodín de cualquier número de caracteres.
# Esto es útil para pruebas que devuelven excepciones.

import doctest
import math

def raizCuadrada(listaNumeros):
	"""
	La función devuelve una lista con la
	raíz cuadrdad de los elementos numéricos
	pasados por parámetros en otra lista

	>>> lista=[]
	>>> for i in [4,9,16]:
	...		lista.append(i)  # Aqui en vez ">>>" hay que poner "..."
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4,-9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error
	"""
	return [math.sqrt(n) for n in listaNumeros]

print(raizCuadrada([9,16,25,36,39]))
doctest.testmod()

