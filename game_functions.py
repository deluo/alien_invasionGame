import sys
import pygame

def check_events(ship):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_kedown_events(event,ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

def check_kedown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
            
            
def update_screen(al_settings,screen,ship):
    screen.fill(al_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
