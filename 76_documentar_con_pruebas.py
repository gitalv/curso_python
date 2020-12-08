# Documentación que incluye pruebas unitarias

import doctest

def areaTriangulo(base, altura):
	"""Calcula el área de un triángulo
	utilizando los parámetros base y altura
	>>> areaTriangulo(3,6)
	9.0
	>>> areaTriangulo(4,5)
	10.0
	>>> areaTriangulo(9,3)
	13.5
	"""
	return (base*altura)/2

def areaTrianguloStr(base, altura):
	"""Calcula el área de un triángulo
	utilizando los parámetros base y altura
	>>> areaTrianguloStr(3,6)
	'El área del triángulo es: 9.0'"""
	return "El área del triángulo es: " + str((base*altura)/2)



def compruebaMail(mailUsuario):
	"""
	La función compruebaMail evalúa un mail recibido en busca de la @.
	Si tiene una @ es correcto, si tiene más de una @ es incorrecto.
	Si la @ está al final es incorrecto.
	>>> compruebaMail('juan@curso.es')
	True
	>>> compruebaMail('juancurso.es@')
	False
	>>> compruebaMail('juancurso.es')
	False
	>>> compruebaMail('juan@curso@.es')
	False
	"""
	arroba = mailUsuario.count("@")
	if arroba != 1 or mailUsuario.rfind("@") == (len(mailUsuario)-1) or mailUsuario.find("@") == 0:
		return False
	else:
		return True


doctest.testmod()

