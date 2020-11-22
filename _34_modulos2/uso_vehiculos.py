# import:
# 1- Primero busca el módulo en el directorio de este fichero
# 2- Si no lo encuentra, busca en el syspath, que incluye el directorio de instalación de python

from modulo_vehiculos import *

miCoche = Vehiculos("Mazda", "MX5")
miCoche.estado()