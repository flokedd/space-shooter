import pygame

class Ship:
    screen = None
    def __init__(self, image, size, start_pos, speed) -> None:
        self.image = pygame.transform.scale(image, size)
        self.size = size
        self.start_pos = start_pos
        self.speed = speed
        self.bullets = []
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0], size[1])

    def shoot(self, bullet):
        self.bullets.append(bullet)

    def move(self, direction_x, direction_y):
        self.rect = self.rect.move(self.speed * direction_x, self.speed * direction_y)

    def draw(self):
        self.screen.blit(self.image, self.rect)