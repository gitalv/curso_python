# Diccionario: Conunto de parejas clave-valor.
# Cada clave es única, no se puede repetir.
miDic = {"Alemania":"Berlín", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
miDic["Italia"] = "Lisboa" # Añadir elemento

print(miDic)
print(miDic["Francia"]) # Obtener el valor de una clave

miDic["Italia"] = "Roma" # Cambiar elemento existente
print(miDic)

del miDic["Italia"] # Borrar un elemento
print(miDic)


# Distintos tipos para la clave y valor
miDic2 = {"aa":"aaaa", 23:"Jordan", "Mosqueteros":3}
print(miDic2)


# Usando tupla
miTupla = ("España", "Francia", "Reino Unido", "Alemania")
miDic3 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDic3)
print(miDic3["Francia"])

# Tupla como valor de una clave
miDic4 = {23:"Jordan", "nombre":"Michael", "equipo":"Chicago", "anillos":(1991,1992,1993,1996,1997,1998)}
print(miDic4)

# Diccionario como valor de una clave
miDic5 = {23:"Jordan", "nombre":"Michael", "equipo":"Chicago", "anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}
print(miDic5)
print(miDic5["anillos"])
print(miDic5["anillos"]["temporadas"][0])

# Sacar todas las claves del diccionario
print(miDic5.keys())

# Sacar todos los valores del diccionario
print(miDic5.values())

# Longitud del diccionario
print(len(miDic5))

