# Imports
import pygame, pymunk

################# Pymunk initialization #################
GRAVITY = 250

################# Pygame initialization #################
WW, WH = 1000, 600      ## Do not change now cuz the level coords are hard coded
FPS = 120
BGCOLOR = (255, 255, 255)
pygame.init()
tiny_font = pygame.font.Font('Roboto-Thin.ttf', 24)
small_font = pygame.font.Font('Roboto-Thin.ttf', 32)
medium_font = pygame.font.Font('Roboto-Thin.ttf', 48)
big_font = pygame.font.Font('Roboto-Thin.ttf', 64)

#################   General Settings    #################
# Colors
WHITE = (255, 255, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
L_BLUE = (0, 255, 255)
PINK = (255, 0, 255)

skins = [
    pygame.image.load('imgs/ball.jpg'),
    pygame.image.load('imgs/EggBlue.jpg'),
    pygame.image.load('imgs/EggGreen.jpg'),
    pygame.image.load('imgs/EggPurp.jpg'),
    pygame.image.load('imgs/EggRed.jpg'),
    pygame.image.load('imgs/EggYellow.jpg'),
    pygame.image.load('imgs/EnBallBlue.jpg'),
    pygame.image.load('imgs/EnBallGreen.jpg'),
    pygame.image.load('imgs/EnBallPurp.jpg'),
    pygame.image.load('imgs/EnBallRed.jpg'),
    pygame.image.load('imgs/EnBallYellow.jpg')
]
