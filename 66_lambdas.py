# Funciones lambda. El ":" es como un return.

def area_triangulo(base, altura):
	return (base*altura)/2


triangulo1 = area_triangulo(2,3)
triangulo2 = area_triangulo(3,4)
print(triangulo1)
print(triangulo2)


# Funcion lambda (anónimas)
area_triangulo_lambda = lambda base, altura: (base*altura)/2
triangulo1 = area_triangulo_lambda(2,3)
triangulo2 = area_triangulo_lambda(3,4)
print(triangulo1)
print(triangulo2)


#al_cubo = lambda numero: pow(numero, 3)
al_cubo = lambda numero: numero**3
print(al_cubo(13))


destacar_valor = lambda comision: "¡{}! €".format(comision)
comision_Ana = 15585
print(destacar_valor(comision_Ana))
