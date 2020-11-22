# Las tuplas son inmutables. Paréntesis en vez de corchetes.
miTupla = ("aa", 5, True, 1.23, "aa")
print(miTupla)
print(miTupla[2])

# También se puede definir una tupla sin poner paréntesis. Se llama empquetado de tupla.
miTupla2 = "aa", 5, True
print(miTupla2)


# Construir una lista a partir de una tupla
miLista = list(miTupla)
print(miLista)

# De lista a tupla
miTupla3 = tuple(miLista)
print(miTupla3)
print("aa" in miTupla3)
print(miTupla.count("aa")) # Numero de veces que aparece un elemento en la tupla
print(len(miTupla)) # Número de elementos en la tupla


# Tuplas unitarias. Tiene que llevar "," al final. Si no se pone "," se considera un String.
miTuplaUnitaria = ("Juan",)
print(type(miTuplaUnitaria))
print(len(miTuplaUnitaria))


# Desempaquetado de tupla
miTup = "Juan", 13, 1, 1995
nombre, mes, dia, anio = miTup
print(nombre)
print(mes)
print(dia)
print(anio)