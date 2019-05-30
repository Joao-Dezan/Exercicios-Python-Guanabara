from time import sleep
valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
opcao = []
while opcao != 5:
    print('')
    sleep(1)
    print('=-=' * 15)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>> Qual é a sua escolha? '))
    if opcao == 1:
        sleep(0.4)
        print('A soma entre {} e {} é {}!'.format(valor1, valor2, valor1+valor2))
    elif opcao == 2:
        sleep(0.4)
        print('O produto de {} e {} é {}!'.format(valor1, valor2, valor1*valor2))
    elif opcao == 3:
        if valor1 > valor2:
            sleep(0.4)
            print('O maior número é {}!'.format(valor1))
        elif valor2 > valor1:
            sleep(0.4)
            print('O maior número é {}!'.format(valor2))
        else:
            sleep(0.4)
            print('Os dois números são iguais!')
    elif opcao == 4:
        sleep(0.2)
        print('Informe os números novamente:')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
    else:
        sleep(0.1)
        print('Opção inválida. Tente novamente!')
print('Finalizando...')
sleep(1.5)
print('=-=' * 15)
print('Fim do programa! Volte sempre!')
