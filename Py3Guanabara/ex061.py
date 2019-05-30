print('Gerador de PA, com 10 termos')
print('-=-' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0
while cont != 10:
    print(t, end=' - ')
    t += r
    cont += 1
print('FIM')