peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura * altura)
print('\nO IMC dessa pessoa é de {:.1f}'.format(imc))
print('Classificação: ', end='')
if imc < 16:
    print('Magreza grave')
    print('Você está muito abaixo do peso, cuidado!')
if 16 <= imc < 17:
    print('Magreza moderada')
    print('Você deve se alimentar mais!')
elif 17 <= imc < 18.5:
    print('Magreza leve')
    print('Você está um pouco abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Saudável')
    print('Você está com o peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso')
    print('Você está um pouco acima do peso!')
elif 30 <= imc < 35:
    print('Obesidade Grau I')
    print('Cuidado, você deve fazer uma dieta!')
elif 30 <= imc < 40:
    print('Obesidade Grau II (severa)')
    print('Você muito acima do peso, cuidado!')
elif imc > 40:
    print('Obesidade Grau III (mórbida)')
    print('Você está acima do peso ao extremo, procure um médico!')
