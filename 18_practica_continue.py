# --------------------------------------
# continue

for letra in "Python":
	if letra == "h":
		continue
	print("Letra: " + letra)


nombre = "Pildoras informaticas"
print(len(nombre)) # 21
# Contar letras quitando espacios
contador = 0
for i in nombre:
	if i == " ":
		continue
	contador += 1
print(contador)
# ---------------------------------------


# --------------------------------------
# pass

# Blucle infinito hasta que se pulse CTRL-C
#while True:
#	pass


class MiClase:
	pass # Implementar más tarde
# -------------------------------------


# --------------------------------------
# else

email = input("Introduce tu email: ")
for i in email:
	if i == "@":
		arroba = True
		break
else: # Forma parte del bucle for. Se ejecuta cuando el blucle termina. El break no entra en el else.
	arroba = False

print(arroba)
# --------------------------------------
