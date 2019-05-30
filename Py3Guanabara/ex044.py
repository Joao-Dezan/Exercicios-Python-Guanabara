print('\n{:=^40}'.format(' Lojas Dezan '.upper()))
valor = float(input('Qual o valor das compras? R$'))
print('Formas de pagamento'.upper())
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    desconto = valor - 10 / 100 * valor
    print('Sua compra de R${:.2f}, à vista irá custar R${:.2f}'.format(valor, desconto))
elif opcao == 2:
    desconto = valor - 5 / 100 * valor
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, desconto))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(valor/2))
    print('Sua compra vai custar exatamente R${:.2f} no final!'.format(valor))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        juros = valor + 20 / 100 * valor
        parcelamento = juros / parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcelamento))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, juros))
    else:
        print('Você deve escolher 3x ou mais a quantidade de parcelas. Tente novamente')
else:
    print('Opção inválida. Tente novamente')
