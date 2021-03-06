'''
PHISIKS OP!
'''

# Imports
import pymunk, pygame, random, math, time
from classes import *
from levels import *
from settings import *
from extra_screens import *

########## PyMunk Initialization ##########
space = pymunk.Space()  # Create a Space which contain the simulation
space.gravity = 0, GRAVITY  # Set its gravity

########## PyGame Initialization ##########
pygame.init()
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Phisiks!')
clock = pygame.time.Clock()

# Handling Levels
current_level = level1

# Player and showing Welcom screen
welcome_screen_data = welcome_screen(screen)
running = welcome_screen_data[0]
p_img = welcome_screen_data[1]
max_speed = 100
player = DynamicBall(current_level[3], 0, 0, p_img, space)

# boxy = StaticBox(100, WH-100, WW, 25, 0, space)
lines = []
for s, e in zip(current_level[0], current_level[1]):  # can't use nested cuz it makes wierd things happen xD
    l = StaticLine(s, e, 10, space)
    lines.append(l)

# Moves in which the player has to complete the level
moves = 5

# Victory Flag
flag = VictoryFlag(current_level[2])


# Some functions
def next_level(curr_level):
    global current_level, lines, flag, player, moves

    try:
        current_level = levels[levels.index(curr_level) + 1]  ## increasing the level by 1
    except IndexError:  ## if list is out of levels
        current_level = levels[0]  ## this can b changed in the future to make a victory page that u have completed all levels !

    flag = VictoryFlag(current_level[2])

    space.remove(player.body, player.shape)         ## i didn't removed the player from the space so collisions were happening xD
    
    player = DynamicBall(current_level[3], 0, 0, p_img, space)

    for rl in lines:
        space.remove(rl.body, rl.shape)  # Extremely Necessary
    lines = []  # Deleting the lines of the prev level

    for s, e in zip(current_level[0], current_level[1]):  # Copy paste from above ;)
        l = StaticLine(s, e, 10, space)
        lines.append(l)

    moves = 5


def reset_level():
    global score, st_time
    next_level(levels[-1])
    score = 0
    st_time = 0


clicked = False

# noting Score
score = 0
st_time = 0  # Time

level_number_to_display = 1
while running:
    if st_time == 0:
        st_time = time.time()
        for l in levels:
            if current_level == l:
                level_number_to_display = levels.index(l) + 1
                break

    screen.fill(BGCOLOR)
    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if e.type == pygame.KEYDOWN:
            if moves == 0 and e.key == pygame.K_r:
                reset_level()

    # Drawing the direction in which a force will b applied
    # it's just for a reference, but it looks cool so ;)
    mx, my = pygame.mouse.get_pos()
    distx = mx - player.body.position.x
    disty = my - player.body.position.y
    pygame.draw.aaline(screen, GREEN, player.body.position, (mx, my), 10)

    player.draw(screen)  # Drawing the player
    flag.draw(screen)  # Drawing the victory flag

    # Drawing the walls/lines whatever u call it -_-
    for line in lines:
        line.draw(screen, L_BLUE)

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

    moves_text = small_font.render('Moves Left: ' + str(moves), True, PINK)
    moves_rect = moves_text.get_rect()
    moves_rect.center = (WW // 2, 50)
    screen.blit(moves_text, moves_rect.topleft)

    level_text = small_font.render(f"level: {level_number_to_display}", True, PINK)
    screen.blit(level_text, (20, 20))

    # Checking collision b/w player and the victory flag
    if player.rect.colliderect(flag.rect):
        # Adding to Score and reset score Variables
        score += 100 + int(float(100 * moves) / float(time.time() - st_time))
        st_time = 0

        # Show score
        # It will return False if Quit
        # it will return True if any key is pressed
        running = score_screen(screen, score)

        next_level(current_level)

    # Falling off the screen.... all games hav it so why not ;)
    if player.body.position.x < 0 or player.body.position.y > WW:
        reset_level()
    if player.body.position.y < 0 or player.body.position.y > WH:
        reset_level()

    # Updating
    space.step(1 / FPS)  # idk why is the value is 1/FPS
    pygame.display.update()
    clock.tick(FPS*2)

pygame.quit()
