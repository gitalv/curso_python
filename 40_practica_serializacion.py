# Serializar una clase a fichero
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



coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seat", "Leon")
coche3 = Vehiculo("Renault", "Megane")
coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero)
