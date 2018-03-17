import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(al_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kedown_events(al_settings, screen, event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_kedown_events(al_settings, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to Group
        bullet = Bullet(al_settings, screen, ship)
        bullets.add(bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(al_settings, screen, ship, aliens, bullets):
    screen.fill(al_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def calc_fleet_num(al_settings, alien_width):
    availabel_space_x = al_settings.screen_width - 2 * alien_width
    number_alien_x = int(availabel_space_x / (2 * alien_width))
    return number_alien_x


def calc_fleet_rows(al_settings, alien_height):
    availabel_space_y = al_settings.screen_height - alien_height
    if int(availabel_space_y / alien_height) >= 3:
        number_alien_y = 3
    else:
        number_alien_y = int(availabel_space_y / alien_height)
    return number_alien_y


def create_aliens(al_settings, screen, alien_num, alien_row, aliens):
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = float(alien_width + 2 * alien_num * alien_width)
    alien.y = float(alien_height + 2*alien_row*alien_height)
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_alien_fleet(al_settings, screen, aliens):
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    num_alien_rows = calc_fleet_rows(al_settings, alien_height)
    num_alien_x = calc_fleet_num(al_settings, alien_width)
    for alien_row in range(num_alien_rows):
        for alien_num in range(num_alien_x):
            create_aliens(al_settings, screen, alien_num, alien_row, aliens)
