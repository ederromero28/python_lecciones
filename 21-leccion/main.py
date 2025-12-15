# def saludo():
#     print("¡Hola! Bienvenido a la lección 21.")
#     print("Que tengas un buen día aprendiendo Python.")

# saludo()


# def saludo(nombre):
#     print("¡Hola, " + nombre + "! Bienvenido a la lección 21.")
#     print("Que tengas un buen día aprendiendo Python.")

# saludo("Eder")

def saludo(a,b,c,d):
    print("¡Hola, " + a + " " + b + "! Bienvenido a la lección 21.")
    print("Que tengas un buen día aprendiendo Python.")
    print("Tu edad es: " + str(c))
    print("Tu ciudad es: " + d)

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")

saludo(nombre, apellido, edad, ciudad)