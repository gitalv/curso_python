# for, range

for i in ["Pildoras", "Informaticas", 3]:
	print("Hola", end="") # Cambia el retorno de carro al final por ""
	print(i)



miEmail = input("Dirección de email: ")

# Iterar los caracteres de un String
email = False
for i in miEmail: # "pildoras@informaticas.es"
	if i == "@":
		email = True

if email:
	print("Email correcto")
else:
	print("Email incorrecto")


miEmail = input("Dirección de email: ")

# Iterar los caracteres de un String
contador = 0
for i in miEmail: # "pildoras@informaticas.es"
	if i == "@" or i == ".":
		contador = contador + 1

if contador == 2:
	print("Email correcto")
else:
	print("Email incorrecto")


# Tipo range. En python 2 es una función, en python 3 es un tipo.
for i in range(5): # 0,1,2,3,4
	print(i)
