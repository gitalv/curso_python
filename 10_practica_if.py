def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "suspenso"
	return valoracion


print("Programa de evaluación de notas de alumnos")
nota_alumno = input("Introduce la nota del alumno: ") # Lee un valor de la entrada estándar. Se condidera string, hay que convertirlo a int.
print(evaluacion(int(nota_alumno)))
