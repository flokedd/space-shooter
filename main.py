import pygame, os
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
player_image = pygame.image.load(os.path.join('assets/ships', 'player-ship.png'))

player = Player(player_image, (35, 42), (screen.get_size()[0]/2-(35/2), screen.get_size()[1]-55), 5)
player.screen = screen

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player.move(0, -1)
    if keys[pygame.K_s]:
        player.move(0, 1)
    if keys[pygame.K_a]:
        player.move(-1, 0)
    if keys[pygame.K_d]:
        player.move(1, 0)

    player.draw()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()