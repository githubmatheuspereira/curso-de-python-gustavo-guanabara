# MINHA SOLUÇÃO PARA O DESAFIO 75 PROPOSTO
contador = 1
valores = (int(input('Dígite o primeiro valor: ')),int(input('Dígite o segundo valor: ')),int(input('Dígite o terceiro valor: ')),int(input('Dígite o quarto valor: ')),)
print(f'Você digitou o seguintes números:\n{valores}')
valor9 = valores.count(9)
print(f'O valor 9 apareceu {valor9} vezes.')
if 3 in valores:
    valor3 = valores.index(3)
    print(f'Você digitou o número 3 na posição {valor3 + 1}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares foram: ')
for numero in valores:
    if numero % 2 == 0:
        print(numero, end=', ')
    