resposta = 'S'
while resposta == 'S':
    valor = float(input('Digite um valor: '))
    resposta = str(input('Quer continuar?\n[S] ou [N] ')).upper()
print('fim')

numero = 1
par = 0
impar = 0
while numero != 0:
    numero = int(input('Digite um número: '))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você dígitou {} números pares e {} números impares.'.format(par, impar))