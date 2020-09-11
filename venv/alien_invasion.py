import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from space_ship import Ship
import  game_functions as gf
from aliens import Alien


def run_game():
    #initialize game and create screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    space_ship = Ship(game_settings,screen)
    #make a group to store bullets and aliens
    bullets = Group()
    aliens =Group()
    gf.create_fleet(game_settings,screen,space_ship,aliens)





    #start main loop for the game
    while True:

        #watch for keyboard and mouse events
        gf.check_events(space_ship,game_settings,screen,bullets)
        space_ship.update()
        if len(bullets)>=1:
            bullets.update()
        gf.update_screen(game_settings, screen, space_ship, bullets,aliens)








run_game()

