import pygame, sys
from settings import *

class Game:
    def _init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

# Fonction qui lance la partie
    def run(self):
        # Tant que le jeu est lancé ..
        while True:
            for event in pygame.event.get():
                # Si le joueur appuies sur la croix en haut à droite
                if event.type == pygame.QUIT:
                    # On coupe tout
                    pygame.quit()
                    sys.exit() 

            # On initialise différents paramètres
            # - On rempli l'écran en noir
            self.screen.fill('black') 

            # - On met continuellement à jour l'écran 
            # (ou plutôt certaines parties de l'écran qui seront modifiées en fonctions des actions)
            pygame.display.update()

            # - On initialise une horloge
            self.clock.tick(FPS)

