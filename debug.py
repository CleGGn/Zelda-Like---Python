import pygame
pygame.init()
font = pygame.font.Font(None,30)

# Fonction qui permet de créer une surface rectangulaire noire avec du texte blanc
# Utilisée pour tester l'affichage
def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface() # Initialisation de la surface
    debug_surf = font.render(str(info), True,'White') # Définition du rendu du texte
    debug_rect = debug_surf.get_rect(topleft = (x,y))  # Définition de la position de la surface
    pygame.draw.rect(display_surface, 'Black', debug_rect) # Création de la surface en fonction des paramètres précédents
    display_surface.blit(debug_surf,debug_rect) # Affichage de la surface