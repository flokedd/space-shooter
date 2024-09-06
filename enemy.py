import pygame
from ship import Ship

class Enemy(Ship):
    enemies = []
    def __init__(self, image, size, start_pos, speed) -> None:
        super().__init__(image, size, start_pos, speed)
        self.image = pygame.transform.rotate(self.image, 180)
        self.enemies.append(self)