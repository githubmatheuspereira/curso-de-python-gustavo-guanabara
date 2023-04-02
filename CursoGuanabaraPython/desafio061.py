# MINHA SOLUÇÃO PARA O DESAFIO 61 PROPOSTO

termo = int(input('Qual é o primeiro termo?\n'))
razao = int(input('Qual é a razão?\n'))
contador = 1
print('-'*10,'Resutado abaixo','-'*10)

while contador <= 10:
    print(termo, end=' ')
    termo += razao
    contador +=1
print('FIM!')