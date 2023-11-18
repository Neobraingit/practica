cadena = "Hola, mundo!"

# Crear un diccionario para almacenar la ocurrencia de caracteres
ocurrencias = {}

# Iterar a través de cada caracter en la cadena
for caracter in cadena:
    # Verificar si el caracter ya está en el diccionario
    if caracter in ocurrencias:
        # Incrementar la cuenta si el caracter ya está presente
        ocurrencias[caracter] += 1
    else:
        # Agregar el caracter al diccionario si no está presente
        ocurrencias[caracter] = 1

# Imprimir el resultado
for caracter, count in ocurrencias.items():
    print(f"El caracter '{caracter}' aparece {count} veces.")

