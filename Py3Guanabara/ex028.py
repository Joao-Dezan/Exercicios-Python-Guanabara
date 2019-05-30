from random import randint
from time import sleep
print('\033[0;36m-=-\033[m'*19)
print('\033[0;35mVou pensar em um número entre 0 e 10. Tente advinhar...\033[m')
print('\033[0;36m-=-\033[m'*19)

n = int(input('\033[0;32mEm qual número eu pensei? \033[m'))
nr = randint(0, 10)
print('\033[0;33m\nPROCESSANDO...\n\033[m')
sleep(2)

if n == nr:
    print('\033[0;34mParabéns, você acertou! Eu pensei no número {}!\033[m'.format(nr))
else:
    print('\033[0;31mGANHEI! Eu pensei no número {} e não no {}!\033[m'.format(nr, n))
print('\n\033[0;31m-FIM-\033[m')
