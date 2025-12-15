def hola(**kwargs):
    # print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ' ' + kwargs['segundo_nombre'])
    print('Hola' , end=' ')
    for clave, valor in kwargs.items():
        print(valor, end=' ')

hola(titulo='joven', nombre='Eder', apellido='Romero', segundo_nombre='Python')