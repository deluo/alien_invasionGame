import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, al_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.al_settings = al_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
