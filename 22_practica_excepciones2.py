# except múltiple
# except general
# finally

def divide():
	try:
		op1 = float(input("Introduce el primer número: "))
		op2 = float(input("Introduce el segundo número: "))
		print("La división es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido es erróneo")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
	finally: # Se ejecuta aunque haya excepción
		print("Cálculo finalizado")


def divide2():
	try:
		op1 = float(input("Introduce el primer número: "))
		op2 = float(input("Introduce el segundo número: "))
		print("La división es: " + str(op1/op2))
	except:
		print("Ha ocurrido un error")

	print("Cálculo finalizado")



divide()
divide2()