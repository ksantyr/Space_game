import pygame
import random

class Moneda:

    def __init__(self): # atributos del objeto
        self.imagen = pygame.image.load('Imagenes/moneda.png') #imagen de la moneda
        self.pos_x = random.randint(50,750) # posición en x en la ventana
        self.pos_y = 0 # posición en y en la ventana
        self.velocidad = 1 # velocidad
        self.rect = self.imagen.get_rect() #se rellena la imagen como un rectangulo con el fin de gestionar las colisiones

    def actualizacion_pos(self,ventana):
        ventana.blit(self.imagen,[self.pos_x,self.pos_y])# proyección de la imagen
        self.pos_y += self.velocidad # actualizacion de la posición
    
    def __del__(self): # destructor
        print('Objeto eliminado')