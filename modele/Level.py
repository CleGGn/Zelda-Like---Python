import pygame
from settings import TILESIZE, WORLD_MAP
from modele.Tile import Tile
from modele.Player import Player
from debug import debug

class Level:
    def __init__(self):
        # Récuperation de la surface d'affichage(méthode qui peut être utilisée partout)
        self.display_surface = pygame.display.get_surface()
        # On initialise les différents groupes de sprite
        # Les sprites visibles à l'écran
        self.visible_sprites = pygame.sprite.Group()
        # Les sprites non visible utilisés pour les collisions
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    # Fonction qui crée notre WORLD_MAP
    def create_map(self):
        # On parcours notre WORLD_MAP pour déterminer quel élément se trouve à chaque index
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                # TILESIZE = 64
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x': 
                    # Si c'est un x, on lui attribut la classe Tile, censée représenter une case du jeu
                    # On positionne cette Tile dans les sprites visibles et invisible pour pouvoir gérer les collisions
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    # Si c'est un p, on lui attribut la classe Player, censée représenter le joueur
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Affiche le niveau (Méthode inhérente à la classe Group())
        self.visible_sprites.draw(self.display_surface)
        # Mets à jour le niveau (Méthode inhérente à la classe Group())
        self.visible_sprites.update()
        debug(self.player.direction)