'''
PHISIKS OP!
'''

# Imports
import pymunk, pygame, random, math
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
vx, vy = 100, 100
player = DynamicBall(WW//2, WH//2, 0, 0, 10, space)

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

# Victory Flag
flag = VictoryFlag(50, 390)

running = True
# Main Loop
while running:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            player.body.velocity = (distx, disty)
    
    # Drawing the direction in which a force will b applied
    mx, my = pygame.mouse.get_pos()
    distx = mx - player.body.position.x
    disty = my - player.body.position.y
    pygame.draw.line(screen, (255, 100, 10), player.body.position, (mx, my), 5)

    player.draw(screen, (255, 100, 10))
    flag.draw(screen)
    
    for line in lines:
        line.draw(screen, (0, 255, 255))

    # Limiting the player's velocity (so that it doesn't flies across like hell xD)
    if distx > 150:
        distx = 150
    if disty > 150:
        disty = 150

    # Updating
    space.step(2/FPS)          # idk why is the value is 2/FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
