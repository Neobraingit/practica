
lista_tareas = []

print ('Introduce una opción: ')
print ('1) Agregar tarea')
print ('2) Eliminar tarea')
print ('"Salir" para cerrar el programa')

opcion = input()


if opcion == '1':
        tarea = input('Introduce la tarea: ')
        lista_tareas.append(tarea)
elif opcion == '2':
        tarea_borrar = input('Escribe la tarea a eliminar: ')
else:
    print ('Saliendo del programa...')
    
print (lista_tareas)

