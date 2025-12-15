def suma(*cosas):
    suma = 0
    cosas = list(cosas)
    cosas[1] = 0

    for i in cosas:
        suma += i
    return suma
print(suma(1, 2, 3, 4, 5))  # Debería imprimir 13