# Clases: Herencia, sobreescritura de método en el hijo
# Herencia múltiple
# super().__init__()
# Vehiculos.__init__(self, ...)
# Vehiculos.<method>(self, ...)

# Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance.
# You can view the MRO by using the __mro__ attribute: print(BicicletaElectrica.__mro__)

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
	hcaballito = ""

	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito"

	# Sobreescribo este método
	def estado(self):
		#print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelera:", self.acelera, "\nFrena:", self.frena, "\nCaballito:", self.hcaballito)
		super().estado()  # Uso el estado de la clase padre con super(), y luego añado el estado adicional de la moto
		print("Caballito:", self.hcaballito)


class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado = cargar
		if self.cargado:
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"


class VElectricos():
	def __init__(self, autonomia):
		self.autonomia = autonomia

	def cargarEnergia(self):
		self.cargando = True


# Herencia múltiple
# Se coge el constructor de la primera clase que se indica como padre
class BicicletaElectrica(VElectricos, Vehiculos):
	def __init__(self, autonomia, marca, modelo):
		#super(Vehiculos, self).__init__("Orbea", "kkk")
		# Para llamar al constructor de Vehiculos. Con super() llamo al constructor de la primera clase definida en la herencia: VElectricos
		super().__init__(autonomia)
		Vehiculos.__init__(self, marca, modelo)

	# Sobreescribo este método
	def estado(self):
		Vehiculos.estado(self)
		print("Autonomia:", self.autonomia)


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()  # Llama al método estado() sobreescrito en la clase Moto, no al de la clase Vehiculos

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica(100, "Orbea", "kkk")
miBici.estado()

print(BicicletaElectrica.__mro__)
