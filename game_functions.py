import sys
import pygame
from bullet import Bullet

def check_events(al_settings,screen,ship,bullets):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_kedown_events(al_settings,screen,event,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

def check_kedown_events(al_settings,screen,event,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to Group
        bullet = Bullet(al_settings,screen,ship)
        bullets.add(bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
            
            
def update_screen(al_settings,screen,ship,bullets):
    screen.fill(al_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    
    

