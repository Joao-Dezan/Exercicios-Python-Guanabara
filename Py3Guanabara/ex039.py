from datetime import date
import sys

ano = int(input('Informe seu ano de nascimento: '))
print('=-='*10)
print('Qual o seu sexo? \n[ 1 ] para feminino\n[ 2 ] para masculino')
sexo = int(input('Coloque aqui >>> '))
print('=-='*10)
idade = date.today().year - ano
if sexo == 1:
    print('Você não precisa fazer o alistamento!')
    print('Mesmo assim você deseja simular o seu alistamento? \n[ 1 ] para sim\n[ 2 ] para não')
    alistamento = int(input('>>> '))
    print('\033[0;34m=-=\033[m'*10)
    if alistamento == 1:
        sexo = 2
        print('\033[0;36mBem-vinda ao alistamento\033[m')
        print('\033[0;34m=-=\033[m' * 10)
    elif alistamento == 2:
        print('Tenha um bom dia senhorita!')
        sys.exit()

print('Você deseja simular o seu alistamento agora? \n[ 1 ] para sim\n[ 2 ] para não')
alistamento = int(input('>>> '))
if alistamento == 2:
    print('Tenha um bom dia senhor(a)!')
if alistamento == 1 and sexo == 2:
        if idade > 0:
            print('=-='*10)
            print('Quem nasceu em {}, em {} tem {} anos!'.format(ano, date.today().year, idade))
        if 0 <= idade < 18:
            print('=-=' * 10)
            print('Você não tem 18 anos. Ainda falta {} anos para o seu alistameto!'.format(18-idade))
            print('Seu alistamento vai ser em {}!'.format(date.today().year + (18 - idade)))
        elif idade == 18:
            print('=-=' * 10)
            print('Seu alistamento acontece neste ano de {}!'.format(date.today().year))
        elif idade > 18:
            print('=-=' * 10)
            print('Você já deveria ter se alistado há {} anos!'.format(idade-18))
            print('Seu alistamento foi em {}!'.format(date.today().year - (idade-18)))
        elif idade < 0:
            print('=-=' * 10)
            print('Desculpe, mas você ainda nem nasceu!')