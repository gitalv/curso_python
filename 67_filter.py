# Funciones filter: Aplican una condición a cada parámetro de una lista

def numero_par(num):
	if num % 2 == 0:
		return True

numeros = [17,24,7,39,8,51,92]
print(list(filter(numero_par, numeros)))

# Filter con lambda
print(list(filter(lambda np: np%2==0, numeros)))


# Ejemplo de filter con objetos de clase
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(
			self.nombre, self.cargo, self.salario)

listaEmpleados = [
	Empleado("Juan", "Director", 75000),
	Empleado("Ana", "Presidenta", 85000),
	Empleado("Antonio", "Administrativo", 25000),
	Empleado("Sara", "Secretaria", 27000),
	Empleado("Mario", "Botones", 21000)
]

# Empleados con salarios mayor que 50000
salarios_altos = filter(lambda empleado: empleado.salario>50000, listaEmpleados)
for empleado_salario in salarios_altos:
	print(empleado_salario)
