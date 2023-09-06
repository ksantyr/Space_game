import pygame
import sys


pygame.init() # inicializamos la libreria de pygame
tamaño = (1000,800)  # tamaño de la ventana

ruta_fondo = 'Imagenes/espacio3.jpeg' #ruta de la imagen de fondo

ventana = pygame.display.set_mode(tamaño) # creación de la ventana
fondo = pygame.image.load(ruta_fondo).convert() # imagen de fondo del juego

while True:

    ventana.blit(fondo,[0,0]) # proyección de la imagen

    for evento in pygame.event.get(): # registro de eventos dentro de la ventana
        if evento.type == pygame.QUIT: # cerrar la ventana
            sys.exit()
    
    pygame.display.flip() # actualización de la pantalla

pygame.quit()