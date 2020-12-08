# Expresiones regulares:
# match: Coincidencia al comienzo
# search: Coincidencia en cualquier parte

import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "sandra López"
nombre5 = "Jara López"
nombre6 = "Lara López"

if re.match("Sandra", nombre4, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")
print()

# El punto es un comodín
if re.match(".ara", nombre6, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")
print()


cadena1 = "Jara López"
cadena2 = "546546546"
cadena3 = "a546546546"

# \d indica si empieza por número
if re.match("\d", cadena2):
	print("Hemos encontrado el número")
else:
	print("No hemos encontrado el número")
print()


if re.search("López", nombre1, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")
print()


codigo1 = "sldfjslfgldksjgjsdlkgj71sldfhslfjlkssdf"
codigo2 = "lsdfjklshdjfh71ñlfgñdsjgñlkdsjfgkñljdgñjk"
codigo3 = "sñlidfjslñakfjdñlskjdfñlsjfdj"

if re.search("71", codigo3):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")
print()
