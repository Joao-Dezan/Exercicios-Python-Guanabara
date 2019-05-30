soma = 0
cont = 0
for num in range(1, 7):
    ns = int(input('Digite o {}° número: '.format(num)))
    if ns % 2 == 0:
        cont += 1
        soma += ns
if cont > 1:
    print('A soma dos {} números pares é {}'.format(cont, soma))
elif cont == 1:
    print('Dentre os números digitados existe apenas um par, que é o {}'.format(soma))
