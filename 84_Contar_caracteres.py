
def contar (cadena):
    numeros = 0
    letras = 0
    for i in cadena:
        if i.isalpha():
            letras += 1
        elif i.isdigit():
            numeros += 1
    print ('{} tiene {} letras y {} números'.format(cadena, letras, numeros))
    
    
contar('Me llamo Marcos2345')