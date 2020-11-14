'''
PHISIKS OP!
'''

# Imports
import pymunk, pygame, random
from classes import *
from settings import *

########## PyMunk Initialization ##########
space = pymunk.Space()          # Create a Space which contain the simulation
space.gravity = 1, GRAVITY            # Set its gravity

########## PyGame Initialization ##########
pygame.init()
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Phisiks!')
clock = pygame.time.Clock()

# Player
px, py = WW//2, WH//2
player = DynamicBall(px, py, -100, 100, 10, space)

# boxy = StaticBox(100, WH-100, WW, 25, 0, space)
lines = []
start_pos = [
    (0, WH), (0, 0), (0, 0), (WW, 0), (0, 400)
]
end_pos = [
    (WW, WH), (WW, 0), (0, WH), (WW, WH), (400, 400)
]
for s, e in zip(start_pos, end_pos):            # can't use nested cuz it makes wierd things happen xD
    l = StaticLine(s, e, 10, space)
    lines.append(l)

running = True
# Main Loop
while running:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    player.draw(screen, (255, 255, 0))

    for line in lines:
        line.draw(screen, (0, 255, 255))

    # Updating
    space.step(2/FPS)          # idk why is the value is 1/FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
