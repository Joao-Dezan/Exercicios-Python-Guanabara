frase = str(input('Digite uma frase qualquer: '))
letra = input('Qual letra você quer encontrar? ')
letra1 = letra.upper()
a = frase.upper().count(letra1)
print('Essa frase tem {} letra(s) "{}"'.format(a, letra))
print('A primeira letra "{}" está localizada na {}ª posição'.format(letra, frase.upper().find(letra1) + 1))
print('A última letra "{}" está localizada na {}ª posição'.format(letra, frase.upper().rfind(letra1) + 1))
