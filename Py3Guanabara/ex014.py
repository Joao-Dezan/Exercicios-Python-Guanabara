tem = float(input('Qual é a temperatura? '))
t = input('Sua temperatura é em C(p/ Celsius) ou F(p/ Farenheint)?')
f = ((9*tem) / 5) + 32
c = ((5 * tem) - 160) / 9
if t == 'C':
    print('A temperatura de {}ºC corresponde a {}ºF'.format(tem, f))
elif t == 'F':
    print('A temperatura de {}ºF corresponde a {}ºC'.format(tem, c))
elif t == 'f':
    print('A temperatura de {}ºF corresponde a {}ºC'.format(tem, c))
elif t == 'c':
    print('A temperatura de {}ºC corresponde a {}ºF'.format(tem, f))
