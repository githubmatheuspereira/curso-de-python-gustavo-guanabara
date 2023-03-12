inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
        passo = 1
for contador in range(inicio, fim+1, passo):
    print(contador)
print('Fim!')