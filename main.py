'''
PHISIKS OP!
'''

# Imports
import pymunk, pygame, random, math
from classes import *
from levels import *
from settings import *

########## PyMunk Initialization ##########
space = pymunk.Space()                # Create a Space which contain the simulation
space.gravity = 0, GRAVITY            # Set its gravity

########## PyGame Initialization ##########
pygame.init()
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Phisiks!')
clock = pygame.time.Clock()

# Handling Levels
current_level = level1

# Player
max_speed = 100
player = DynamicBall(current_level[3], 0, 0, 10, space)

# boxy = StaticBox(100, WH-100, WW, 25, 0, space)
lines = []
for s, e in zip(current_level[0], current_level[1]):            # can't use nested cuz it makes wierd things happen xD
    l = StaticLine(s, e, 10, space)
    lines.append(l)

# Moves in which the player has to complete the level
moves = 5

# Victory Flag
flag = VictoryFlag(current_level[2])

# Some functions
def change_level(level):
    global current_level, lines, flag, player, moves
    current_level = level
    for rl in lines:
        space.remove(rl.body, rl.shape)            # Extremely Necessary 
    lines = []                      # Deleting the lines of the prev level
    for s, e in zip(current_level[0], current_level[1]):        # Copy paste from above ;)
        l = StaticLine(s, e, 10, space)
        lines.append(l)
    
    flag = VictoryFlag(current_level[2])
    player = DynamicBall(current_level[3], 0, 0, 10, space)
    moves = 5

running = True
clicked = False
# Main Loop
while running:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    
    # Drawing the direction in which a force will b applied
    # it's just for a reference, but it looks cool so ;)
    mx, my = pygame.mouse.get_pos()
    distx = mx - player.body.position.x
    disty = my - player.body.position.y
    pygame.draw.aaline(screen, (255, 100, 10), player.body.position, (mx, my), 10)

    player.draw(screen, (255, 100, 10))     # Drawing the player
    flag.draw(screen)                       # Drawing the victory flag
    
    # Drawing the walls/lines whatever u call it -_-
    for line in lines:
        line.draw(screen, (0, 255, 255))

    # Adding a velocity to the ball if it clicked
    if clicked:
        if moves > 0:
            moves -= 1
            player.body.velocity = (distx, disty)
        clicked = False

    # Limiting the player's velocity (so that it doesn't flies across like hell xD)
    if distx > max_speed:
        distx = max_speed
    if disty > max_speed:
        disty = max_speed

    # Displaying the number of moves left
    moves_text = small_font.render('Moves Left: '+ str(moves), True, (255, 0, 255))
    moves_rect = moves_text.get_rect()
    moves_rect.center = (WW//2, 50)
    screen.blit(moves_text, moves_rect.topleft)

    # Checking collision b/w player and the victory flag
    if player.rect.colliderect(flag.rect):
        print('You win!')
        change_level(level2)

    # Updating
    space.step(1/FPS)          # idk why is the value is 2/FPS
    pygame.display.update()
    clock.tick(FPS*2)

pygame.quit()
