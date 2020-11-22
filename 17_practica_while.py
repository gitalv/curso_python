# while

import math

i=1
while i <= 10:
	print("Ejecucion " + str(i))
	i = i+1

print("Terminó la ejecución")


edad = int(input("Introduce la edad: "))
while edad < 0 or edad > 100:
	print("Edad incorrecta")
	edad = int(input("Introduce la edad: "))

print("Edad correcta: " + str(edad))



print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número: "))

intentos = 0
while numero < 0:
	print("No se puede hayar la raíz de un número negativo")
	if intentos == 2:
		print("Has consumido demasiados intentos")
		break
	numero = int(input("Introduce un número: "))
	if numero < 0:
		intentos = intentos+1

if intentos < 2:
	solucion = math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
