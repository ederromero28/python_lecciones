capitales = {
    'EE.UU.': 'Washington D.C.',
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Colombia': 'Bogotá',
    'cursos' : ['Python', 'JavaScript', 'Java'],
    'años': 2024
}

# print(capitales.get('Argentina'))  # Output: Buenos Aires
# print(capitales.keys())  # Output: dict_keys(['EE.UU.', 'Argentina', 'Brasil', 'Colombia'])
# print(capitales.values())  # Output: dict_values(['Washington D.C.', 'Buenos Aires', 'Brasilia', 'Bogotá'])
# print(capitales.items())  # Output: dict_items([('EE.UU.', 'Washington D.C.'), ('Argentina', 'Buenos Aires'), ('Brasil', 'Brasilia'), ('Colombia', 'Bogotá')])
capitales.update({'Perú': 'Lima'})
capitales.pop('Brasil')
# capitales.clear()

for key,value in capitales.items():
    print(f'La capital de {key} es {value}')