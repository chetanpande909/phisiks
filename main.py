'''
PHISIKS OP!
'''

# Imports
import pymunk, pygame, random
from classes import *
from settings import *

########## PyMunk Initialization ##########
space = pymunk.Space()          # Create a Space which contain the simulation
space.gravity = 0, GRAVITY            # Set its gravity

########## PyGame Initialization ##########
pygame.init()
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Phisiks!')
clock = pygame.time.Clock()

# Creating Objects
balls = []
for i in range(num_of_balls):
    x, y = random.randint(50, WW-50), random.randint(50, WH-50)
    b = DynamicBall(x, y, -100, 100, 10, space)
    balls.append(b)

# boxy = StaticBox(100, WH-100, WW, 25, 0, space)
liney1 = StaticLine((0, WH), (WW, WH), 10, space)     # Bottom
liney2 = StaticLine((0, 0), (WW, 0), 10, space)           # Top
liney3 = StaticLine((0, 0), (0, WH), 10, space)           # Left
liney4 = StaticLine((WW, 0), (WW, WH), 10, space)     # Right

running = True
# Main Loop
while running:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # Drawing starts now ;)
    for ball in balls:
        ball.draw(screen, (255, 255, 0))
    liney1.draw(screen, (0, 255, 255))
    liney2.draw(screen, (0, 255, 255))
    liney3.draw(screen, (0, 255, 255))
    liney4.draw(screen, (0, 255, 255))
    # boxy.draw(screen, (255, 255, 0))

    # Updating
    space.step(2/FPS)          # idk why is the value is 1/FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
