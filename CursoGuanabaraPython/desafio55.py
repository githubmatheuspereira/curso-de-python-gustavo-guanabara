maior = 0
menor = 0
for contador in range(0,5):
    peso = float(input('Peso da {}ª pessoa: '.format(contador+1)))
    if contador == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg.'.format(maior))
print('O menor peso foi de {}Kg.'.format(menor))
