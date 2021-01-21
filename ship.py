import pygame


class Ship():
    def __init__(self, settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.settings = settings
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.center += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
