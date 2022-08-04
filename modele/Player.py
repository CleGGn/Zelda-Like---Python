import pygame
from settings import *
from pygame.math import Vector2
from modele.Support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('assets/test/player.png').convert_alpha() # Le visuel
        self.rect = self.image.get_rect(topleft = pos) # la position
        self.hitbox = self.rect.inflate(0, -26) # la hitbox de notre player

        # Graphismes
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Mouvements 
        self.direction = pygame.math.Vector2() # la direction
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites

    # Fonction qui va extraire chaque image et l'attribuer à son dossier correspondant
    def import_player_assets(self):
        character_path = "assets/player/" # On prépare notre string de chemin
        self.animations ={'up': [],'down': [],'left': [],'right': [], 
        'up_idle': [],'down_idle': [],'left_idle': [],'right_idle': [],
        'up_attack': [],'down_attack': [],'left_attack': [],'right_attack': [],} # Notre dictionnaire de mouvements

        for animation in self.animations.keys(): # Pour chaque animation dans dictionnaire, on va importer le contenu correspondant et le rétribuer sous forme de liste
            full_name = character_path + animation # Nom complet du sous dossier
            self.animations[animation] = import_folder(full_name) #On appelle notre fonction qui nous créée une liste pour chaque mouvement
        
    # Fonction qui check les inputs du joueur
    def input(self):
        if not self.attacking: # On bloque les mouvements si le joueur est en train d'attaquer
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction.y = -1 # Notre map est un array donc aller vers le haut équivaut à reduire x de 1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1     
                self.status = 'down'
            else:
                self.direction.y = 0 # Il faut remettre la direction à 0 si rien n'est pressé, sinon le joueur continuera d'aller dans cette direction
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE]: # On vérifie lors de l'input que le joueur ne soit pas déja entrain d'attaquer 
                self.attacking = True # S'il ne l'est pas, il le devient
                self.attack_time = pygame.time.get_ticks() # On produit donc un tick (une seule fois) qui correspond à une valeur en millisecondes 

            if keys[pygame.K_LCTRL]: # On vérifie lors de l'input que le joueur ne soit pas déja entrain de faire de la magie 
                self.attacking = True # S'il ne l'est pas, il le devient
                self.attack_time = pygame.time.get_ticks() # On produit donc un tick (une seule fois) qui correspond à une valeur en millisecondes 

    # Fonction qui change la string de self.status en fonction des actions et des mouvements
    def get_status(self):
        # Statut immobile
        if self.direction.x ==0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status +'_idle'
                
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:    
                    self.status = self.status +'_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','_idle')

    # Fonction qui déplace le personnage en fonction de sa vitesse
    def move(self,speed):
        if self.direction.magnitude() != 0: # magnitude correspond à la taille du vecteur. On vérifie donc qu'il soit supérieur à 0
            # Si le vecteur est supérieur à 0, on le "normalize". Grosso modo on enlève la virgule pour lui donner une valeur fixe  
            # On utilise cette méthode pour les déplacements en diagonale qui sont toujours légèrement supérieur à déplacement en ligne
            self.direction = self.direction.normalize() 
        # Une fois la normalisation faite, on donne la nouvelle position du personnage    
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    # Fonction qui gère les collisions (non pas avec la surface des sprites mais avec les hitboxes)
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): # "colliderect()"" verifie s'il y a collision entre "sprite" et "hitbox"
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left # s'il y a collision entre les hitboxs alors on place la droite de la hitbox du personnage sur la gauche de la hitbox du sprite
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    # Fonction qui gère les temps entre les actions
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown: # Si la valeur du tick current_time - celle produite par une action est supérieur ou égale à notre variable attack_cooldown alors on considère que l'action a encore lieu (Cooldown en cours)
                self.attacking = False

    # Fonction qui anime les actions en fonctions du statut
    def animate(self):
        animation = self.animations[self.status] # Variable qui correspond au dossier de l'animation en cours

        self.frame_index += self.animation_speed # On veut afficher à la suite les images du dossier à la vitesse déclarée plus tot
        if self.frame_index >= len(animation):
            self.frame_index = 0      # Si on arrive à la dernière image, on retourne à la première
        self.image = animation[int(self.frame_index)] # On gènère une nouvelle image en fonction de l'index de la frame (qu'on transforme en int)
        self.rect = self.image.get_rect(center = self.hitbox.center) # On la met sur notre surface et on replace le centre de la hitbox

    # Fonction appelé continuellement pour mettre à jours les différents éléments
    def update(self):
        self.input()
        self.cooldowns() 
        self.get_status()
        self.animate()
        self.move(self.speed)
    