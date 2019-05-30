numero = int(input('Digite um número inteiro qualquer: '))
base = int(input('''Para que base você deseja coverter esse número?
[1] para binário\n[2] para octal\n[3] para hexadecimal\n\033[36m>>>\033[m'''))
if base == 1:
    print('{} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
