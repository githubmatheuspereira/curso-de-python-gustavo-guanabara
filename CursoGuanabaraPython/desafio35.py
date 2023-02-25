# MINHA SOLUÇÃO PARA O DESAFIO 35 PROPOSTO

linha1 = float(input('Digite o comprimento da primeira reta: '))
linha2 = float(input('Digite o comprimento da segunda reta: '))
linha3 = float(input('Digite o comprimento da terceira reta: '))

if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha1 + linha2:
    print('Os valores acima podem formar um triângulo!')
else:
    print('Os valores acima não podem formar um triângulo!')