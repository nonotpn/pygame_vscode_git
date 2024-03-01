import pygame
import sys
import random

# Iniatialisation de Pyame
pygame.init()

#Paramètre du jeu 
largeur_fenetre = 800
hauteur_fenetre = 600
vitesse_personnage = 40
vitesse_obstacle = 35

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

#Création de la fenêtre du jeu 
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu d'aventure")

