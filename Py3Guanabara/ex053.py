nome = str(input('Digite o nome: ')).upper().replace(' ', '')
# inverso = nome[::-1]
inverso = ''
for letra in range(len(nome) - 1, -1, -1):
    inverso += nome[letra]
if nome == inverso:
    print('Essa frase é palindromo')
else:
    print('Essa frase não é palindromo')
