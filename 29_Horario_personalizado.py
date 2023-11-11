
from datetime import datetime, date, time

print ('Dime la hora que es en este momento: ')
print (datetime.now())

eventos = []
opcion = input('Escribe un evento o escribe "fin": ')

while opcion != 'fin':
    eventos.append(opcion)
    opcion = input('Escribe un evento o escribe "fin": ')

for i in eventos:
    print (i)
    