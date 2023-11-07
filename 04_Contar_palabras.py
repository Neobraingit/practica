# Contador de palabras: Cuenta la cantidad de palabras en una cadena de texto.

cadena = input('Introduce una cadena de texto: ')

for i in cadena:
    total = len(cadena.split(' '))
print ('La cadena contiene {} palabras.'.format(total))