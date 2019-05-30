numero = int(input('Me diga um número: '))
if numero % 2 == 0:
    print('')
    print('\033[4;31m02468\033[m'*4)
    print('\033[0;34mEsse número é PAR!\033[m')
    print('\033[4;31m02468\033[m'*4)
else:
    print('')
    print('\033[4;34m13579\033[m'*4)
    print('\033[0;31mEsse número é ÍMPAR!\033[m')
    print('\033[4;34m13579\033[m'*4)
