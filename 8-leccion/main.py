nombre = "Eder Code"
primer_nombre = nombre[0:4]

apellido = nombre[5:9]
nombre_dos = nombre[0:9:2]

nombre_invertido = nombre[::-1]

website = "https://www.garena-delta-force.com"

slice = slice(12, -4)
sitioWeb = website[slice]


# print(primer_nombre)  # Salida: Eder
# print(nombre_dos)
# print(nombre_invertido)  # Salida: edoC redE
print(sitioWeb)