import pygame
import sys
from pygame import sprite
from  settings import Settings
from bullet import Bullet
from aliens import Alien


def check_events(space_ship,game_settings,screen,bullets):


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            chech_key_down_events(event,game_settings,space_ship,screen,bullets)

        elif event.type == pygame.KEYUP:
            check_key_up_events(event,space_ship)



def chech_key_down_events(event,game_settings,space_ship,screen,bullets):

    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        space_ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to bullets group
        fire_bullet(game_settings,space_ship,screen,bullets)





def check_key_up_events(event,space_ship):
    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        space_ship.moving_left = False



def update_screen(game_settings,screen,space_ship,bullets,aliens):
    screen.fill(game_settings.bg_color)

    for bullet in bullets.sprites():
        update_bullet(bullet,bullets)
    aliens.draw(screen)
    space_ship.blitme()
    pygame.display.flip()



def update_bullet(bullet,bullets):
    if bullet.bullet_rect.bottom <= 0:
        bullets.remove(bullet)
    else:
        bullet.draw_bullet()


def fire_bullet(game_settings,space_ship,screen,bullets):
    new_bullet = Bullet(game_settings, space_ship, screen)
    bullets.add(new_bullet)


def create_fleet(game_settings,screen,aliens):
    # create a full fleet of aliens
    alien = Alien(game_settings,screen)
    alien_width = alien.rect.width
    number_of_aliens = get_alien_number(game_settings,alien_width)


    # creating first row of aliens
    for alien_number in range(number_of_aliens):
        create_alien(game_settings,screen,alien_number,aliens)








def get_alien_number(game_settings,alien_width):

    available_space_x = game_settings.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def create_alien(game_settings,screen,alien_number,aliens):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    aliens.add(alien)



