
def contar_letras_digitos(cadena):
    letras = 0
    digitos = 0
    for caracter in cadena:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            digitos += 1
    return letras, digitos

# Ejemplo de uso
resultado = contar_letras_digitos("Me llamo Marcos")
print(resultado)  # Debería imprimir (8, 6)
