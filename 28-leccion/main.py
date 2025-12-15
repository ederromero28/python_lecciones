# str.format() =

str_1 = 'leche'
str_2 = 'casar'

# print('Arroz con leche me quiero casar')
# print('Arroz con ' + str_1 + ' me quiero ' + str_2)
# print('Arroz con {0} me quiero {1}'.format(str_1, str_2))
# print('Arroz con {str_1} me quiero {str_2}'.format(str_1 = str_1, str_2 = str_2))

texto = 'Arroz con {} me quiero {}'

# print(texto.format(str_1, str_2))

nombre = 'Eder'
# print('Hola mi nombre es {0}'.format(nombre))
# print('Hola mi nombre es {:10}. Mucho gusto'.format(nombre))
# print('Hola mi nombre es {:<10}. Mucho gusto'.format(nombre))
# print('Hola mi nombre es {:>10}. Mucho gusto'.format(nombre))
# print('Hola mi nombre es {:^10}. Mucho gusto'.format(nombre))

# numero = 3.14159

# print('El numero PI es: {:.2f}'.format(numero))

numero = 1000

# print('El numero es: {:.2f}'.format(numero))
# print('El numero es: {:b}'.format(numero))
# print('El numero es: {:o}'.format(numero))
# print('El numero es: {:x}'.format(numero))
print('El numero es: {:e}'.format(numero))
