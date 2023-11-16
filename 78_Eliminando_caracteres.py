
cadena = input('Introduce la cadena de caracteres: ')
elemento_a_eliminar = input('Introduce el caracter que deseas eliminar: ')
elementos_eliminados = []

if elemento_a_eliminar in cadena:
    print (cadena.replace(elemento_a_eliminar, ' '))
    elementos_eliminados.append(elemento_a_eliminar)
    
    print (elementos_eliminados)

    