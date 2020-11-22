# yield, yield from

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))



def devuelve_ciudades2(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudades_devueltas = devuelve_ciudades2("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))



def devuelve_ciudades3(*ciudades):
	for elemento in ciudades:
		yield from elemento # Hace lo mismo que iterar sobre elemento, en este caso devuelve letra a letra

ciudades_devueltas = devuelve_ciudades3("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
