soma_idade = 0
mm = 0
nomev = ''
mvelho = 0
for dados in range(1, 5):
    print('----- {}ª PESSOA -----'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    soma_idade += idade
    if idade < 20 and sexo == 'F':
        mm += 1
    if idade == 1 and sexo == 'M':
        mvelho = idade
        nomev = nome
    else:
        if idade > mvelho and sexo == 'M':
            mvelho = idade
            nomev = nome
media = soma_idade / 4
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(mvelho, nomev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mm))
