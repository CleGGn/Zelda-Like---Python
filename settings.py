#Les paramètres de base du jeu
WIDTH = 1280 # Largeur
HEIGHT = 720 # Hauteur
FPS = 60 # Images par seconde (Utilisées pour la mise à jour de l'affichage)
TILESIZE = 64 # Proportion d'une "case" ( en pixel )

# Les Armes
weapon_data = {
    'sword':{'cooldown':100, 'damage':15, 'graphics':'assets/weapons/sword/full.png'},
    'lance':{'cooldown':400, 'damage':30, 'graphics':'assets/weapons/lance/full.png'},
    'axe':{'cooldown':300, 'damage':20, 'graphics':'assets/weapons/axe/full.png'},
    'rapier':{'cooldown':50, 'damage':8, 'graphics':'assets/weapons/rapier/full.png'},
    'sai':{'cooldown':80, 'damage':10, 'graphics':'assets/weapons/sai/full.png'}
}