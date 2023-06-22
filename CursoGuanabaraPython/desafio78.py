# MINHA SOLUÇÃO PARA O DESAFIO 77 PROPOSTO

valores = []
indice = 0
for valor in range(0,5):
    indice += 1
    valores.append(int(input('Digite o {}º valor: '.format(indice))))
menorOuMaior = valores[:]
print(f'Você digitou os valores: {valores}')
valores.sort()
print(f'O maior valor digitado foi: {valores[-1]}  na posição {menorOuMaior.index(valores[-1])+1}')
print(f'O menor valor digitado foi: {valores[0]} na posição {menorOuMaior.index(valores[0])+1}')
