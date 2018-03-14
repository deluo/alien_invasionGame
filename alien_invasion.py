import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(al_settings,screen)
    #创建一个存储子弹的编组
    bullets = Group()

    """开始游戏的主循环"""
    while True:
        gf.check_events(al_settings,screen,ship,bullets)
        ship.update(screen)
        bullets.update()
        gf.update_screen(al_settings,screen,ship,bullets)
run_game()