velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO! Você passou do limite de velocidade que é de 80km/h!\033[m')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
if velocidade == 80:
    print('-=-'*30)
    print('Cuidade! Reduza a velocidade! Você está passando do limite de velocidade que é de 80km/h!')
    print('-=-'*30)
print('Tenha um bom dia!')
