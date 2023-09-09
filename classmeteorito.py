import pygame
import random

class Meteorito(pygame.sprite.Sprite):

    def __init__(self,tamano): # atributos del objeto
        super().__init__() #Verifica que se inicialice todo correctamente y permite heredar de la clase    
        self.image = pygame.image.load('Imagenes/meteorito.png') #imagen del meteorito     
        self.velocidad = 15 # velocidad
        self.rect = self.image.get_rect() #se rellena la imagen como un rectangulo con el fin de gestionar las colisiones
        self.rect.x = random.randint(0,tamano[1])  #posicion x en la ventana
        self.rect.y =0  # Posicion y en la ventana
       
    def update(self):
        self.rect.y += self.velocidad # actualizacion de la posición
         
    def __del__(self): # destructor
        print('meteorito eliminado')