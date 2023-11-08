#  Adivina el número: Genera un número aleatorio y pide al usuario que lo adivine.

import random

usuarionumero = int(input('Adivina el número secreto: '))
numero = random.randint(0, 10)


while usuarionumero != numero:
    print ('Prueba otra vez...')
    usuarionumero = int(input('Adivina el número secreto: '))
else:
    print ('Enhorabuena¡¡ Has acertado el número {}'.format(numero))


