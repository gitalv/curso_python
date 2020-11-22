# for

for i in range(5,50,3): # Inicio, fin, incremento
	print(f"Valor de la variable {i}") # 5, 8, 11, ..., 47


valido = False
email = input("Introduce tu email: ")
for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")