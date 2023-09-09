import pygame
import random

class Moneda(pygame.sprite.Sprite):

    def __init__(self,tamano): # atributos del objeto
        super().__init__() #Verifica que se inicialice todo correctamente y permite heredar de la clase
        self.image = pygame.image.load('Imagenes/moneda.png') # imagen de la moneda
        self.image = pygame.transform.scale(self.image,(50,50)) # redimensionamos la imagen
        self.velocidad = 10 # velocidad
        self.rect = self.image.get_rect() #se rellena la imagen como un rectangulo con el fin de gestionar las colisiones
        self.rect.x = random.randint(0,tamano[1])  #posicion x en la ventana
        self.rect.y =0  # Posicion y en la ventana

    def update(self):
        self.rect.y += self.velocidad # actualizacion de la posición
    
    def __del__(self): # destructor
        print('moneda eliminado')