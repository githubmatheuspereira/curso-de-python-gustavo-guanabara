numeros = list()
while True:
    valor = int(input('Digite o valor: '))
    numeros.append(valor)
    continuar = str(input('Deseja continuar? [S] Sim [N] Não\n'))
    if continuar in 'Nn':
        break
print(numeros)  