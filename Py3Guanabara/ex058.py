from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
palpite = 11
tentativas = 0
while computador != palpite:
    palpite = int(input('Qual é seu palpite?'))
    tentativas += 1
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
print('Acertou com {} tentetivas. Parabéns!'.format(tentativas))
