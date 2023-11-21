# Instalamos playsound así : pip3 install playsound

from playsound import playsound


# Hacemos un menú

print ('Escoge la opción que quieras: \n')
print ('1) Escuchar Google\n')
print ('2) Escuchar Soy el único\n')
opcion = input()

# Generamos el cuerpo del programa

if opcion == '1':
    archivo1 = 'ruta/al/archivo.mp3'
    playsound('ruta_archivo')
elif opcion == '2':
    archivo2 = 'ruta/al/archivo2.mp3'
else:
    print ('No has elegido ninguna opción.')
    
    
