
lista_de_libros = []

print ('ESCOGE UNA OPCIÓN: ')
print ('1) Agregar libro')
print ('2) Eliminar libro')
print ('"Salir" para cerrar el programa')
opcion = input('Dime tu opción: ')

while opcion != 'Salir':
    if opcion == '1':
        elemento = input('Dime tu libro: ')
        lista_de_libros.append(elemento)
        opcion = input('Dime tu opción: ')
        
        
    elif opcion == '2':
        elemento_a_borrar = input('Dime tu libro: ')
        lista_de_libros.remove(elemento_a_borrar)
        opcion = input('Dime tu opción: ')
        
    elif opcion == 'Salir':
        print ('SALIENDO DEL PROGRAMA...¡ADIOS!')

        
        
for item in lista_de_libros:
    print (item)
        
        
