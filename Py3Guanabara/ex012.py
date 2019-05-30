d = float(input('Qual a porcentagem do desconto(%)?'))
preco = float(input('Qual o valor do produto? R$'))
desconto = preco - (preco * d / 100)
print('O valor do produto que era R${}, agora com {}% de desconto passa a ser R${:.2f}'.format(preco, d, desconto))
