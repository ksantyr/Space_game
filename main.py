import pygame
import sys
import classmeteorito
import classmoneda
pygame.init() # inicializamos la libreria de pygame
tamaño = (1400,800)  # tamaño de la ventana
ruta_fondo = 'Imagenes/espacio3.jpeg' #ruta de la imagen de fondo
reloj = pygame.time.Clock()

ventana = pygame.display.set_mode(tamaño) # creación de la ventana
ventana.fill((255,255,255)) # color blanco en la ventana
fondo = pygame.image.load(ruta_fondo).convert() # imagen de fondo del juego

meteoritos = [classmeteorito.Meteorito()] # lista con todos los metehoritos generados

# Configuración del temporizador para meteoritos
generador_meteoritos = pygame.USEREVENT + 1  # Evento personalizado
pygame.time.set_timer(generador_meteoritos, 1300)  # Generar cada 1.3 segundos (1300 milisegundos)

monedas = [classmoneda.Moneda()] # lista con todos las monedas generadas

# configuración del temporizador para las monedas
generador_monedas = pygame.USEREVENT + 2  # Evento personalizado
pygame.time.set_timer(generador_monedas, 3000)  # Generar cada 3 segundos (3000 milisegundos)

while True:
    ventana.blit(fondo,[0,0]) # proyección de la imagen de fondo     
    for evento in pygame.event.get(): # registro de eventos dentro de la ventana
        if evento.type == pygame.QUIT: # cerrar la ventana
            sys.exit()
        elif evento.type == generador_meteoritos: # registro de la generación de los meteoritos
            meteoritos.append(classmeteorito.Meteorito()) # generamos un meteorito
        
        elif evento.type == generador_monedas:# registro de la generación de las monedas
            monedas.append(classmoneda.Moneda())# generamos una moneda

    for i in meteoritos: # actualizamos la posicón de los meteorito
        i.actualizacion_pos(ventana)
    
    for j in monedas: # actualizamos la posicón de las monedas
        j.actualizacion_pos(ventana)

    pygame.display.flip() # actualización de la pantalla
    reloj.tick(250)

for i in meteoritos: # destrucción de los meteoritos
    del i

for i in monedas: # destruccion de las monedas creadas
    del i

pygame.quit()