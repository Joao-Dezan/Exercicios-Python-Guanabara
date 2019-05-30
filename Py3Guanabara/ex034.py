salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento = 15
    novo = salario + (salario*15/100)
else:
    aumento = 10
    novo = salario + (salario*10/100)

print('O salário que antes era R${:.2f}, agora com o aumento de {}% passa a ser R${:.2f}!'.format(salario, aumento, novo))
