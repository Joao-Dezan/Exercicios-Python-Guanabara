sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dado inválido. Por favor informe o sexo [F/M]: ')).upper().strip()[0]
print('Sexo {} coletado com sucesso!'.format('Masculino' if sexo == 'M' else 'Feminino'))
