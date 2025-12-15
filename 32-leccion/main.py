try:
    with open ('E:\\PP\\texto.txt') as file:
        contenido = file.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")