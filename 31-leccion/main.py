import os

path = "E:\\PP\\Utilidades"

if os.path.exists(path):
    print("La ubicación existe.")
    if os.path.isfile(path):
        print("Es un archivo.")
    elif os.path.isdir(path):
        print("Es un directorio.")
else:
    print("El archivo no existe.")