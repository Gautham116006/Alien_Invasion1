import pygame
import sys
from pygame import sprite
from  settings import Settings




def check_events(space_ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            chech_key_down_events(event,space_ship)

        elif event.type == pygame.KEYUP:
            check_key_up_events(event,space_ship)



def chech_key_down_events(event,space_ship):

    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        space_ship.moving_left = True
    elif event.key == pygame.K_SPACE:

        # create a new bullet and add it to bullets group

        new_bullet = Bullet(game_settings,space_ship,screen)
        bullets.add(new_bullet)



def check_key_up_events(event,space_ship):
    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        space_ship.moving_left = False



def update_screen(game_settings,screen,space_ship,bullets):
    screen.fill(game_settings.bg_color)
    space_ship.blitme()
    pygame.display.flip()
