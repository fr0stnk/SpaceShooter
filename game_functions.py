import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # Переместить корабль вправо.
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # print('shoot')
            fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            # Переместить корабль вправо.
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #for alien in aliens.sprites():

    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль.
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        # print(bullet.y)
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))


def fire_bullet(settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут."""
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(settings, screen, aliens):
    #new_alien = Alien(settings, screen)
    #aliens.add(new_alien)

    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду.
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)