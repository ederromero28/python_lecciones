nombre = ''

# while len(nombre) == 0:
#     nombre = input("Por favor, ingresa tu nombre: ")

while not nombre or len(nombre) == 0:
    nombre = input("Por favor, ingresa tu nombre: ")

print('Hola ' + nombre)