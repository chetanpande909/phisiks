import pymunk, pygame
from classes import *

################# Pymunk initialization #################
space = pymunk.Space()      # Create a Space which contain the simulation
space.gravity = 0,10     # Set its gravity

################# Pygame initialization #################
pygame.init()
WW, WH = 500, 500
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Pymunk!')
FPS = 50
clock = pygame.time.Clock()

bouncy = Ball(WW//2, WH//2, 10, 10, 10, space)

running = True
while running:                 # Infinite loop simulation
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    ## Drawing starts now ;)
    bouncy.draw(screen, (0, 0, 0))

    space.step(1/FPS)        # Step the simulation one step forward

    pygame.display.update()
    clock.tick()

pygame.quit()