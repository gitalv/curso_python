# Expresiones regulares: Rangos

import re

lista_nombres = [
	'Ana',
	'Pedro',
	'María',
	'Rosa',
	'Sandra',
	'Celia'
	]

for elemento in lista_nombres:
	if re.findall('[o-t]', elemento): # Que contengan cualquier letra entre la o y la t
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('^[O-T]', elemento): # Que empiecen por cualquier letra entre la O y la T
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('[o-t]$', elemento): # Que terminen por cualquier letra entre la o y la t
		print(elemento)
print()


lista_nombres = [
	'Ma1',
	'Se1',
	'Ma2',
	'Ba1',
	'Ma3',
	'Va1',
	'Va2',
	'Ma4',
	'MaA',
	'Ma5',
	'MaB',
	'MaC',
	'Ma.1',
	'Ma:3',
	'Ma.5',
	'Ma:C',
	]

for elemento in lista_nombres:
	if re.findall('Ma[0-3]', elemento): # Que contengan cualquier letra entre 0 y 3
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('Ma[^0-3]', elemento): # Que contengan cualquier letra que no esté entre 0 y 3
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('Ma[0-3A-B]', elemento): # Que contengan cualquier letra entre 0 y 3 o entre A y B
		print(elemento)
print()

for elemento in lista_nombres:
	if re.findall('Ma[.:]', elemento): # Que contengan . o :
		print(elemento)
print()
