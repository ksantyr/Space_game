# -*- coding: utf-8 -*-
import pygame

def start(ventana, fuente):
    
    # muestra la imagen de inicio
    imagen = pygame.image.load("Imagenes/cover.jpg")
    ventana.blit(imagen, (0,0))
    
    mensaje = fuente.render("Presione enter para jugar", True, (255,255,255))
    ventana.blit(mensaje, (550, 700))

    
def gameOver(ventana,fuente):
    # Muestra el Fin de juego
    imagen = pygame.image.load("Imagenes/game over.jpg")
    ventana.blit(imagen, (0, 0))
    
    mensaje = fuente.render("Presione enter para volver a jugar", True, (255, 255, 255))
    ventana.blit(mensaje, (500, 700))


