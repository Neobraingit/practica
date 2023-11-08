# Tareas pendientes

print ('LISTA DE TAREAS')
print ('1) Agregar\n')
print ('2) Eliminar\n')
print ('3) Completar\n')
print ('Elige tu opción: ')
opcion = input()
lista = ['Trabajar', 'correr', 'dormir']

if opcion == '1':
    elemento = input('Introduce algo: ')
    lista.append(elemento)
    print (lista)
elif opcion == '2':
    elemento = input('Qué elemento quieres borrar: ')
    lista.remove(elemento)
    print (lista)
else:
    print ('Has completado la lista¡¡')
    
