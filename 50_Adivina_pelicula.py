import random
peliculas = ['Terminator', 'Regreso al futuro', 'Robocop']
pistas = 'Robot que viene del futuro', 'Michael .J .Fox', 'Robot policía'

print (input('Apreta una tecla para generar una descripción: '))



opcion = random.choice(pistas)
print (opcion)
respuesta = input('Dime tu respuesta: ')

if respuesta == peliculas[0]:
        print ('Has acertado')
elif respuesta == peliculas[1]:
        print ('Has acertado')
elif respuesta == peliculas[2]:
        print ('Has acertado')
else:
        print ('Lo siento, has fallado¡¡')
    
  
