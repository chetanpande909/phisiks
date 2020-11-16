import pygame, time
from settings import small_font, medium_font, big_font, WW, WH
import leaderboard as lb

# Player Skins
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

def welcome_screen(screen):
    while True:
        screen.fill((255, 255, 255))
        heading_text = big_font.render('Welcome to the Physics Game!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press a key to continue!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 350)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press L to see the leaderboard!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 450)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press M to change ball skin!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 550)
        screen.blit(heading_text, heading_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Leaderboard screen
                if event.key == pygame.K_l:
                    temp_data = leaderboard_screen(screen)
                    if temp_data == 'quit':
                        return False
                    break
                # Ball Skin Screen
                if event.key == pygame.K_m:
                    temp_data = ball_skin_screen(screen)
                    if temp_data == 'quit':
                        return False
                    break
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
# pycharm setting msg above -_-
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

    while True:
        # Drawing
        screen.fill((255, 255, 255))

        heading_text = big_font.render('Choose ball Skin:', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = small_font.render('Press ESCAPE to go back', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.topleft = (0, WH-heading_rect.height)
        screen.blit(heading_text, heading_rect.topleft)

        for skin, x in zip(skins, range(16, WW, WW//len(skins))):
            scaled_skin = pygame.transform.scale2x(skin)
            screen.blit(scaled_skin, (x, WH//2))

        pygame.display.update()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'start'
