# Expresiones regulares: Metacaracteres

import re

lista_nombres = [
	'Ana Gómez',
	'María Martín',
	'Sandra López',
	'Santiago Martín',
	'Sandra Fernández'
	]
for elemento in lista_nombres:
	if re.findall('^Sandra', elemento): # Nombres que empiezan por Sandra
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('Martín$', elemento): # Nombres que acaben por Martín
		print(elemento)
print()


lista_nombres = [
	'http://pildorasinformaticas.es',
	'ftp://pildorasinformaticas.es',
	'http://pildorasinformaticas.com',
	'ftp://pildorasinformaticas.com'
	]

for elemento in lista_nombres:
	if re.findall('.es$', elemento): # Nombres que acaben por es
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('^ftp', elemento): # Nombres que empiecen por ftp
		print(elemento)
print()


lista_nombres = [
	'http://informaticaenespaña.es',
	'http://pildorasinformaticas.es',
	'http://pildorasinformaticas.com'
	]

for elemento in lista_nombres:
	if re.findall('[ñ]', elemento): # Si contiene 'ñ'
		print(elemento)
print()


lista_nombres = [
	'hombres',
	'mujeres',
	'mascotas',
	'niños',
	'niñas',
	'camión',
	'camion'
	]

# El corchete funcionar como OR
for elemento in lista_nombres:
	if re.findall('niñ[oa]s', elemento): # niños o niñas
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('cami[oó]n', elemento): # camion o camión
		print(elemento)
print()
