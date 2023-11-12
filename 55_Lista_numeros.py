
print ('Vamos a crear una lista de números¡¡')
lista = []

while  True:
    if len(lista) < 10:
        numero = float(input('Añade un número: '))
        lista.append(numero)
        print (lista)
    else:
        print ('Saliendo del programa...')
        break