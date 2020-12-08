# Esto guarda una lista de objetos en un fichero.
# Al inicio lee los objetos del fichero, añade uno más y vuelve a escribir toda la lista al fichero truncándolo.
# Sería mejor que para escribir un nuevo objeto se hiciera un nuevo dump(), sin truncar lo anterior.
# Después para leer habría que hacer tantos load() como dump() se hayan hecho:
'''
f=open('a.p', 'wb')
pickle.dump({1:2}, f)
pickle.dump({3:4}, f)
f.close()
 
f=open('a.p', 'rb')
pickle.load(f)
pickle.load(f)
f.close()
'''
# He hecho ese método en "41_practica_guardado_permanente2.py". Problema: El fichero que se crea ocupa el doble que haciendo un solo dump().

import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con nombre", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
	personas = []

	def __init__(self):
		# Usamos el modo "a" en vez de "r" para que cuando no exista el fichero lo cree.
		# Open modes:
		# a: Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
		# b: Open in binary mode.
		# +: Open a file for updating (reading and writing)
		listaDePersonas = open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)  # Necesario porque con "a" el seek está al final

		try:
			self.personas = pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero no existe o está vacío")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def guardarPersonasEnFicheroExterno(self):
		# Truncamos el fichero y escribimos toda la lista de personas en el.
		# La lista contiene las personas del fichero original más las que hayamos añadido ahora.
		# w: Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
		listaDePersonas = open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()

	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es:")
		for p in self.personas:
			print(p)


miLista = ListaPersonas()

p1 = Persona("Sandra", "Femenino", 29)
p2 = Persona("Antonio", "Masculino", 39)
p3 = Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(p1)
miLista.agregarPersonas(p2)
miLista.agregarPersonas(p3)

miLista.mostrarInfoFicheroExterno()
