# MINHA SOLUÇÃO PARA O DESAFIO 64 PROPOSTO

numero = 0
contador = 0
total = 0
while numero != 999:
    numero = int(input('Dígite aqui: '))
    if numero == 999:
        numero = 999
    else:
        total += numero
        numero = 0
    contador += 1
print('Tivemos {} numeros digitados e o total deles é {}'.format(contador - 1, total))