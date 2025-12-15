try:
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))

    resultado = numerador / denominador

except ZeroDivisionError as e:
    print(e)
    print("Error: No se puede dividir por cero.")

except ValueError as e:
    print(e)
    print("Error: Entrada inválida. Por favor, ingrese números enteros.")

except Exception as e:
    print(e)
    print("Se produjo un error al realizar la división.")

else:
    print(resultado)
finally:
    print("Esto se ejecuta siempre, haya o no error.")