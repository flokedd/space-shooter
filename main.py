import pygame, os, time, random
from ship import Ship
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
last_enemy = time.time()
player_image = pygame.image.load(os.path.join('assets/ships', 'player-ship.png'))
enemy_one_image = pygame.image.load(os.path.join('assets/ships', 'enemy-1.png'))

Ship.screen = screen

player = Player(player_image, (35, 42), (screen.get_size()[0]/2-(35/2), screen.get_size()[1]-55), 5)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        if player.rect.top > 0:
            player.move(0, -1)
    if keys[pygame.K_s]:
        if player.rect.bottom < screen.get_size()[1]:
            player.move(0, 1)
    if keys[pygame.K_a]:
        if player.rect.left > 0:
            player.move(-1, 0)
    if keys[pygame.K_d]:
        if player.rect.right < screen.get_size()[0]:
            player.move(1, 0)
    
    if keys[pygame.K_SPACE]:
        bullet = Bullet(player, (player.rect.x + player.size[0]/2-3.5, player.rect.y), (7, 10), 5)
        player.shoot(bullet)

    if last_enemy + 2 < time.time():
        Enemy(enemy_one_image, (42, 32), (random.randint(0, screen.get_size()[0]), 0), 5)
        last_enemy = time.time()

    for b in player.bullets:
        b.move(0, -1)
        b.draw()

    for e in Enemy.enemies:
        e.move(0, 1)
        e.draw()

    player.draw()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()