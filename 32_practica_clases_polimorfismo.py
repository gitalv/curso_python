# Polimorfismo. Para llamar a un método común no hace falta que los objetos deriven de la misma clase base

class Coche:
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")


class Moto:
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")


class Camion:
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")


def desplazamiento(vehiculo):
	vehiculo.desplazamiento()  # Polimorfismo


miVehiculo = Moto()
miVehiculo.desplazamiento()
desplazamiento(miVehiculo)

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()
desplazamiento(miVehiculo2)

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()
desplazamiento(miVehiculo3)