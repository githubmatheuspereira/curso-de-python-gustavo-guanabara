# MINHA SOLUÇÃO PARA O DESAFIO 68 PROPOSTO
from time import sleep
from random import randint
jogoGanho = 0
ganhouOuPerdeu = ''

print(':'*10,'PAR OU IMPAR',':'*10)
while ganhouOuPerdeu != 'perdeu':
    contador = 1
    numeroApostado = int(input('Qual número você escolhe: '))
    jogador = int(input('Você quer IMPAR(1) ou PAR(2) '))
    print('Ok, vamos lá!')
    while contador <= 3:
        print(contador)
        contador += 1
        sleep(1)
    numeroSorteado = randint(1, 10)
    soma = numeroSorteado + numeroApostado
    if soma % 2 == 0:
        valor = 'par'
        if jogador == 2:
            ganhouOuPerdeu = 'ganhou'
            jogoGanho += 1
        elif jogador != 2:
            ganhouOuPerdeu = 'perdeu'
    elif soma % 2 != 0:
        valor = 'impar'
        if jogador == 1:
            ganhouOuPerdeu = 'ganhou'
            jogoGanho += 1
        elif jogador != 1:
            ganhouOuPerdeu = 'perdeu'
    print(f'Seu número escolhido foi: {numeroApostado}')
    print(f'O número escolhido foi {numeroSorteado}.\nNo entanto, {numeroSorteado} + {numeroApostado} é igual à {soma}.\nEle é {valor}.')
    sleep(1)
    print(f'Você {ganhouOuPerdeu}!')
print(f'Total de jogo ganho: {jogoGanho} vezes.')

