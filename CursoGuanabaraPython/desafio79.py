# MINHA SOLUÇÃO PARA O DESAFIO 79 PROPOSTO

valores = []
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if (valor in valores) == True:
        print('Número já existe. Apagando...')
    else:
        valores.append(valor)
    continuar = str(input('Deseja continuar?\n[S] SIM [N] NÃO\n')).upper()
valores.sort()
print(valores)

"""
Exercício feito por Guanabara:

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, não irei adicionar!')
    r = str(input('Quer continuar? [S] SIM [N] NÃO\n'))
    if r in 'Nn':
        break
"""

