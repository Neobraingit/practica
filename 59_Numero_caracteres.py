
archivo = 'archivo.txt'

def numero_caracteres(archivo):
    with open (archivo, 'r') as miarchivo:
        contenido = miarchivo.read()
        print (len(contenido))
       
        
numero_caracteres(archivo)