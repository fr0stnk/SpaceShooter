import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from game_functions import *
from pygame.sprite import Group


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(settings, screen)
    # Создание пришельцев
    alien = Alien(settings, screen)
    # Создание группы снарядов
    bullets = Group()
    aliens = Group()

    create_fleet(settings, screen, aliens)



    # Назначение цвета фона.
    # bg_color = (230, 230, 230)

    # Запуск основного цикла игры.
    while True:
        # При каждом проходе цикла перерисовывается экран.
        check_events(settings, screen, ship, bullets)
        # Отображение последнего прорисованного экрана.
        # Отслеживание событий клавиатуры и мыши.
        ship.update()
        alien.update()
        update_bullets(bullets)

        update_screen(settings, screen, ship, aliens, bullets)


run_game()
