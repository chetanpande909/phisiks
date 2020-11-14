# Imports
import pygame, pymunk

################# Pymunk initialization #################
GRAVITY = 250

################# Pygame initialization #################
WW, WH = 1000, 600      ## Do not change now cuz the level coords are hard coded
FPS = 60
pygame.init()
small_font = pygame.font.Font('Roboto-Thin.ttf', 32)
big_font = pygame.font.Font('Roboto-Thin.ttf', 64)

#################   General Settings    #################
