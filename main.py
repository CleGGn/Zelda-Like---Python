import pygame, sys
from settings import *
from modele.Game import Game

# Si le fichier main.py est appelé, on lance le jeu
if __name__ == "__main__":
    game = Game()
    game.run()