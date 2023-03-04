# MINHA SOLUÇÃO PARA O DESAFIO 37 PROPOSTO

numero1 = int(input('Escreva o primeiro valor: '))
numero2 = int(input('Escreva o segundo valor: '))

if numero1 > numero2:
    print('O primeiro valor ({}) é maior que o segundo ({})!'.format(numero1, numero2))
elif numero1 < numero2:
    print('O segundo valor ({}) é maior que o primeiro ({})!'.format(numero2, numero1))
elif numero1 == numero2:
    print('Não existe valor maior ou menor, os dois valores são iguais.')
else:
    print('ERROR - FALHA NO SISTEMA. TENTE NOVAMENTE!')