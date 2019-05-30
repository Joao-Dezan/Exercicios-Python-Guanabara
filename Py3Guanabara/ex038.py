num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
print('')
if num1 == num2 and num1 != num3:
    print('O PRIMEIRO e SEGUNDO número são iguais!')
elif num1 == num3 and num1 != num2:
    print('O PRIMEIRO e TERCEIRO número são iguais!')
elif num2 == num3 and num2 != num1:
        print('O SEGUNDO e TERCEIRO número são iguais!')
if num1 > num2 and num1 > num3:
    print('O PRIMEIRO número é maior')
elif num2 > num1 and num2 > num3:
    print('O SEGUNDO número é maior')
elif num3 > num2 and num3 > num1:
        print('O TERCEIRO número é maior')
if num1 < num2 and num1 < num3:
    print('O PRIMEIRO número é menor')
elif num2 < num1 and num2 < num3:
    print('O SEGUNDO número é menor')
elif num3 < num2 and num3 < num1:
        print('O TERCEIRO número é menor')
elif num1 == num2 and num1 == num3 and num2 == num3:
    print('Os três números são iguais!')
else:
    print('Desculpe valor inválido. Tente novamente')