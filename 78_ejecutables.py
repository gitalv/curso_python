# Ejecutable
# 1- Instalar pyinstaller:
#	  pip install pyinstaller
# 2- Ir al directorio donde está la aplicación python
# 3-  pyinstaller practicaCalculadora.py
# 4- Se genera una carpeta dist, que contiene el exe,
#    pero debe acompañarse con todos los demás archivos.
#    Si ejectuas el exe sale también la consola.
#    Si se quiere quitar esa consola lanzarlo así:
#     pyinstaller --windowed practicaCalculadora.py
# 5- Para no necesitar todos los demás ficheros, y tampoco necesitar
#    tener python instalado en otros ordenadores:
#     pyinstaller --windowed --onefile practicaCalculadora.py
# 6- Para agregar un icono al exe, poner un .ico al lado del fichero python.
#    Y lanzarlo así:
#     pyinstaller --windowed --onefile --icon=./logo.ico practicaCalculadora.py
