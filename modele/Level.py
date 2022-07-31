import pygame

class Level:
    def __init__(self):
        # Récuperation de la surface d'affichage(méthode qui peut être utilisée partout)
        self.display_surface = pygame.display.get_surface()

        # On initialise les différents groupes de sprite
        # Les sprites visibles à l'écran
        self.visible_sprites = pygame.sprite.Group()
        # Les sprites non visible utilisés pour les collisions
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        #Mets à jour et affiche le niveau
        pass