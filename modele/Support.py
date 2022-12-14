from csv import reader
from os import walk
import pygame

# Fonction qui permet de lire un fichier CSV et d'en extraire les données
def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',') # On délimite chacune des données avec une virgule
        # Chacun des rangs de données de "layout" sera ajouté sous forme de liste à terrain_map
        # Chaque rang devient donc une liste 
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map # On retourne un tableau de liste

# Fonction qui permet de lire un dossier et placer le contenu dans un tableau
def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
