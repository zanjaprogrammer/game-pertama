import keyboard
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
player = pygame.sprite.Sprite()
player.image = pygame.image.load('playerkiri.png')
player.rect = player.image.get_rect()
kiri = 200
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
        print('kiri')
        power = power - 1
        print(power)
        kiri = kiri - 10
        player.rect.topleft = [kiri, 250]
        screen.fill((0, 0, 0))
        screen.blit(player.image, player.rect)
    if pressed[pygame.K_RIGHT]:
        print('kanan')
        power = power + 1
        print(power)
        kiri = kiri + 10
        player.rect.topleft = [kiri, 250]
        screen.fill((0, 0, 0))  # fill the screen
        screen.blit(player.image, player.rect)
    # if keyboard.is_pressed('a'):
    #     print('kiri')
    #     power = power - 0.01
    #     print(power)
    # if keyboard.is_pressed('d'):
    #     print('kanan')
    #     power = power + 0.01
    #     print(power)
    # if keyboard.is_pressed('w'):
    #     print('maju')
    # if keyboard.is_pressed('s'):
    #     print('mundur')
    #
    # if keyboard.is_pressed('esc'):
    #     break
    #

    pygame.display.flip()
    clock.tick(40)
print('Game over!')