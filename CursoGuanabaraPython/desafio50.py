# MINHA SOLUÇÃO PARA O DESAFIO 50 PROPOSTO

soma = 0
for contador in range(0,6):
    valor = int(input('Escreva o {}º número: '.format(contador+1)))
    if valor % 2 == 0:
        soma += valor
print('O valor total da soma dos números pares é {}.'.format(soma))