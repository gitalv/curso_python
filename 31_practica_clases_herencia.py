# Clases: super(), isinstance()
# super() is equivalent to super(Subclass, self) when Subclass is the same as the one we are in now,
#   but we can put other previous sublasses there, to skip overwrited methods.

class Persona:
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre = nombre
		self.edad = edad
		self.lugar_residencia = lugar_residencia

	def descripcion(self):
		print("Nombre:", self.nombre, "Edad:", self.edad, "Lugar residencia:", self.lugar_residencia)


class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario:", self.salario, "Antiguedad:", self.antiguedad)


antonio = Persona("Antonio", 55, "España")
antonio.descripcion()

#pepe = Empleado("Pepe", 55, "España")  # Error, llama al constructor de Empleado, no al de Persona
#pepe = Empleado(1500, 10)  # Esto funciona pero luego da error en descripcion() porque no se ha definido nombre, etc. ==> Solución: Añadir super() al constructor
#pepe.descripcion()

pepe = Empleado(1500, 10, "Pepe", 45, "Colombia")
pepe.descripcion()


print(isinstance(antonio, Persona))  # True
print(isinstance(antonio, Empleado)) # False

print(isinstance(pepe, Persona))  # True
print(isinstance(pepe, Empleado)) # True
