import pygame

class Bullet:
    def __init__(self, ship, pos, size) -> None:
        self.ship = ship
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self):
        pygame.draw.rect(self.ship.screen, (255, 255, 255), self.rect)