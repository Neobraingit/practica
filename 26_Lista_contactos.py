
Lista_contactos = []
producto = input('Introduce un contacto o escribe "fin": ')

while producto != 'fin':
    Lista_contactos.append(producto)
    producto = input('Introduce un contacto o escribe "fin": ')
    

for item in Lista_contactos:
    print (item)

    