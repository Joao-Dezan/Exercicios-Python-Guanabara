from datetime import date

nascimento = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos'.format(nascimento, idade))
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')