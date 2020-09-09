import pygame

class Ship():

    def __init__(self,game_settings,screen):
        # initialize the ship and set it's starting position
        self.screen = screen
        self.game_settings = game_settings
        #load ship image and get its rectangle
        self.image = pygame.image.load("Include\images\space_ship.jpeg")
        self.ship_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #start each ship at bottom centre of screen
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom
        #store a decimal value for the ships center
        self.center = float(self.ship_rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right == True:
            if self.ship_rect.centerx<=1050:
                self.center+= self.game_settings.ship_speed
        elif self.moving_left == True:
            if self.ship_rect.centerx >= 50 :
                self.center -= self.game_settings.ship_speed

        # update rectangle from self.center
        self.ship_rect.centerx = self.center

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image,self.ship_rect)



