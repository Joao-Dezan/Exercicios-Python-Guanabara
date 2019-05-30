distancia = float(input('Qual a distâcia da viagem (em km)? '))
if distancia <= 200:
    preco = distancia * 0.5
    print('O preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(preco))
