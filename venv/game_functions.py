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


def create_fleet(game_settings,screen,space_ship,aliens):
    # create a full fleet of aliens
    alien = Alien(game_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = space_ship.ship_rect.height
    number_of_aliens = int(get_alien_number(game_settings,alien_width))
    number_of_rows = int(get_number_of_rows(game_settings,alien_height,ship_height))
    for row_number in range(number_of_rows - 1):
        for alien_number in range(number_of_aliens):
             create_alien(game_settings,screen,alien_number,aliens,row_number)











def get_alien_number(game_settings,alien_width):

    available_space_x = game_settings.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def create_alien(game_settings,screen,alien_number,aliens,row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.y = alien_height + (2 * alien_height * row_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_of_rows(game_settings,alien_height,ship_height):
    available_space_y = (game_settings.screen_height -(3*alien_height)-ship_height)
    num_rows = int(available_space_y/(2*alien_height))
    return num_rows


def check_fleet_edges(game_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_fleet_edges():
            change_fleet_direction(game_settings,aliens)
            break


def change_fleet_direction(game_settings,aliens):
    #drop the enire fleet and change its direction
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def update_aliens(game_settings,aliens):
    # update the position of each alien to the right
    check_fleet_edges(game_settings,aliens)
    aliens.update()







