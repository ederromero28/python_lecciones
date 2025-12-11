# fila = int(input("Ingrese el número de filas: "))
# columna = int(input("Ingrese el número de columnas: "))
# simbolo = input("Ingrese el símbolo a utilizar: ")

# for i in range(fila):
#     for j in range(columna):
#         print(simbolo, end="")
#     print()  # Salto de línea después de cada fila


while True:
    fila = int(input("Ingrese el número de filas: "))
    columna = int(input("Ingrese el número de columnas: "))
    simbolo = input("Ingrese el símbolo a utilizar: ")

    for i in range(fila):
        for j in range(columna):
            print(simbolo, end="")
        print()  # Salto de línea después de cada fila

    respuesta = input("¿Quieres continuar? (SI/NO): ").upper()

    if respuesta == "NO":
        break