# Clases: Herencia

class Vehiculos:
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
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelera:", self.acelera, "\nFrena:", self.frena)

# Hereda de Vehiculos
class Moto(Vehiculos):
	pass

miMoto = Moto("Honda", "CBR")
miMoto.estado()