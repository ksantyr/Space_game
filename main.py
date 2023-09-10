import pygame
import sys
import classmeteorito
import classmoneda
import procesado
import cv2
import classjugador
import estados

pygame.init() # inicializamos la libreria de pygame
tamano = (1400,800)  # tamaño de la ventana
ruta_fondo = 'Imagenes/espacio3.jpeg' #ruta de la imagen de fondo
reloj = pygame.time.Clock()

ventana = pygame.display.set_mode(tamano) # creación de la ventana
ventana.fill((255,255,255)) # color blanco en la ventana
fondo = pygame.image.load(ruta_fondo) # imagen de fondo del juego

pygame.display.set_caption("Space Game") #Titulo de la ventana

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

# Fuente para el control de las vidas
font_vidas = pygame.font.Font(None,36)
vidas = 3 
running = True

estado = "inicio"
# Escala la imagen de fondo para que coincida con las dimensiones de la ventana
fondo = pygame.transform.scale(fondo, (1024,800))


while running:
    
    ventana.blit(fondo,(0,0)) # proyección de la imagen de fondo
    for evento in pygame.event.get(): # registro de eventos dentro de la ventana

        if evento.type == pygame.QUIT: # cerrar la ventana
            # Liberar la cámara y cerrar las ventanas
            camara.release()
            cv2.destroyAllWindows()
            pygame.quit()
            sys.exit()
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
        
        elif evento.type == pygame.KEYDOWN: #Revisa si se presiona una tecla
            if estado == "inicio" and evento.key == pygame.K_RETURN:
                estado = "jugando"
            elif estado == "fin" and evento.key == pygame.K_RETURN:
                estado = "jugando"
                vidas = 3
        
            
            
            
    if estado == "inicio": 
        estados.start(ventana,font_punt)
        
        
    elif estado == "jugando":
        running,frame_py, frame_bin= procesado.lectura(jugador, tamano,camara)
        ventana.blit(frame_py, (1024,0))
        ventana.blit(frame_bin, (1024,410))
        
        
        
        #Comprueba una colision del enemigo con el jugador
        colisiones = pygame.sprite.spritecollide(jugador, meteoritos, True)
        if colisiones:
            if vidas > 0:
                vidas -= 1 # secrestan las vidas al detectr colisiones con meteoritos
            if vidas == 0:
                estado = "fin"
       
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
    
        # Mostrar la puntuación en la esquina inferior derecha
        mensaje_puntuacion = font_punt.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        ventana.blit(mensaje_puntuacion, (tamano[0] - 570, tamano[1] - 50))
    
        mensaje_vidas = font_punt.render("Vidas: {}".format(vidas),True,(255,255,255))
        ventana.blit(mensaje_vidas, (tamano[0] - 570, tamano[1] - 100))
        
        
        reloj.tick(250)
        
        
    elif estado == "fin":
        estados.gameOver(ventana,font_punt)
    
    
    
    pygame.display.flip() # actualización de la pantalla
        








