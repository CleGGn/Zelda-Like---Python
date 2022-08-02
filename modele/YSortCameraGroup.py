import pygame
from pygame.math import Vector2

# Cette classe permet d'afficher les sprites en fonctionde la position du joueur (Le joueur est toujours placé au centre de la caméra)
# On hérite de la classe "pygame.sprite.Group" en réecrivant certains paramètres
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface() # Notre surface d'affichage
        self.half_width = self.display_surface.get_size()[0] // 2 # La largeur de la surface d'affichage divisée par deux (// revient à faire une division entière (on récupère un int))
        self.half_heigth = self.display_surface.get_size()[1] // 2 # La largeur de la surface d'affichage divisée par deux

        self.offset = pygame.math.Vector2() # On initialise un vecteur pour le décalage de l'écran

        # On créer le terrain
        self.floor_surf = pygame.image.load('assets/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        # On donne à notre vecteur des coordoonées équivalentes au centre du sprite du joueur moins la moitié et la hauteur de l'écran
        self.offset.x = player.rect.centerx - self.half_width 
        self.offset.y = player.rect.centery - self.half_heigth

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset # On positionne chaque sprites en fonction de notre offset (Notre personnage au centre de l'écran)
            self.display_surface.blit(sprite.image, offset_pos) # On dessine ces sprites