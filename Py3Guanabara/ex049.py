n = int(input('A tabuada de qual número você deseja ver? '))
x = int(input('Por qual número multiplicado você deseja começar a tabuada: '))
y = int(input('E até qual número multiplicado você deseja terminar a tabuada? '))
print(12*'=')
for c in range(x, y+1):
    print('{} x {:2} = {}'.format(n, c, n*c))
print(12*'=')
