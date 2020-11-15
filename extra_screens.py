import pygame, time
from settings import small_font, big_font, WW, WH


def welcome(screen):
    while True:
        screen.fill((0, 0, 0))
        heading_text = big_font.render('Welcome to the Physics Game!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 50)
        screen.blit(heading_text, heading_rect.topleft)

        heading_text = big_font.render('Press a key to continue!', True, (255, 0, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = (WW // 2, 350)
        screen.blit(heading_text, heading_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                return 'start'

        pygame.display.update()
