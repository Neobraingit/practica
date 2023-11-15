
palabras_a_adivinar = ['Perro', 'Gato', 'Mesa', 'Silla']


def acertar():
    while True:
     respuesta = input('Introduce la palabra a adivinar: ')
     if respuesta == palabras_a_adivinar[1]:
        print ('Has acertado¡¡')
     elif respuesta == palabras_a_adivinar[0]:
        print ('Has acertado¡¡')
     elif respuesta == palabras_a_adivinar[2]:
        print ('¡Has acertado¡¡')
     elif respuesta == palabras_a_adivinar[3]:
        print ('¡Has acertado¡¡')
     else:
        print ('Intentalo otra vez ')




acertar()