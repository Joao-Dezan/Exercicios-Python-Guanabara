a = float(input('Qual a porcentagem do aumento (%)? '))
salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario * a / 100)
print('O funcionário que recebia R${}, agora com {}% de desconto passa a receber R${:.2f}'.format(salario, a, aumento))