import keyboard

nama = 'kahfi'
power = 100

print(nama)

while power > 0:
    print('Game is running')
    if keyboard.is_pressed('a'):
        print('kiri')
        power = power - 0.01
        print(power)
    if keyboard.is_pressed('d'):
        print('kanan')
        power = power + 0.01
        print(power)
    if keyboard.is_pressed('w'):
        print('maju')
    if keyboard.is_pressed('s'):
        print('mundur')

    if keyboard.is_pressed('esc'):
        break
print('Game over!')