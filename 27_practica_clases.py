# Constructor y variables privadas (encapsulación)

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
			return "El coche está en marcha"
		else:
			return "El coche está parado"	

	def estado(self):
		print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", miCoche.__largoChasis)


miCoche = Coche()
print(miCoche.arrancar(True));
miCoche.estado();

print("----------A continuación creamos el segundo objeto-----------")
miCoche2 = Coche()
print(miCoche2.arrancar(False));

# No cambia __ruedas porque es privado. No da error, porque self.__ruedas se renombra internamente a _Coche__ruedas
miCoche2.ruedas = 2   # Esto solo crea una nueva variable
miCoche2.__ruedas = 2 # Esto solo crea una nueva variable

miCoche2.estado();
