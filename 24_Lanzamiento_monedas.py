import random
monedas = ['cara', 'cruz']
valor = random.choice(monedas)

resultado = input('¿Quires tirar la moneda? ')
if resultado == 'Si':
    print ('La moneda muesta {}'.format(valor))
else:
    print ('Perfecto, otra vez será..x.union')
