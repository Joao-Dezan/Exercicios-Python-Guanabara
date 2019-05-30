me = float(input('Digite a medida: '))
medida = input('Qual o tipo de medida que você digitou? ')
cm = me * 100
mm = me * 1000
dm = me * 10
hm = me / 100
dam = me / 10
km = me / 1000
if medida == 'metros':
    print('A medida {}m corresponde a: '.format(me))
    print('{:.0f}mm\n{:.0f}cm\n{:.0f}dm\n{:.2f}dam\n{:.2f}hm\n{:.2f}km'.format(mm, cm, dm, dam, hm, km))
