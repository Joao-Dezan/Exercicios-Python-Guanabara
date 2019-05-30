num = int(input('Digite um número para ver o seu fatorial: '))
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while num > 1:
    print(num, end=' x ')
    fatorial = fatorial * num
    num = num - 1
print('1 = {}'.format(fatorial))