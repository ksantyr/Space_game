# -*- coding: utf-8 -*-
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self,tamano):
        super().__init__() #Verifica que se inicialice todo correctamente y permite heredar de la clase
        # Cargar la imagen del jugador
        self.image = pygame.image.load('Imagenes/cohete.png')  # Carga una imgagen (cohete) que representa el jugador      
        #Se genera en el centro de la ventana
        self.rect = self.image.get_rect() #Crea un rectangulo con las mismas dimensiones de
        self.pos_x = 1024//2 # posición en x en la ventana(centro)
        self.pos_y = 700 # posición en y en la ventana(centro)
        #la superficie anterior, el jugador y sus dimensiones esta almacenado en rect
        self.tamano_ventana =tamano#itupla que contiene el tamaño de la ventana ancho=tamano(0), alto=tamano(1)
        #Coordenadas actualizables 
        self.cX = self.pos_x
        self.cY = self.pos_y
        #Inicia en el centro de la pantalla
        self.rect.center = (self.pos_x // 2, self.pos_y // 2) 
    
    def posicion (self,x,y):
        self.cX = x
        self.cY = y

    def update(self):
        self.rect.x = self.cX
        self.rect.y = self.cY
            
        # Actualizar la posición del jugador con límites en los bordes de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1024:
            self.rect.right = 1024
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.tamano_ventana[1]:
            self.rect.bottom = self.tamano_ventana[1]
    
    def __del__(self): # destructor
        print('cohete eliminado')
