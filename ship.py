import pygame


class Ship(object):
    def __init__(self, al_settings, screen):
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.move_right = False
        self.move_left = False
        self.al_settings = al_settings

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, screen):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.al_settings.ship_speed_factor
        elif self.move_left and self.rect.left > 0:
            self.center -= self.al_settings.ship_speed_factor

        self.rect.centerx = self.center
