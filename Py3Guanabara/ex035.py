m1 = float(input('Informe o primeiro segmento: '))
m2 = float(input('Informe o segundo segmento: '))
m3 = float(input('Informe o terceiro segmento: '))
if (m2 - m3) < m1 < (m2 + m3) and (m1 - m3) < m2 < (m1 + m3) and (m1 - m2) < m3 < (m1 + m2):
    print('Esses segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Esses segmentos acima NÃO PODEM FORMAR um triângulo!')
