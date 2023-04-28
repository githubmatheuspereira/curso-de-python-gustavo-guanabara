# MINHA SOLUÇÃO PARA O DESAFIO 70 PROPOSTO
continuar = 'S'
totalGasto = 0
maisDeMil = 0
maisBaratoValor = 0
maisBaratoNome = ''
print('+'*10,'SUPERMERCADO TAKARO','+'*10)

while continuar == 'S':
    nome = str(input('Qual o nome do produto?\n'))
    preco = float(input('Qual o valor do produto?\n'))
    totalGasto += preco
    if preco > 1000:
        maisDeMil += 1
    if maisBaratoValor == 0:
        maisBaratoValor = preco
    elif preco < maisBaratoValor:
        maisBaratoValor = preco
        maisBaratoNome = nome
    continuar = str(input('Deseja continuar?\n[S] SIM / [N] Não\n')).upper()
print('+'*10,' COMPRA FINALIZADA ','+'*10)
print(f'O total gasto é {totalGasto:.2f}\nTemos {maisDeMil} que custa mais de R$ 1.000,00\nO nome do produto mais barato é {maisBaratoNome}')