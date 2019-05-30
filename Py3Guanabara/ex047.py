quantidade = 0
print('Os números pares de 1 a 50 são:')
x = int(input('Você deseja começar com qual número? '))
y = int(input('Você deseja terminar com qual número? '))
for c in range(x, y+1):
    if c % 2 == 0:
        quantidade += 1
        print(c, end=' ')
print('\nExistem {} números pares entre {} a {}'.format(quantidade, x, y))
