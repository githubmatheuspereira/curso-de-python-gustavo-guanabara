# MINHA SOLUÇÃO PARA O DESAFIO 45 PROPOSTO
from random import randint
from time import sleep
nome = str(input('Bem vindo ao Jokenpô!\nMeu nome é Kenpô, qual é o seu nome?\n')).strip()
player1 = int(input('Prazer, {}!\nEscolha entre pedra, papel e tesoura conforme indicado abaixo:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n'.format(nome)))
player2 = randint(1,3)
#CONDIÇÃO JOGADOR
if player1 == 1:
    print('{} jogou pedra.'.format(nome))
elif player1 == 2:
    print('{} jogou papel.'.format(nome))
elif player1 == 3:
    print('{} jogou tesoura.'.format(nome))
else:
    print('Opção inválida. Siga as regras!')
#CONDIÇÃO COMPUTADOR
if player2 == 1:
    print('Kenpô jogou pedra.')
elif player2 == 2:
    print('Kenpô jogou papel.')
elif player2 == 3:
    print('Kenpô jogou tesoura.')
else:
    print('Opção inválida. Siga as regras!')

print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ...')
sleep(0.5)

if player1 == player2:
    print('EMPATE!')
elif player1 == 1 and player2 == 2:
    print('Kenpô GANHOU!')
elif player1 == 1 and player2 == 3:
    print('{} GANHOU!'.format(nome))
elif player2 == 1 and player1 == 2:
    print('{} GANHOU!'.format(nome))
elif player2 == 1 and player1 == 3:
    print('Kenpô GANHOU!')
