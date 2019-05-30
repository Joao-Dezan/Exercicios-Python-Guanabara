from random import sample, shuffle
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
alunos = [a1, a2, a3, a4]
'''shuffle(alunos)'''
print('A ordem de apresentação será\n{}'.format(sample(alunos, k=4)))
