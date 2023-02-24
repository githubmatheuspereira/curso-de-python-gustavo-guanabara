# MINHA SOLUÇÃO PARA O DESAFIO 31 PROPOSTO
quantidadeKm = int(input('Quantos quilômetros será?\n'))
print('O preço da passagem será R${:.2f}'.format(quantidadeKm*0.50) if quantidadeKm <= 200 else 'O preço da passagem será R${:.2f}'.format(quantidadeKm*0.45))