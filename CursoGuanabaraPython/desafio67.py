# MINHA SOLUÇÃO PARA O DESAFIO 67 PROPOSTO

numero1 = 1
numero2 = 1

print('-'*4,'TABUADA','-'*4)
while True:
    valor = int(input('Qual tabuada você deseja ver? '))
    if valor < 0:
        print('Ok, encerrando a tabuada!')
        break
    while numero1 <= 10:
        total = numero1 * valor
        print(f'{numero1} x {valor} = {total}')
        numero1 += 1
    print('\n')
    numero1 = 1