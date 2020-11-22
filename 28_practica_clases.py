# Métodos privados (encapsulación)

class Coche:
	# Contructor
	def __init__(self):
		# Propiedades (variables de clase)
		# Estado: Valores de las variables para una instancia de la clase
		# Hacer una variable privada: Poner "__" como prefijo. Se renombra internamente a _Coche__ruedas
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4
		self.__enMarcha = False

	# Comportamiento (métodos)
	def arrancar(self, arrancamos):
		self.__enMarcha = arrancamos

		if self.__enMarcha:
			chequeo = self.__chequeo_interno()
			if chequeo:
				return "El coche está en marcha"
			else:
				return "Algo ha ido mal en el chequeo. No podemos arrancar" 
		else:
			return "El coche está parado"	

	def estado(self):
		print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", miCoche.__largoChasis)

	# Este método para que sea privado hay que llamarle con dos quiones bajos al principio
	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		self.gasolina = "ok"
		self.aceite = "ok"  # Si pongo "mal" el coche no arranca porque falla el chequeo interno
		self.puertas = "cerradas"
		if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
			return True
		else:
			return False


miCoche = Coche()
print(miCoche.arrancar(True));
miCoche.estado();
#print(miCoche.__chequeo_interno()); # Esto da error porque el método es privado

print("----------A continuación creamos el segundo objeto-----------")
miCoche2 = Coche()
print(miCoche2.arrancar(False));

# No cambia __ruedas porque es privado. No da error, porque self.__ruedas se renombra internamente a _Coche__ruedas
miCoche2.ruedas = 2   # Esto solo crea una nueva variable
miCoche2.__ruedas = 2 # Esto solo crea una nueva variable

miCoche2.estado();
