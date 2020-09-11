import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,game_settings,screen):
        super(Alien,self).__init__()
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load("Include\images\ship2.jpeg")
        self.rect = self.image.get_rect()
        self.rect.top = 0

        #store aliens exact position
        self.top = float(self.rect.top)


    def blitme(self):
        self.screen.blit(self.image,self.rect)


