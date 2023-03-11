# MINHA SOLUÇÃO PARA O DESAFIO 42 PROPOSTO

linha1 = float(input('Digite o comprimento da primeira reta: '))
linha2 = float(input('Digite o comprimento da segunda reta: '))
linha3 = float(input('Digite o comprimento da terceira reta: '))

if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha1 + linha2:
    print('Os valores acima podem formar um triângulo!')
    if linha1 == linha2 == linha3:
        print('Este é um triângulo equilátero, todos os lados são iguais!')
    elif linha1 == linha2 or linha2 == linha3 or linha3 == linha1:
        print('Este é um triângulo isósceles, dois lados são iguais!')
    elif linha1 != linha2 and linha1 != linha3 and linha2 != linha3:
        print('Este é um triângulo escaleno, todos os lados são diferentes!')
else:
    print('Os valores acima não podem formar um triângulo!')
