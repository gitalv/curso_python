def becas():
	print("Programa becas")

	distancia_escuela = int(input("Distancia escuela en Km: "))
	print(distancia_escuela)

	numero_hermanos = int(input("Número de hermanos: "))
	print(numero_hermanos)

	salario_familiar = int(input("Salario anual bruto: "))
	print(salario_familiar)

	if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
		print("Tienes derecho a beca")
	else:
		print("No tienes derecho a beca")


def optativas():
	print("Asignaturas optativas:")
	asignaturas = ("informática gráfica, pruebas de software, usabilidad y accesibilidad")
	print(asignaturas)
	asignatura = input("Asignatura: ")
	asignatura = asignatura.lower()
	if asignatura in asignaturas:
		print("Asignatura elegida: " + asignatura)
	else:
		print("Asignatura no existe")


# becas()
optativas()
