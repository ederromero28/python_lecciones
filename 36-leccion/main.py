import os
import shutil

path = "tempfile.txt"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("El archivo no se encontro")
except PermissionError:
    print("No tienes permisos para eliminar el archivo")
except OSError:
    print("No se puede eliminar el archivo, probablemente es un directorio no vacio")
else:
    print(path + " El archivo se elimino correctamente")