# OPERADORES LOGICOS

temperatura = int(input("Ingrese la temperatura actual: "))

# if temperatura > 30 and temperatura <= 40:
#     print("Hace calor")
# elif temperatura >= 20 and temperatura <= 30:
#     print("Hace una temperatura agradable")
# elif temperatura >= 10 and temperatura < 20:
#     print("Hace fresco")
# else:
#     print("Hace frio")

if not(temperatura >= 0 and temperatura <= 30):
    print("La temperatura esta mal hoy")
elif not (temperatura < 0 or temperatura > 30):
    print("La temperatura esta bien hoy")

