class Settings():
    # a class containing all th settings FOR ALIEN INVASION
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 750
        self.bg_color = (30,30,30)
        self.ship_speed = 1.5
        #bullet settings
        self.bullet_speed_factor = 1.7
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255,255,0)
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # fleet direction 1 represents right and -1 represents left
        self.fleet_direction = -1

