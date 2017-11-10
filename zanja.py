import keyboard
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
player = pygame.sprite.Sprite()
player.image = pygame.image.load('playerkiri.png')
player.rect = player.image.get_rect()
kiri = 200
atas = 250
player.rect.topleft = [kiri, 250]
screen.blit(player.image, player.rect)
clock = pygame.time.Clock()


nama = 'kahfi'
power = 100

print(nama)

while power > 0:
    # print('Game is running')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            power = -1

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        power = power - 1
        kiri = kiri - 10

    if pressed[pygame.K_RIGHT]:
        power = power + 1
        kiri = kiri + 10

    if pressed[pygame.K_UP]:
        atas = atas - 10

    if pressed[pygame.K_DOWN]:
        atas = atas + 10
    player.rect.topleft = [kiri, atas]
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(40)
print('Game over!')