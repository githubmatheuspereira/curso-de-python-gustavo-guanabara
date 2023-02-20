numero = str(input('Escreva um número de 0 à 9999: '))
print('O número foi {}.'.format(numero))
print('Unidades: {}\nDezenas: {}\nCentenas {}\nMilhas: {}'.format(numero[3], numero[2], numero[1], numero[0]))
#NESTE EXERCÍCIO FUNCIONA SOMENTE COM OS 4 DÍGITOS DIGITADOS.

"""
RESOLUÇÃO GUSTAVO GUANABARA
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
"""