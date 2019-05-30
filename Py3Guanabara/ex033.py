v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
v3 = float(input('Terceiro valor: '))

maior = v3
if v2 < v1 and v3 < v1:
    maior = v1
if v1 < v2 and v3 < v2:
    maior = v2

menor = v3
if v2 > v1 and v3 > v1:
    menor = v1
if v1 > v2 and v3 > v2:
    menor = v2
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
