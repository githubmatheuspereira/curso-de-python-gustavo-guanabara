# MINHA SOLUÇÃO PARA O DESAFIO 28 PROPOSTO
import random
numeroSorteado = random.randint(1, 5)
numero = int(input('Qual numero que você acha que é? (1 à 3)\n'))
print('Parabéns, você acertou!' if numero == numeroSorteado else 'Você errou, tente novamente!')
print('O número correto é {}'.format(numeroSorteado))