archivo = open('prueba.txt', 'r', encoding='utf8')  # Las letras son: 'r' read, 'a' append, 'w' write, 'x'
# print(archivo.read())
# print(archivo.read(16))
# print(archivo.read(5))
# print(archivo.readline())

# Vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
    # print(linea)
#print(archivo.readlines()[12])# accedemos al archivo como si fuera una lista

# Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primero
archivo2.close() # cerramos el segundo

print('Se ha terminado el proceso de leer y copar archivos')
