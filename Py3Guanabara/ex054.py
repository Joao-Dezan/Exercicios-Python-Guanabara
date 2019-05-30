from datetime import date
maiores = 0
menores = 0

for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = date.today().year - nascimento
    if idade >= 21:
        maiores += 1
    elif idade < 21:
        menores += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(maiores))
print('E {} pessoas menores de idade!'.format(menores))
