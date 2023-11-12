
nombre_archivo = 'archivo.txt'

# Abre el archivo en modo de lectura ('r')
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()

print(contenido)
print (len(contenido))
