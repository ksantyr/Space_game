import pygame
import sys
import classmeteorito

pygame.init() # inicializamos la libreria de pygame
tamaño = (1400,800)  # tamaño de la ventana
ruta_fondo = 'Imagenes/espacio3.jpeg' #ruta de la imagen de fondo
reloj = pygame.time.Clock()

ventana = pygame.display.set_mode(tamaño) # creación de la ventana
ventana.fill((255,255,255)) # color blanco en la ventana
fondo = pygame.image.load(ruta_fondo).convert() # imagen de fondo del juego

meteoritos = [classmeteorito.Meteorito()] #lista con todos los metehoritos generados

# Configuración del temporizador para generar objetos
GENERATE_OBJECT_EVENT = pygame.USEREVENT + 1  # Evento personalizado
pygame.time.set_timer(GENERATE_OBJECT_EVENT, 1300)  # Generar cada 1.3 segundos (1300 milisegundos)

while True:
    ventana.blit(fondo,[0,0]) # proyección de la imagen de fondo     
    for evento in pygame.event.get(): # registro de eventos dentro de la ventana
        if evento.type == pygame.QUIT: # cerrar la ventana
            sys.exit()
        elif evento.type == GENERATE_OBJECT_EVENT: # registro de la generación de las monedas
            meteoritos.append(classmeteorito.Meteorito()) # generamos un meteorito

    for i in meteoritos: # actualizamos la posicón de los meteorito
        i.actualizacion_pos(ventana)

    pygame.display.flip() # actualización de la pantalla
    reloj.tick(250)

for i in meteoritos: # destrucción de objetos
    del i
pygame.quit()