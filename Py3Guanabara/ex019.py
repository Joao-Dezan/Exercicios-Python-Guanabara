from random import choice
a1 = input('Nome do Primeiro Aluno: ')
a2 = input('Nome do Segundo Aluno: ')
a3 = input('Nome do Terceiro Aluno: ')
a4 = input('Nome do Quarto Aluno: ')
alunos = [a1, a2, a3, a4]
print('O aluno(a) escolhido foi o(a){}'.format(choice(alunos)))
