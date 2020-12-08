# Deserializar una clase a partir de fichero. Problema: Aqui se tiene que conocer la clase que se serializó
# Solución:
#  - O bien se vuelve a definir aquí la clase
#  - O bien se define la clase en un tercer fichero, para que su definición no esté duplicada
# Ejecutar: CTRL-ALT-B

import pickle
#from _34_modulos2.modulo_vehiculos import Vehiculos

class Vehiculo:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelera:", self.acelera, "\nFrena:", self.frena, "\n")



fichero_apertura = open("losCoches", "rb")
mis_coches = pickle.load(fichero_apertura)
fichero_apertura.close()
del(fichero_apertura)

for c in mis_coches:
	c.estado()
