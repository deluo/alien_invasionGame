import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions


def run_game():
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(al_settings,screen)
    """开始游戏的主循环"""
    while True:
        game_functions.check_events(ship)
        ship.update(screen)
        game_functions.update_screen(al_settings,screen,ship)
run_game()