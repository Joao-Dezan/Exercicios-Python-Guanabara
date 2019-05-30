h = float(input('Digite a altura da parede em metros: '))
b = float(input("Digite a largura da parede em metros: "))
a = b * h
t = a / 2
print('Essa parede tem uma dimensão de {}m x {}m e sua área é {}m².'.format(b, h, a))
print('E para pintar essa parede precisaria de {:.2f}l de tintas.'.format(t))
