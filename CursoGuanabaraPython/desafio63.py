# MINHA SOLUÇÃO PARA O DESAFIO 63 PROPOSTO

contador = 0
fibonacci = 0
numeroAnterior = 1
numeroAtual = 1
quantidade = int(input('Quantos números você gostaria da sequência de fibonacci? '))
if quantidade == 1:
    print('1')
elif quantidade == 2:
    print('1\n1')
else:
    print('1\n1')
    while contador != quantidade:
        contador += 1
        fibonacci = numeroAtual + numeroAnterior
        numeroAnterior = numeroAtual
        numeroAtual = fibonacci
        print(fibonacci)
