import pygame, time

class Ship:
    screen = None
    def __init__(self, image, size, start_pos, speed) -> None:
        self.image = pygame.transform.scale(image, size)
        self.size = size
        self.start_pos = start_pos
        self.speed = speed
        self.bullets = []
        self.bullet_delay = 1
        self.last_shot = time.time()
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0], size[1])

    def shoot(self, bullet):
        if self.last_shot + self.bullet_delay < time.time():
            self.bullets.append(bullet)
            self.last_shot = time.time()

    def move(self, direction_x, direction_y):
        self.rect = self.rect.move(self.speed * direction_x, self.speed * direction_y)

    def draw(self):
        self.screen.blit(self.image, self.rect)