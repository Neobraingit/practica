import random
chistes = ['Va uno y cae el de el medio', ' ¿Qué es un mudo? Una paded de ladrillod']

print ('Opciones: ')
print ('1) Generar un chiste')
print ('2) Añadir un chiste')
print ('3) Eliminar un chiste')
print ('4) Salir')
opcion = input('Dime tu opción: ')

while opcion != '4':
    if opcion == '1':
        print (random.choice(chistes))
        opcion = input('Dime tu opción: ')
    elif opcion == '2':
        elemento = input('Dime el chiste a añadir: ')
        chistes.append(elemento)
        opcion = input('Dime tu opción: ')
    elif opcion == '3':
        elemento_borrar = input('Dime el chiste a eliminar: ')
        chistes.remove(elemento_borrar)
        opcion = input('Dime tu opción: ')
for item in chistes:
    print (chistes)
        
print ('Saliendo del programa...')