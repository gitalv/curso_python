# Serialización: librería pickle. Métodos dump(), load()

import pickle

lista_nombres = ["Pedro","Ana","Maria","Isabel"]

# Serializo a fichero
fichero_binario = open("lista_nombres", "wb") # Escritura en binario
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()

# Deserializar
fichero = open("lista_nombres", "rb")
lista = pickle.load(fichero)
print(lista)
fichero.close()
