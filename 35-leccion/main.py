import os

origen = 'E:\\PP\\texto.txt'
destino = 'E:\\PP\\PeruPetro\\text.txt'

try:
    if os.path.exists(destino):
        print("Ya hay un archivo con ese nombre en la ruta destino")
    else:
        os.replace(origen, destino)
        print(origen + " fue movido exitosamente a " + destino)

    pass
except FileNotFoundError:
    print(origen + " El archivo no existe")
