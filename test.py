import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

def demarrer_jeu():
    global en_jeu, score, obstacles, personnage
    en_jeu = False
    score = 0
    personnage.x = 50
    personnage.y = hauteur_fenetre // 2 - 15
    obstacles = [pygame.Rect(random.randint(100, 700), random.randint(0, hauteur_fenetre - 30), 30, 30) for _ in range(5)]

# Paramètres du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
vitesse_personnage = 15
vitesse_obstacle = 25

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu d'aventure")

# Initialisation du personnage et des obstacles
personnage = pygame.Rect(50, hauteur_fenetre // 2 - 15, 30, 30)
obstacles = [pygame.Rect(random.randint(100, 700), random.randint(0, hauteur_fenetre - 30), 30, 30) for _ in range(5)]

# Score
score = 0
vitesse_score = 1

# Police pour le score
police = pygame.font.Font(None, 36)

# État du jeu
en_jeu = False


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if en_jeu:
        # Déplacement du personnage
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP] and personnage.top > 0:
            personnage.y -= vitesse_personnage
        if touches[pygame.K_DOWN] and personnage.bottom < hauteur_fenetre:
            personnage.y += vitesse_personnage
        if touches[pygame.K_LEFT] and personnage.left > 0:
            personnage.x -= vitesse_personnage
        if touches[pygame.K_RIGHT] and personnage.right < largeur_fenetre:
            personnage.x += vitesse_personnage

        # Déplacement des obstacles
        for obstacle in obstacles:
            obstacle.x -= vitesse_obstacle
            if obstacle.right < 0:
                obstacle.x = largeur_fenetre
                obstacle.y = random.randint(0, hauteur_fenetre - 30)

            # Vérification de la collision avec le personnage
            if personnage.colliderect(obstacle):
                print("Collision !")
                demarrer_jeu()

        # Augmenter le score en fonction de la distance parcourue
        score += vitesse_obstacle

        # Dessin du jeu
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, blanc, personnage)
        for obstacle in obstacles:
            pygame.draw.rect(fenetre, rouge, obstacle)

        # Affichage du score
        texte_score = police.render(f"Score: {score}", True, blanc)
        fenetre.blit(texte_score, (10, 10))

        # Rafraîchir l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images pour éviter une exécution trop rapide
        pygame.time.Clock().tick(30)

    if not en_jeu:
    
    #Affichage de l'écran de démarrage 
        def afficher_ecran_demarrage():
            fenetre.fill(noir)
            texte_demarrage = police.render("Appuyez sur ESPACE pour démarrer", True, blanc)
            texte_demarrage_rect = texte_demarrage.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
            fenetre.blit(texte_demarrage, texte_demarrage_rect)
        afficher_ecran_demarrage()

    #touche démarrage
        touches = pygame.key.get_pressed()
        if touches[pygame.K_SPACE]:
            en_jeu = True

    

        # Rafraîchir l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images pour éviter une exécution trop rapide
        pygame.time.Clock().tick(30)

