m1 = float(input('Informe o primeiro segmento: '))
m2 = float(input('Informe o segundo segmento: '))
m3 = float(input('Informe o terceiro segmento: '))
if (m2 - m3) < m1 < (m2 + m3) and (m1 - m3) < m2 < (m1 + m3) and (m1 - m2) < m3 < (m1 + m2):
    print('Esses segmentos acima PODEM FORMAR um triângulo ', end='')
    if m1 == m2 == m3:
        print('Equilátero!'.upper())
    elif m1 == m2 and m1 != m3 or m1 == m3 and m1 != m2 or m2 == m3 and m2 != m1:
        print('Isósceles!'.upper())
    elif m1 != m2 != m3 != m1:
        print('Escaleno'.upper())
else:
    print('Esses segmentos acima NÃO PODEM FORMAR um triângulo!')

