import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,game_settings,screen):
        super(Alien,self).__init__()
        self.game_settings = game_settings

        self.image = pygame.image.load("Include\images\ship2.jpeg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()






    def update(self):
        # move alien right
        self.x = float(self.rect.x)
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x


    def check_fleet_edges(self):
        # check for the screens edge
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True


