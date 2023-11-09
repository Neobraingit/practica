


# Ingresar la palabra para verificar
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Eliminar espacios en blanco y convertir a minúsculas
palabra = palabra.replace(" ", "").lower()

# Verificar si la palabra es un palíndromo
es_palindromo = palabra == palabra[::-1]

# Mostrar el resultado
if es_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

    

    