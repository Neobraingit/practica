
'''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
 '''
 
def contar_palabras(frase):
    # Convertir la frase a minúsculas y dividirla en palabras
    palabras = frase.lower().split()

    # Crear un diccionario para almacenar el recuento de cada palabra
    recuento = {}

    # Iterar sobre cada palabra y actualizar el recuento
    for palabra in palabras:
        # Eliminar signos de puntuación al final de la palabra
        palabra = palabra.strip('.,!?()[]{}"\'')
        
        # Incrementar el recuento de la palabra en el diccionario
        recuento[palabra] = recuento.get(palabra, 0) + 1

    return recuento

def main():
    # Ingresar la frase desde el usuario
    frase = input("Ingrese una frase: ")

    # Obtener el recuento de palabras
    recuento = contar_palabras(frase)

    # Mostrar el recuento final
    print("\nRecuento final de palabras:")
    for palabra, cantidad in recuento.items():
        print(f"{palabra}: {cantidad}")

if __name__ == "__main__":
    main()

        