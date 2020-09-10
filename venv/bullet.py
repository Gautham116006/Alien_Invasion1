import pygame
from  pygame.sprite import Sprite
from settings import Settings




class Bullet(Sprite):
    def __init__(self,game_settings,space_ship,screen):
        super(Bullet,self).__init__()
        self.screen = screen
        self.bullet_width = game_settings.bullet_width
        self.bullet_height = game_settings.bullet_height
        self.bullet_rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.bullet_rect.centerx = space_ship.ship_rect.centerx
        self.bullet_rect.top = space_ship.ship_rect.top
        # store the bullet position as decimal value
        self.y = float(self.bullet_rect.y)

        # color and speed
        self.bullet_color = game_settings.bullet_color
        self.bullet_speed = game_settings.bullet_speed_factor

    def update(self):
            self.y -= self.bullet_speed
            self.bullet_rect.y = self.y


    def draw_bullet(self):
        # draw bullet to screen
        pygame.draw.rect(self.screen,self.bullet_color,self.bullet_rect)







