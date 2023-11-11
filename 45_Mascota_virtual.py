import random

print ('VAMOS A CUIDAR DE TU MASCOTA¡¡')

necesidades = ['Limpieza', 'Baño', 'Caca', 'Pis']
necesidades_nuevas = []

opcion = input('Si quieres saber qué necesita tu mascota pulsa una tecla: . Si quieres salir escribe "Salir" ')


solucion = random.choice(necesidades)

if solucion == 'Limpieza':
    print (solucion)
    print ('Lavando...')
elif solucion == 'Baño':
    print (solucion)
    print ('Duchándose...')
elif solucion == 'Caca':
    print (solucion)
    print ('Usando papel...')
elif solucion == 'Pis':
    print (solucion)
    print ('Sacándose la minga...')

print ('Saliendo del programa...')
 


