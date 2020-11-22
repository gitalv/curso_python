print("Verificación de acceso")
edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario < 18:
	print("No puedes pasar")
elif edad_usuario > 100:
	print("Ead incorrecta")
else:
	print("Puedes pasar")


nota_alumno = int(input("Introduce tu nota: "))

if nota_alumno < 5:
	print("Insuficiente")
elif nota_alumno < 6:
	print("Suficiente")
elif nota_alumno < 7:
	print("Bien")
elif nota_alumno < 9:
	print("Notable")
else:
	print("Sobresaliente")

print("Fin")
