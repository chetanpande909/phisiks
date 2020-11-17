import pygame, time
from settings import *
import leaderboard as lb



def welcome_screen(screen):
    to_return = [True, skins[0]]
    while True:
        screen.fill((255, 255, 255))
        heading_text = big_font.render('Welcome to the Physics Game!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press a key to continue!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 250)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = tiny_font.render('Press I to see the instructions!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 440)
        # heading_rect[0]+=150
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = tiny_font.render('Press L to see the leaderboard!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 500)
        # heading_rect[0]+=150
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = tiny_font.render('Press M to change ball skin!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 560)
        # heading_rect[0]+=150
        screen.blit(heading_text, heading_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                to_return[0] = False
                return to_return
            elif event.type == pygame.KEYDOWN:

                # Leaderboard screen
                if event.key == pygame.K_l:
                    temp_data = leaderboard_screen(screen)
                    if temp_data == 'quit':
                        to_return[0] = False
                        return to_return
                    break

                # Ball Skin Screen
                if event.key == pygame.K_m:
                    temp_data = ball_skin_screen(screen)
                    if temp_data[0] == 'quit':
                        to_return[0] = False
                        print(id(to_return[1]))
                        to_return[1] = temp_data[1]
                        return to_return
                    break

                # Instructions Screen
                elif event.key == pygame.K_i:
                    temp_data = instructions_screen(screen)
                    if temp_data == False:
                        to_return[0] = False
                        return to_return
                    break
                return to_return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return to_return

        pygame.display.update()

def instructions_screen(screen):
    while True:
        screen.fill((255, 255, 255))
        text1 = big_font.render('Instructions', True, (255, 0, 255))
        heading_rect = text1.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(text1, heading_rect.topleft)

        screen.blit(small_font.render('1. Click To Move', True, (255, 0, 255)), (50, 150))
        screen.blit(small_font.render('2. write More Code', True, (255, 0, 255)), (50, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return True

        pygame.display.update()

def leaderboard_screen(screen):
    screen.fill((255, 255, 255))

    heading_text = big_font.render('Physics Game Leaderboard', True, (255, 0, 255))
    heading_rect = heading_text.get_rect()
    heading_rect.center = (WW // 2, 50)
    screen.blit(heading_text, heading_rect.topleft)

    heading_text = small_font.render('Fetching data... this Might take a couple of minutes...', True, (255, 0, 255))
    heading_rect = heading_text.get_rect()
    heading_rect.center = (WW // 2, 250)
    screen.blit(heading_text, heading_rect.topleft)

    pygame.display.update()

    Data = lb.receive()

    while True:
        screen.fill((255, 255, 255))

        heading_text = big_font.render('Physics Game Leaderboard', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press a Key to go back', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 150)
        screen.blit(heading_text, heading_rect.topleft)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                return 'start'


# noinspection DuplicatedCode
# pycharm setting msg above -_-     > LMAO xD
def score_screen(screen, score):
    while True:
        screen.fill((255, 255, 255))
        heading_text = big_font.render('You passed the Level!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = medium_font.render(f'Your Score {score}', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 350)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press a key to continue!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 450)
        screen.blit(heading_text, heading_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return True

        pygame.display.update()


def ball_skin_screen(screen):
    cursor_rect = pygame.Rect(0, 0, 10, 10)
    clicked = False

    # phew... simple solution to a complex problem 
    click_offset = 20  ## this is the gap b/w the focus and the ball image
    click_focus = pygame.Rect(0, 0, 0, 0)

    # default selected skin
    selected_skin = skins[0]

    while True:
        # Drawing
        screen.fill((255, 255, 255))

        heading_text = big_font.render('Choose ball Skin:', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press ESCAPE to go back', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.topleft = (0, WH - heading_rect.height)
        screen.blit(heading_text, heading_rect.topleft)

        ## too lazy to compare the x and y of each skin and mouse so, 
        ## shorter method > use rect collisions ;)
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        ## looping thru all skins and it's x coord
        for skin, x in zip(skins, range(48, WW, WW // len(skins))):
            ## maybe in future, will add another list of bigger imgs cuz these imgs are too low res
            scaled_skin = pygame.transform.scale2x(skin).convert_alpha()
            skin_rect = scaled_skin.get_rect(center=(x, WH // 2))
            screen.blit(scaled_skin, skin_rect.topleft)  ## Drawing all skins

            ## too much :brain: was req to make this whole thing work 
            ## phew..... at last ;)
            click_focus.width = skin_rect.width + click_offset
            click_focus.height = skin_rect.height + click_offset

            ## Select skin
            if selected_skin == skin:
                click_focus.center = (x, WH // 2)  ## focusing on the skin

            pygame.draw.ellipse(screen, PINK, click_focus, click_offset // 2)  ## drawing the focus circle
            if cursor_rect.colliderect(skin_rect):  ## colliderect OP!
                ## Clicking
                if clicked:
                    selected_skin = skin  ## changing the skin
        print(id(selected_skin))

        pygame.display.update()
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ['quit', selected_skin]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ['start', selected_skin]  ## Maybe, we can return the value of selected_skin instead of 'start'
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False


