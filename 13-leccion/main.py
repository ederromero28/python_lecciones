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

    intentos = 0

    while intentos < 3:
        respuesta = input("¿Quieres continuar? (SI/NO): ").upper()
        
        if respuesta == "SI" or respuesta == "NO":
            break
        else:
            print("Solo tienes dos opciones: SI o NO.")
            intentos += 1
    
    if intentos == 3:
        print("Has agotado tus intentos. Saliendo...")
        break
    
    if respuesta == "NO":
        print("Gracias por usar el programa. Hasta luego.")
        break