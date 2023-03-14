# MINHA SOLUÇÃO PARA O DESAFIO 52 PROPOSTO

numero = int(input('Qual número você gostaria de saber se é primo?: '))
total = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(contador), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')