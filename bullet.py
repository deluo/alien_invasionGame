import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,al_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        #create a rectangle bullet at (0,0)
        self.rect = pygame.Rect(0,0,al_settings.bullet_width,al_settings.bullet_height)
        # set bullet's location equal ship's 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = al_settings.bullet_color
        self.speed_factor = al_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        # draw bullet on the screen
        pygame.draw.rect(self.screen,self.color,self.rect)
        