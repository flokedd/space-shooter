import pygame

class Ship:
    screen = None
    def __init__(self, image, size, start_pos) -> None:
        self.image = pygame.transform.scale(image, size)
        self.size = size
        self.start_pos = start_pos
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0], size[1])

    def draw(self):
        self.screen.blit(self.image, self.rect)