print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont1 = 0
while cont1 != 10:
    print(t, end=' - ')
    t += r
    cont1 += 1
tm = 1
cont3 = 0
while tm > 0:
    cont2 = 10
    tm = int(input('\nQuantos termos você deseja ver a mais? '))
    while cont2 != cont1 + tm:
        print(t, end=' - ')
        t += r
        cont2 += 1
        cont3 += 1
print('Progressão finalizada com {} termos mostrados.'.format(10 + cont3))

