# MINHA SOLUÇÃO PARA O DESAFIO 58 PROPOSTO

from random import randint
numeroSorteado = randint(1,10)
numeroEscolhido = 0
chances = 0
while numeroEscolhido != numeroSorteado:
    numeroEscolhido = int(input('Qual número você acha que é?\n'))
    if numeroEscolhido != numeroSorteado:
        chances += 1
        print('Errado, tente novamente!')
    elif numeroEscolhido == numeroSorteado:
        chances += 1
        print('Você acertou o número é {}. Você precisou de {} chances.'.format(numeroSorteado, chances))
print('Volte sempre!')