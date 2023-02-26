# MINHA SOLUÇÃO PARA O DESAFIO 28 PROPOSTO
import random
from time import sleep
numeroSorteado = random.randint(1, 5)
numero = int(input('Qual numero que você acha que é? (1 à 5)\n'))
#Adicionado função sleep após assistir resolução prof. Guanabara
print('VERIFICANDO...')
sleep(1)
print('Parabéns, você acertou!' if numero == numeroSorteado else 'Você errou, tente novamente!')
print('O número correto é {}'.format(numeroSorteado))