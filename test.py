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

#Initialisation du personnage et des obstacles 
personnage = pygame.Rect(50, hauteur_fenetre // 2 - 15, 30, 30)
obstacles = [pygame.Rect(random.randint(100, 700), random.randint(0, hateur_fenetre - 30), 30, 30) for _ in range(5)]

#Score
score = 0

#Tableau des scores
tableau_scores = []

#Police pour le score
police = pygame.font.Font(None, 36)

#Boucle principale du jeu 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Deplacement du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_UP] and personnage.top > 0:
        personnage.y -= vitesse_personnage
    if touches[pygame.K_DOWN] and personnage.bottom < hauteur_fenetre:
        personnage.y += vitesse_personnage
    if touches[pygame.K_LEFT] and personnage.left > 0:
        personnage.x -= vitesse_personnage
    if touches[pygame.K_RIGHT] and personnage.right < largeur_fenetre:
        personnage.x += vitesse_personnage

    #Deplacement des obstacles
    for obstacle in obstacles:
        obstacle.x -= vitesse_obstacle
        if obstacle.right < 0:
            obstacle.x = largeur_fenetre
            obstacle.y = random.randint(0, hauteur_fenetre -30)

        #Verification de la collision le personnage
        if personnage.colliderect(obstacle):
            print("Collision !")
            pygame.quit()
            sys.exit()

    #Augmenter le score en fonction de la distance parcourue 
            score += vitesse_obstacle

    #Dessin du jeu 
    fenetre.fill(noir)
    pygame.draw.rect(fenetre, blanc, personnage)
    for obstacle a

