# Lista
miLista = ["aa", "bb", "cc"]

# Añadir un elemento al final
miLista.append("dd")

# Insertar un elemento en cualquier posición
miLista.insert(1, "aa2")

# Añade otra lista al final
miLista.extend(["xx", "yy"])

print(miLista)    # Imprime toda la lista
print(miLista[:]) # Imprime toda la lista
print(miLista[2]) # Imprime elemento en posición 2. El primer elemento es el 0.
print(miLista.index("cc")) # Ìmprime la posición de un elemento. Sólo la primera coincidencia.
print("bb" in miLista) # Imprime si un elemento está en la lista
miLista.remove("bb") # Borra un elemento de la lista
print("bb" in miLista) # Imprime si un elemento está en la lista
miLista.pop() # Borra el último elemento de la lista
print(miLista)    # Imprime toda la lista


# Lista con elementos de tipos distintos
miLista2 = ["aa", 2, 3.5, True]
print(miLista2)

miLista3 = miLista + miLista2 # Suma de dos listas. Igual que extend()
print(miLista3)

miLista4 = miLista2 * 3 # Repite la lista 3 veces
print(miLista4)
