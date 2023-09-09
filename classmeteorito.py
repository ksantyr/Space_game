import pygame
import random

class Meteorito(pygame.sprite.Sprite):

    def __init__(self,tamano): # atributos del objeto
        super().__init__() #Verifica que se inicialice todo correctamente y permite heredar de la clase    
    
        self.image = pygame.image.load('Imagenes/meteorito.png') #imagen del meteorito
        self.image = pygame.transform.scale(self.image,(60,60)) # redimensionamos la imagen
        """
        self.pos_x = random.randint(100,700) # posición en x en la ventana
        self.pos_y = 0 # posición en y en la ventana
        """
        
        self.velocidad = 1.5 # velocidad
        self.rect = self.image.get_rect() #se rellena la imagen como un rectangulo con el fin de gestionar las colisiones
        self.rect.x = random.randint(0,tamano[1])  #posicion x en la ventana
        self.rect.y =0  # Posicion y en la ventana
       
    def update(self):
        #ventana.blit(self.image,[self.pos_x,self.pos_y])# proyección de la imagen
        #pygame.display.flip() # actualización de la ventana 
        self.rect.y += self.velocidad # actualizacion de la posición
         
    
    def __del__(self): # destructor
        print('meteorito eliminado')