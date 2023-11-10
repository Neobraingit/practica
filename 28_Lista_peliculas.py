
import signal , sys
lista_peliculas = []
peliculas = input('Introduce la película a añadir o escribe "fin": ')

while peliculas != 'fin':
    lista_peliculas.append(peliculas)
    peliculas = input('Introduce la película a añadir o escribe "fin": ')

    
for item in lista_peliculas:
 print (item)
 
 
