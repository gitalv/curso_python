# Expresiones regulares

import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
# Buscar si existe una cadena dentro de otra
print(re.search("aprender", cadena))  # <re.Match object; span=(8, 16), match='aprender'>
print(re.search("aprenderrr", cadena))  # None ==> No está

textoBuscar = "aprender"
if re.search(textoBuscar, cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")

textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start())  # Dice el caracter inicial dónde lo encuentra
print(textoEncontrado.end())  # Dice el caracter final dónde lo encuentra
print(textoEncontrado.span())  # (8, 16): Dice el caracter inicial y final dónde lo encuentra


textoBuscar = "Python"
print(re.findall(textoBuscar, cadena))  # ['Python', 'Python']
