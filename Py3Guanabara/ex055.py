pesos = []
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    pesos.append(peso)
print('O maior peso foi {} Kg e o menor foi {} Kg.'.format(max(pesos), min(pesos)))
