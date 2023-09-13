#-------------------------------------------------------------------------------------------------
#------- Juego Yellow Ball -----------------------------------------------------------------------
#------- Coceptos básicos de PDI------------------------------------------------------------------
#------- Por: Victor Manuel Arbeláez Ramírez  victor.arbelaez@udea.edu.co ------------------------
#-------      Kevin Santiago Restrepo Alzate  Kevin.restrepo2@udea.edu.co-------------------------
#------- Presentado a: David Stephen Fernández MC CAN --------------------------------------------
#-------      Profesor Facultad de Ingenieria BLQ 21-409  ----------------------------------------
#-------      CC 71629489, Tel 2198528,  Wpp 3007106588 ------------------------------------------
#------- Curso Básico de Procesamiento de Imágenes y Visión Artificial----------------------------
#------- Septiembre de 2023-----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------
#--1. Inicializo el sistema ----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

import pygame
import sys
import classmeteorito
import classmoneda
import procesado
import cv2
import classjugador
import estados

pygame.init() # inicializamos la libreria de pygame

#-------------------------------------------------------------------------------------------------
#--2. Inicialización de las variables y funciones del juego --------------------------------------
#-------------------------------------------------------------------------------------------------

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
dificultad = 1300 # variable que controla el tiempo de aparición de los meteoritos
pygame.time.set_timer(generador_meteoritos,dificultad)  # Generar cada 1.3 segundos (1300 milisegundos)
sonido_meteorito = pygame.mixer.Sound("sonidos/asteroid-hitting-something-152511.mp3") # sonido de colision con meteorito


#monedas = [classmoneda.Moneda()] # lista con todos las monedas generadas
monedas = pygame.sprite.Group() #Grupo con todos los objetos de monedas

# configuración del temporizador para las monedas
generador_monedas = pygame.USEREVENT + 2  # Evento personalizado
pygame.time.set_timer(generador_monedas, 3000)  # Generar cada 3 segundos (3000 milisegundos)
sonido_monedas = pygame.mixer.Sound("sonidos/moneda.mpeg")

#Grupo con todos los sprites
sprites = pygame.sprite.Group()

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

#condiciones iniciales del bucle principal
estado = "inicio"
validar = 0

# Configuracion de 3 canalas pera reproducie sonidos simultaneos
pygame.mixer.set_num_channels(3)
sonido_juego = pygame.mixer.Sound("sonidos/juego.mpeg")
sonido_inicio = pygame.mixer.Sound("sonidos/inicio.mpeg")
timer_sonido = pygame.USEREVENT + 3 # evento para reproducir la musica de fondo de forma indefinida
# canales de reproducción de sonido
canal1 = pygame.mixer.Channel(0)
canal2 = pygame.mixer.Channel(1)
canal3 = pygame.mixer.Channel(2)
pygame.time.set_timer(timer_sonido,90000)  # Se repite al finalizar la canción

#-------------------------------------------------------------------------------------------------
#------------------------------------ INICIO DEL JUEGO -------------------------------------------
#-------------------------------------------------------------------------------------------------

while running:
    
    for evento in pygame.event.get(): # registro de eventos dentro de la ventana

        if evento.type == pygame.QUIT: # cerrar la ventana
            # Liberar la cámara y cerrar las ventanas
            camara.release()
            cv2.destroyAllWindows()
            pygame.quit()
            sys.exit()
            running = False

        elif evento.type == generador_meteoritos and estado == "jugando": # registro de la generación de los meteoritos
            #meteoritos.append(classmeteorito.Meteorito()) # generamos un meteorito
            meteorito = classmeteorito.Meteorito(tamano) #Genera un objeto meteorito
            meteoritos.add(meteorito) #lo añade al grupo de meteoritos
            sprites.add(meteorito) #lo añade al grupo que contiene todos los sprites
            
        elif evento.type == generador_monedas and estado == "jugando":# registro de la generación de las monedas
            #monedas.append(classmoneda.Moneda())# generamos una moneda
            moneda = classmoneda.Moneda(tamano) #Genera un objeto moneda
            monedas.add(moneda)#lo añade al grupo de monedas
            sprites.add(moneda) #lo añade al grupo que contiene todos los sprites
        
        elif evento.type == pygame.KEYDOWN: #Revisa si se presiona una tecla
            canal1.play(sonido_juego)
            if estado == "inicio" and evento.key == pygame.K_RETURN:
                estado = "jugando"
                jugador  = classjugador.Jugador(tamano)
                sprites.add(jugador)
            elif estado == "fin" and evento.key == pygame.K_RETURN: # reestablecemos valores
                jugador  = classjugador.Jugador(tamano)
                sprites.add(jugador)
                estado = "jugando"
                vidas = 3
                puntuacion = 0
                dificultad = 1300
        
        if evento.type == timer_sonido and estado == "jugando": # control de reproducción del audio de juego
             canal1.play(sonido_juego)
        

    if estado == "inicio": 
        
        estados.start(ventana,font_punt)
        if validar == 0: # se reproduce solo una vez el sonido inicial
            # sonido de inicio
            sonido_inicio.play()
            validar = 1
        
    elif estado == "jugando":
        ventana.blit(fondo,(0,0)) # proyección de la imagen de fondo
        running,frame_py, frame_bin= procesado.lectura(jugador, tamano,camara)
        # ubicacion de las camaras
        ventana.blit(frame_py, (1024,0)) 
        ventana.blit(frame_bin, (1024,410))
        
        #Comprueba una colision del enemigo con el jugador
        colisiones = pygame.sprite.spritecollide(jugador, meteoritos, True)
        if colisiones:
            canal2.play(sonido_meteorito) # reproducir sonido de la colision
            if vidas > 0:
                vidas -= 1 # secrestan las vidas al detectr colisiones con meteoritos
            if vidas == 0:
                estado = "fin"
       
        # Verificar colisión con nedasmo y actualizar la puntuación, el true elimina el enemigo verde de la pantalla
        colisiones_monedas = pygame.sprite.spritecollide(jugador, monedas, True) #Devuelve una lista con el numero de colisiones
        if colisiones_monedas:
            canal3.play(sonido_monedas) # sonido al detectar colisiones
            #Revisa con cuantas colisiono y multiplica por 10 (para dar la puntuacion en multiplos de 10)
            puntuacion += (len(colisiones_monedas)) * 10
            #Cada moneda da 10 puntos
            if puntuacion % 50 == 0: # se aumenta la aparición cada 50 puntos
                if dificultad > 450: # se establece limite
                    pygame.time.set_timer(generador_meteoritos,dificultad)  # actualizamos el timer para generar los objetos
                    dificultad -= 150 #se disminuye en 150 milisegundos
            
        #Actualizar la posicion de todos los sprites
        sprites.update()
        # Dibujar todos los sprites en la pantalla
        sprites.draw(ventana)
    
        # Mostrar la puntuación en la esquina inferior derecha
        mensaje_puntuacion = font_punt.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        ventana.blit(mensaje_puntuacion, (tamano[0] - 570, tamano[1] - 50))

        # Mostrar las vidas en la esquina inferior derecha
        mensaje_vidas = font_punt.render("Vidas: {}".format(vidas),True,(255,255,255))
        ventana.blit(mensaje_vidas, (tamano[0] - 570, tamano[1] - 100))

        reloj.tick(250)
        
    elif estado == "fin":
        estados.gameOver(ventana,font_punt,puntuacion)
        for i in sprites: # destruccion de objetos
            i.__del__()
        for i in meteoritos:
            i.__del__()
        sprites.empty() 
        meteoritos.empty()
    pygame.display.flip() # actualización de la pantalla