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

joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(1)
    my_joystick.init()


while power > 0:
    # print('Game is running')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            power = -1

    pressed = pygame.key.get_pressed()
    h_axis_pos = my_joystick.get_axis(0)
    v_axis_pos = my_joystick.get_axis(1)
    print (h_axis_pos, v_axis_pos)

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