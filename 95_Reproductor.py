# Instalamos playsound así : pip3 install playsound

from playsound import playsound


# Hacemos un menú

print ('Escoge la opción que quieras: \n')
print ('1) Escuchar Google\n')
print ('2) Escuchar Soy el único\n')
opcion = input()

# Generamos el cuerpo del programa

if opcion == '1':
    archivo1 = 'oldie.mp3'
    playsound(archivo1)
elif opcion == '2':
    archivo2 = 'oldie2.mp3'
    playsound(archivo2)
else:
    print ('No has elegido ninguna opción.')
    
    
