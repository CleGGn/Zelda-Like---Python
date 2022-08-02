import pygame
from settings import TILESIZE, WORLD_MAP
from modele.Tile import Tile
from modele.Player import Player
from modele.YSortCameraGroup import YSortCameraGroup
from debug import debug
from modele.Support import import_csv_layout

class Level:
    def __init__(self):
        # Récuperation de la surface d'affichage(méthode qui peut être utilisée partout)
        self.display_surface = pygame.display.get_surface()
        # On initialise les différents groupes de sprite
        # Les sprites visibles à l'écran
        self.visible_sprites = YSortCameraGroup()
        # Les sprites non visible utilisés pour les collisions
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    # Fonction qui crée notre WORLD_MAP 
    def create_map(self):
        # On crée un dictionnaire dans lequel chaque fichier CSV sera importé sous une variable
        layouts = {
                'boundary': import_csv_layout('map/map_FloorBlocks.csv') # Les obstacles
        }
        # On parcours notre fichier CSV pour déterminer quel élément se trouve à chaque index
        # style correspond au fichier CSV
        # layout correspond au contenu
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    # -1 = rien du tout
                    # 395 = obstacle
                    # Si le contenu de l'index de notre boucle n'est pas égal à -1 on crée des coordonnées et crée une case obstacle
                    if col != '-1':    
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE                      
                        if style == 'boundary':    
                            Tile((x,y),[self.obstacle_sprites],'invisible')              
        #         if col == 'x': 
        #             # Si c'est un x, on lui attribut la classe Tile, censée représenter une case du jeu
        #             # On positionne cette Tile dans les sprites visibles et invisible pour pouvoir gérer les collisions
        #             Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
        #         if col == 'p':
        #             # Si c'est un p, on lui attribut la classe Player, censée représenter le joueur
        self.player = Player((2000,1430),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Affiche le niveau (On utilise une méthode d'affichage inhérente à notre Classe YSortCameraGroup)
        self.visible_sprites.custom_draw(self.player)
        # Mets à jour le niveau (Méthode inhérente à la classe Group())
        self.visible_sprites.update()
