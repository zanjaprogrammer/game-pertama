import keyboard
import pygame

pygame.init()
# screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1920, 1080))
player2 = pygame.sprite.Sprite()
player2.image = pygame.image.load('redship.png')
player2.rect = player2.image.get_rect()

player1 = pygame.sprite.Sprite()
player1.image = pygame.image.load('blueship.png')
player1.rect = player2.image.get_rect()
kiri_player = 200
atas_player = 250
player2.rect.topleft = [kiri_player, atas_player]

peluru1 = pygame.sprite.Sprite()
peluru1.image = pygame.image.load('pelurubiru.png')

kiri_enemy = 300
atas_enemy = atas_player
player1.rect.topleft = [kiri_enemy, atas_enemy]
clock = pygame.time.Clock()


nama = 'kahfi'
power = 100

print(nama)

joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    for j in range(0, joystick_count):
        name = pygame.joystick.Joystick(j).get_name().strip()
        print (name)
        if name == 'Twin USB Gamepad':
            player1_joystick = pygame.joystick.Joystick(j)
            player1_joystick.init()
        if name == 'Controller (Gamepad F310)':
            player2_joystick = pygame.joystick.Joystick(j)
            player2_joystick.init()

bg = pygame.image.load("latarbelakang2.jpg")








while power > 0:
    # print('Game is running')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            power = -1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    pressed = pygame.key.get_pressed()
    h2 = player2_joystick.get_axis(0)
    v2 = player2_joystick.get_axis(1)
    # print (h_axis_pos, v_axis_pos)

    h1 = player1_joystick.get_axis(0)
    v1 = player1_joystick.get_axis(1)
    # print (h1, v1)

    # tombol senjata
    r1 = player1_joystick.get_button(5)
    if r1 == 1:
        # gambar peluru

        print (r1)

    tabrakan = pygame.sprite.collide_rect(player2, player1)

    if (pressed[pygame.K_LEFT] or h2 == -1):
        power = power - 1
        kiri_player = kiri_player - 10

    if (pressed[pygame.K_RIGHT] or h2 == 0.999969482421875):
        power = power + 1
        kiri_player = kiri_player + 10

    if (pressed[pygame.K_UP] or v2 == -1):
        atas_player = atas_player - 10

    if (pressed[pygame.K_DOWN] or v2 == 0.999969482421875):
        atas_player = atas_player + 10

    if (h1 == -1):
        kiri_enemy = kiri_enemy - 10
    if (h1 == 0.999969482421875):
         kiri_enemy = kiri_enemy + 10
    if (v1 == -1):
        atas_enemy = atas_enemy - 10
    if (v1 == 0.999969482421875):
        atas_enemy = atas_enemy + 10

    player2.rect.topleft = [kiri_player, atas_player]
    player1.rect.topleft = [kiri_enemy, atas_enemy]
    # screen.fill((255,0 ,0 ))
    screen.blit(bg, (0, 0))
    screen.blit(player2.image, player2.rect)
    screen.blit(player1.image, player1.rect)
    if r1 == 1:
        screen.blit(peluru1.image, player1.rect)

    pygame.display.flip()
    clock.tick(40)
print('Game over!')