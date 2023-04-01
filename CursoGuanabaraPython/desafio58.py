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

#SOLUÇÃO GUANABARA
"""

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')
acertor = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))

"""