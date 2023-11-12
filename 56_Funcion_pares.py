
lista = [1, 2, 3, 4, 5, 6, 7, 8]

def numeros_pares(lista):
    pares = []
    for item in lista:
        if item % 2 == 0:
            pares.append(item)
    print (pares)

numeros_pares(lista)