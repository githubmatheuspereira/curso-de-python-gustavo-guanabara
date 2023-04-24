# MINHA SOLUÇÃO PARA O DESAFIO 65 PROPOSTO

numero = 0
total = 0
media = 0
maior = 0
menor = 0
continuar = ''
contador = 0

while continuar != 'N':
    numero = int(input('Dígite um número: '))
    continuar = ''
    total += numero
    if numero == 0 or numero > maior:
        maior = numero
    if menor == 0 or numero < menor:
        menor = numero
    while (continuar != 'S') and (continuar != 'N'):
        continuar = str(input('Quer continuar? [S] SIM [N] NÃO\n')).upper()
        if continuar != 'S' and continuar != 'N':
            print('Comando errado, tente novamente!')
print('O menor valor foi {}\nO maior valor foi {}\nA soma dos valores foi {}'.format(menor, maior, total))
        