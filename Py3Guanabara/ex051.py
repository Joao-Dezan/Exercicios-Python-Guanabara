primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual a razão da PA? '))
print('{}'.format(primeiro), end=' > ')
for c in range(1, 10):
    primeiro += razao
    print('{}'.format(primeiro), end=' > ')
print('Acabou')
