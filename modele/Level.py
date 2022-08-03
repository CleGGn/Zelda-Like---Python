from random import random
import pygame
from settings import TILESIZE
from modele.Tile import Tile
from modele.Player import Player
from modele.YSortCameraGroup import YSortCameraGroup
from debug import debug
from modele.Support import import_csv_layout, import_folder
from random import choice

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

    # Fonction qui créer notre map à partir des fichiers CSV
    def create_map(self):
        # On crée un dictionnaire dans lequel chaque fichier CSV sera importé sous une variable
        layouts = {
                'boundary': import_csv_layout('map/map_FloorBlocks.csv'), # Les obstacles
                'grass': import_csv_layout('map/map_Grass.csv'), # L'herbe'
                'object': import_csv_layout('map/map_LargeObjects.csv'), # Les objets
        }

        # On crée un dictionnaire dans lequel chaque variable correspond à un dossier d'image
        graphics = {
            'grass': import_folder('assets\grass'),
            'objects':import_folder('assets\objects')
        }
        
        # On parcours notre fichier CSV pour déterminer quel élément se trouve à chaque index
        # style correspond au fichier CSV
        # layout correspond au contenu
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    # -1 = rien du tout
                    # 395 = obstacle
                    # Si le contenu de l'index de notre boucle n'est pas égal à -1 on crée des coordonnées et crée un sprite en fonction du contenu
                    if col != '-1':    
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE                      
                        if style == 'boundary':    # Si obstacle
                            Tile((x,y),[self.obstacle_sprites],'invisible') # on crée une instance de la class Tile, on la positionne dans les sprites invisibles et on le label
                        if style == 'grass':  # si grass
                            random_grass_image = choice(graphics['grass']) # on selectionne le dossier des sprites et on randomize l'affichage avec la méthode choice()
                            Tile((x,y),[self.visible_sprites],'grass', random_grass_image)
                        if style == 'object': # si objet (chaque objet étant unique, le nom du fichier correspond à l'id dans le CSV)
                            surf_object = graphics['objects'][int(col)] #col = un objet
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'object', surf_object) # on crée une instance de la class Tile, on la positionne dans les sprites invisibles et visible (obstacle visible) et on le label
                        
        self.player = Player((2000,1430),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Affiche le niveau (On utilise une méthode d'affichage inhérente à notre Classe YSortCameraGroup)
        self.visible_sprites.custom_draw(self.player)
        # Mets à jour le niveau (Méthode inhérente à la classe Group())
        self.visible_sprites.update()
