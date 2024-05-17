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
     # Définir la zone sûre autour du personnage (par exemple, un rectangle de 200x200 autour du personnage)
    zone_sure = pygame.Rect(100, 100, largeur_fenetre - 200, hauteur_fenetre - 200)

    # Générer les obstacles en évitant la zone sûre
    obstacles = []
    for _ in range(5):
        x = random.randint(100, 700)
        y = random.randint(0, hauteur_fenetre - 30)
        obstacle_rect = pygame.Rect(x, y, 100, 100)
        
        # Vérifier si l'obstacle est dans la zone sûre, ajuster si nécessaire
        while obstacle_rect.colliderect(zone_sure):
            x = random.randint(100, 700)
            y = random.randint(0, hauteur_fenetre - 30)
            obstacle_rect = pygame.Rect(x, y, 100, 100)

        obstacles.append((obstacle_rect, obstacle_image))
delai_obstacle = 5

# Paramètres du jeu
largeur_fenetre = 1200
hauteur_fenetre = 800
vitesse_personnage = 15
vitesse_obstacle = 25

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu d'aventure")



# Chargement de l'image du personnage
personnage_image = pygame.image.load ("d:/pygame/sprites/plane.png")
personnage_image = pygame.transform.scale(personnage_image, (100, 100))  # Redimensionner si nécessaire
personnage_rect = personnage_image.get_rect()
personnage_rect.topleft = (50, hauteur_fenetre // 2 - 15)

# Chargez les images des sprites d'obstacles
obstacle_image = pygame.image.load("d:/pygame/sprites/sprite_fire.png")
# Redimensionnez les sprites si nécessaire
obstacle_image = pygame.transform.scale(obstacle_image, (100, 100))  # Ajustez la taille selon vos besoins

# Initialisation du personnage et des obstacles
personnage = pygame.Rect(50, hauteur_fenetre // 2 - 15, 30, 30)
obstacles = [(pygame.Rect(random.randint(100, 700), random.randint(0, hauteur_fenetre - 30), 100, 100),obstacle_image) for _ in range(5)]

# Score
score = 0
vitesse_score = 1

# Police pour le score
police = pygame.font.Font(None, 36)

# État du jeu
en_jeu = False

sprite_animation = pygame.image.load("d:/pygame/sprites/sprite_background2.jpg")
# Redimensionner l'image du sprite
nouvelle_taille = (sprite_animation.get_width() * 2, sprite_animation.get_height() * 2)
sprite_animation = pygame.transform.scale(sprite_animation, nouvelle_taille)
sprite_animation_rect = sprite_animation.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if en_jeu:

       
        # Déplacement du personnage
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP] and personnage_rect.top > 0:
            personnage_rect.y -= vitesse_personnage
        if touches[pygame.K_DOWN] and personnage_rect.bottom < hauteur_fenetre:
            personnage_rect.y += vitesse_personnage
        if touches[pygame.K_LEFT] and personnage_rect.left > 0:
            personnage_rect.x -= vitesse_personnage
        if touches[pygame.K_RIGHT] and personnage_rect.right < largeur_fenetre:
            personnage_rect.x += vitesse_personnage

        # Gestion du délai avant le démarrage des obstacles
        if delai_obstacle > 0:
           delai_obstacle -= 1
        else:

        # Déplacement des obstacles
             for obstacle, _ in obstacles:
                 obstacle.x -= vitesse_obstacle
                 if obstacle.right < 0:
                    obstacle.x = largeur_fenetre
                    obstacle.y = random.randint(0, hauteur_fenetre - 30)

            # Vérification de la collision avec le personnage
                 if personnage_rect.colliderect(obstacle):
                     print("Collision !")
                     demarrer_jeu()

        # Augmenter le score en fonction de la distance parcourue
        score += vitesse_obstacle

        

        # Dessin du jeu
        fenetre.fill(noir)
        # Afficher le sprite de fond
        fenetre.blit(sprite_animation, sprite_animation_rect)
        # Afficher le personnage
        fenetre.blit(personnage_image, personnage_rect)

        for obstacle in obstacles:
           fenetre.blit(obstacle[1], obstacle[0])

 

        # Affichage du score
        texte_score = police.render(f"Score: {score}", True, blanc)
        fenetre.blit(texte_score, (10, 10))

        

        # Rafraîchir l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images pour éviter une exécution trop rapide
        pygame.time.Clock().tick(30)

    if not en_jeu:
    
    # Charger l'image du sprite pour le titre
        sprite_titre = pygame.image.load("d:/pygame/sprites/title_demarrage.png")
        sprite_titre_rect = sprite_titre.get_rect(center=(largeur_fenetre // 2.7, hauteur_fenetre // 4))
        nouvelle_taille = (sprite_titre.get_width() * 1.5, sprite_titre.get_height() * 1.5)
        sprite_titre = pygame.transform.scale(sprite_titre, nouvelle_taille) 

   # Chargement de l'image du sprite pour l'écran de démarrage
        sprite_demarrage = pygame.image.load("d:/pygame/sprites/sprite_demarrage.jpg")
        sprite_demarrage_rect = sprite_demarrage.get_rect(center=(largeur_fenetre // 4, hauteur_fenetre // 4))
        nouvelle_taille = (sprite_demarrage.get_width() * 2, sprite_demarrage.get_height() * 2)
        sprite_demarrage = pygame.transform.scale(sprite_demarrage, nouvelle_taille)

   # Charger une nouvelle police avec une taille plus grande
        police_ecran_demarrage = pygame.font.Font(None, 58)  # 48 est la nouvelle taille de police

  

    #Affichage de l'écran de démarrage 
        def afficher_ecran_demarrage():
            fenetre.fill(noir)
            fenetre.blit(sprite_demarrage, sprite_demarrage_rect)
            fenetre.blit(sprite_titre, sprite_titre_rect)
            texte_demarrage = police_ecran_demarrage.render("START", True, blanc)
            texte_demarrage_rect = texte_demarrage.get_rect(center=(largeur_fenetre // 2 , hauteur_fenetre // 2 + 140))
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
