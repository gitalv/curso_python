# Strings
# Doc python: pyspanishdoc.sourceforge.net

nombreUsuario = input("Introduce tu nombre de usuario: ")
print("Nombre usuario:", nombreUsuario.upper())
print("Nombre usuario:", nombreUsuario.lower())
print("Nombre usuario:", nombreUsuario.capitalize())

edad = input("Introduce la edad: ")
while(edad.isdigit() == False):
	print("La edad debe ser numérica")
	edad = input("Introduce la edad: ")

if int(edad) < 18:
	print("No puede pasar")
else:
	print("Puede pasar")