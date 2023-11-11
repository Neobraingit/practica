
import pygame
pygame.init()
 
ancho = 640
alto = 480
 
pantalla = pygame.display.set_mode( (ancho, alto) )
 
imagen = pygame.image.load("spaceinvader.png")
rectanguloImagen = imagen.get_rect()
 
rectanguloImagen.left = 300
rectanguloImagen.top = 200
 
pantalla.fill( (0,0,0) )
pantalla.blit(imagen, rectanguloImagen)
pygame.display.flip()
pygame.time.wait(5000)
 
pygame.quit()