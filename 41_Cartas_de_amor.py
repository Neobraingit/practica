import random
print ('Vamos a hacer cartas de amor personalizadas')

nombres = input('Introduce tu nombre: ')

cartas = ['Te quiero más que a nada {}'.format (nombres),'Más guapa ella... mi {}'.format(nombres)]

print (random.choice(cartas))