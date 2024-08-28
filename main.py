import pygame, os
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
player_image = pygame.image.load(os.path.join('assets/ships', 'player-ship.png'))

player = Player(player_image, (35, 42), (screen.get_size()[0]/2-(35/2), screen.get_size()[1]-55))
player.screen = screen

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player.draw()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()