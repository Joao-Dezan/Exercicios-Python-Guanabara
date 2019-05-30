num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\nO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
