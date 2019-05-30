cidade = str(input('Digite o nome da cidade: ')).strip()
nome = cidade.split()[0].upper()
print('A cidade começa com Santo? {}'.format('SANTO' in nome))
