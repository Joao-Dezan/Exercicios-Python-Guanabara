valor = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: '))
tempo = int(input('Quantidade de anos para pagar a casa: '))
meses = tempo * 12
prestacao = valor / meses

print('Para pagar uma casa de R${:2f} em {} anos, a prestação mensal será de R${:2f}'.format(valor, tempo, prestacao))

if prestacao <= (salario * 30 / 100):
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')