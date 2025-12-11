edad = int(input('Cuantos años tienes? '))

if edad >= 100:
    print('Tienes un siglo de vida.')
elif edad >= 18 and edad < 100:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')