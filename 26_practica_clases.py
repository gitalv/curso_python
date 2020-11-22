# Clases

class Coche:
	# Propiedades (variables de clase)
	# Estado: Valores de las variables para una instancia de la clase
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enMarcha = False

	# Comportamiento (métodos)
	def arrancar(self):
		self.enMarcha = True

	def estado(self):
		if(self.enMarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"

miCoche = Coche()
print("El largo del coche es", miCoche.largoChasis)
print("El ancho del coche es", miCoche.anchoChasis)
print("El coche tiene", miCoche.ruedas, "ruedas")
miCoche.arrancar();
print(miCoche.estado());
