import pygame
import sys
import classmeteorito
import classmoneda
import procesado
import cv2
import classjugador

pygame.init() # inicializamos la libreria de pygame
tamano = (1400,800)  # tamaño de la ventana
ruta_fondo = 'Imagenes/espacio3.jpeg' #ruta de la imagen de fondo
reloj = pygame.time.Clock()

ventana = pygame.display.set_mode(tamano) # creación de la ventana
#ventana.fill((255,255,255)) # color blanco en la ventana
fondo = pygame.image.load(ruta_fondo).convert() # imagen de fondo del juego
# Redimensiona la imagen de fondo para que coincida con las dimensiones de la ventana
fondo = pygame.transform.scale(fondo, tamano)

pygame.display.set_caption("Space Game") #Titulo de la ventana

#meteoritos = [classmeteorito.Meteorito()] # lista con todos los metehoritos generados

meteoritos = pygame.sprite.Group() #Grupo con todos los objetos de meteoritos

# Configuración del temporizador para meteoritos
generador_meteoritos = pygame.USEREVENT + 1  # Evento personalizado
pygame.time.set_timer(generador_meteoritos, 1300)  # Generar cada 1.3 segundos (1300 milisegundos)

#monedas = [classmoneda.Moneda()] # lista con todos las monedas generadas
monedas = pygame.sprite.Group() #Grupo con todos los objetos de monedas

# configuración del temporizador para las monedas
generador_monedas = pygame.USEREVENT + 2  # Evento personalizado
pygame.time.set_timer(generador_monedas, 3000)  # Generar cada 3 segundos (3000 milisegundos)

#Grupo con todos los sprites

sprites = pygame.sprite.Group()

jugador  = classjugador.Jugador(tamano)
sprites.add(jugador)

# Inicializar la cámara (por defecto)
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Fuente para el contador de puntos 
font_punt = pygame.font.Font(None, 36)
puntuacion = 0 #Variable que controla la puntuacion

running = True
while running:
    ventana.blit(fondo,[0,0]) # proyección de la imagen de fondo
         
    for evento in pygame.event.get(): # registro de eventos dentro de la ventana
        if evento.type == pygame.QUIT: # cerrar la ventana
            #sys.exit()
            running = False
        elif evento.type == generador_meteoritos: # registro de la generación de los meteoritos
            #meteoritos.append(classmeteorito.Meteorito()) # generamos un meteorito
            meteorito = classmeteorito.Meteorito(tamano) #Genera un objeto meteorito
            meteoritos.add(meteorito) #lo añade al grupo de meteoritos
            sprites.add(meteorito) #lo añade al grupo que contiene todos los sprites
            
        
        elif evento.type == generador_monedas:# registro de la generación de las monedas
            #monedas.append(classmoneda.Moneda())# generamos una moneda
            moneda = classmoneda.Moneda(tamano) #Genera un objeto moneda
            monedas.add(moneda)#lo añade al grupo de monedas
            sprites.add(moneda) #lo añade al grupo que contiene todos los sprites
            

    
    #sprites.update(ventana)
    running= procesado.lectura(jugador, tamano,camara)
    
    #Comprueba una colision del enemigo con el jugador
   
    colisiones = pygame.sprite.spritecollide(jugador, meteoritos, False)
    if colisiones:
        print("game Over")
   

    # Verificar colisión con nedasmo y actualizar la puntuación, el true elimina el enemigo verde de la pantalla
    colisiones_monedas = pygame.sprite.spritecollide(jugador, monedas, True) #Devuelve una lista con el numero de colisiones
    if colisiones_monedas:
        #Revisa con cuantas colisiono y multiplica por 10 (para dar la puntuacion en multiplos de 10)
        puntuacion += (len(colisiones_monedas)) * 10
        #Cada moneda da 10 puntos
        
        
        
    
     
    #Actualizar la posicion de todos los sprites
    sprites.update()
    # Dibujar todos los sprites en la pantalla
    sprites.draw(ventana)
    #sprites.draw(ventana)
    #sprites.draw(ventana)
    """
    for i in meteoritos: # actualizamos la posicón de los meteorito
        i.actualizacion_pos(ventana)
    
    for j in monedas: # actualizamos la posicón de las monedas
        j.actualizacion_pos(ventana)
    """

    # Mostrar la puntuación en la esquina inferior derecha
    mensaje_puntuacion = font_punt.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    ventana.blit(mensaje_puntuacion, (tamano[0] - 300, tamano[1] - 50))
    
    pygame.display.flip() # actualización de la pantalla
    reloj.tick(250)

#meteoritos.pop()
#monedas.pop()
#meteoritos.remove()
#monedas.remove()

"""
for i in meteoritos: # destrucción de los meteoritos
    del i

for i in monedas: # destruccion de las monedas creadas
    del i
"""

# Liberar la cámara y cerrar las ventanas
camara.release()
cv2.destroyAllWindows()


# Salir del juego con esc por defecto 
pygame.quit()
sys.exit()