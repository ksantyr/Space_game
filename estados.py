# -*- coding: utf-8 -*-
import pygame

#pygame.init() # inicializamos la libreria de pygame
#fuente = pygame.font.Font('fonts/ARCO.ttf', 50)
#fuente = pygame.font.Font(None,36)

def start(ventana, fuente):
    
    # Muestra el titulo
    #ventana.fill ((0,0,0))
    
    titulo = fuente.render("Space Game", True, (255, 255, 255))
    ventana.blit(titulo, (1024//2, 800//2))
    
    mensaje = fuente.render("Presione enter para jugar", True, (255, 255, 255))
    ventana.blit(mensaje, (1024//2, 900//2))
    


def gameOver(ventana,fuente):
    # Muestra el Fin de juego
    mensaje = fuente.render("Game Over", True, (255, 255, 255))
    ventana.blit(mensaje, (1024//2, 800//2))
    
    mensaje = fuente.render("Presione enter para volver a jugar", True, (255, 255, 255))
    ventana.blit(mensaje, (1024//2, 900//2))


