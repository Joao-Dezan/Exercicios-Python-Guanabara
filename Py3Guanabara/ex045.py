from random import randint
from time import sleep
print('{:=^40}'.format(' Game de Jokenpô '))
itens = ('Pedra', 'Papel', 'Tesoura')
print('Escolha sua Jogada: ')
print('[ 0 ] para pedra\n[ 1 ] para papel\n[ 2 ] para tesoura')
escolha = int(input('Opção: '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(0.2)
print('\033[0;31m-=-\033[m'*15)
if 3 > escolha >= 0:
    print('O COMPUTADOR escolheu {}\nO JOGADOR escolheu {}'.format(itens[computador], itens[escolha]))
else:
    print('Opção inválida. Tente novamente!')
print('\033[0;31m-=-\033[m'*15)
if escolha == computador:
    print('EMPATE!')
elif escolha == 0 and computador == 1:
    print('O COMPUTADOR venceu!')
elif escolha == 0 and computador == 2:
    print('O JOGADOR venceu!')
elif escolha == 1 and computador == 0:
    print('O JOGADOR venceu!')
elif escolha == 1 and computador == 2:
    print('O COMPUTADOR venceu!')
elif escolha == 2 and computador == 0:
    print('O COMPUTADOR venceu!')
elif escolha == 2 and computador == 1:
    print('O JOGADOR venceu!')
