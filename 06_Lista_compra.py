
# Lista de la compra: Crea una lista de la compra y permite al usuario agregar, eliminar o ver elementos.

lista = ['pan', 'leche', 'tomates']
print ('Decide qué deseas hacer: ')
print ('\n\t',1, 'Añadir')
print ('\n\t',2, 'Eliminar')
print ('\n\t',3, 'Ver\n')
decision = input()

if decision == '1':
    elemento = input('\nIntroduce tu elemento: ')
    lista.append(elemento)
    print (lista)
elif decision == '2':
    elemento_a_borrar = input('Introduce el elemento a borrar de la siguiente lista {}: '.format(lista))
    lista.remove(elemento_a_borrar)
    print (lista)
else:
    print ('La lista de la compra es la siguiente: {}'.format(lista))

