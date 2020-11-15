import pygame, time
from settings import small_font, big_font, WW, WH
import leaderboard as lb

def welcome(screen):
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    temp_data = leaderboard_screen(screen)
                    if temp_data == 'quit':
                        return 'quit'
                    break
                return 'start'

        pygame.display.update()

def leaderboard_screen(screen):
    screen.fill((255,255,255))

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
