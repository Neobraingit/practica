def vocal_mas_comun(cadena):
    # Convertir la cadena a minúsculas para considerar mayúsculas y minúsculas iguales
    cadena = cadena.lower()
    
    # Definir las vocales
    vocales = "aeiou"
    
    # Inicializar un diccionario para contar la frecuencia de cada vocal
    frecuencia_vocales = {vocal: 0 for vocal in vocales}
    
    # Contar la frecuencia de cada vocal en la cadena
    for letra in cadena:
        if letra in vocales:
            frecuencia_vocales[letra] += 1
    
    # Encontrar la vocal más común
    vocal_mas_comun = max(frecuencia_vocales, key=frecuencia_vocales.get)
    
    return vocal_mas_comun

# Ejemplo de uso
cadena_ejemplo = "Hola, ¿cómo estás?"
resultado = vocal_mas_comun(cadena_ejemplo)
print("La vocal más común es:", resultado)

        