
# Abrir el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()

# Dividir el contenido en palabras usando split()
palabras = contenido.split()

# Contar el número de palabras
num_palabras = len(palabras)

# Imprimir el resultado
print(f"El archivo tiene {num_palabras} palabras.")

