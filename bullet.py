import pygame

class Bullet:
    def __init__(self, ship, pos, size, speed) -> None:
        self.ship = ship
        self.speed = speed
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def move(self, direction_x, direction_y):
        self.rect = self.rect.move(self.speed * direction_x, self.speed * direction_y)

    def draw(self):
        pygame.draw.rect(self.ship.screen, (255, 255, 255), self.rect)