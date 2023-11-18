
contraseña = 'admin123'
while True:
 respuesta = input('Introduce la contraseña: ')
 if respuesta == contraseña:
    print ('Adelante, puedes pasar...')
    break
 else:
    print ('Inténtalo otra vez: ')
    respuesta = input('Introduce la contraseña: ')

    