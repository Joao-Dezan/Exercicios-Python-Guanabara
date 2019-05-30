percorrido = float(input('Quantos quilometros foi percorrido? '))
dias = int(input('Por quantos dias foi alugado o carro? '))
preco = (60 * dias) + (0.15 * percorrido)
print('O preço total a pagar pelo aluguel é R${:.2f}'.format(preco))
