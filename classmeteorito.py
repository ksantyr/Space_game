import pygame
import random

class Meteorito:

    def __init__(self): # atributos del objeto
        self.imagen = pygame.image.load('Imagenes/meteorito.png') #imagen del meteorito
        self.pos_x = random.randint(100,700) # posición en x en la ventana
        self.pos_y = 0 # posición en y en la ventana
        self.velocidad = 3 # velocidad
        self.rect = self.imagen.get_rect() #se rellena la imagen como un rectangulo con el fin de gestionar las colisiones

    def actualizacion_pos(self,ventana):
        
        
        ventana.blit(self.imagen,[self.pos_x,self.pos_y])# proyección de la imagen
        pygame.display.flip() # actualización de la ventana 
        self.pos_y += self.velocidad # actualizacion de la posición
    
    def __del__(self): # destructor
        self.y = 900