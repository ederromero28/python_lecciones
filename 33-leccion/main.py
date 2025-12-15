
texto = '\nWooooooo'


# ('E:\\PP\\texto2.txt', 'w') sobre escribe (write) y borra el contenido anterior
# ('E:\\PP\\texto2.txt', 'a') agrega (append) el nuevo contenido al final del archivo

with open ('E:\\PP\\texto2.txt', 'w') as file:
    contenido = file.write(texto)   
    print (contenido)