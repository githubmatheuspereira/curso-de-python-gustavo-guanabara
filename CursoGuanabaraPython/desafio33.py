# MINHA SOLUÇÃO PARA O DESAFIO 33 PROPOSTO
numero1 = int(input('Escreva o 1º número: '))
numero2 = int(input('Escreva o 2º número: '))
numero3 = int(input('Escreva o 3º número: '))
#Maior
if numero1 > numero2:
    maior = numero1
if numero2 > numero3:
    maior = numero2
if numero3 > numero1:
    maior = numero3
#Menor
if numero1 < numero2:
    menor = numero1
if numero2 < numero3:
    menor = numero2
if numero3 < numero1:
    menor = numero3

print('O número {} é o maior e o número {} é o menor!'.format(maior, menor))