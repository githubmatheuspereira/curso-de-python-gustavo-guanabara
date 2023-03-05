# MINHA SOLUÇÃO PARA O DESAFIO 43 PROPOSTO

nomeProduto = str(input('Qual o nome do produto?\n'))
valor = float(input('Qual o valor do produto?\n'))
formaDePagamento = int(input('Qual será a forma de pagamento? Sendo:\n[1] Pagamento à vista dinheiro/cheque com 10% de desconto\n[2] Pagamento à vista no cartão de débito/crédito com 5% de desconto\n[3] Pagamento em até 2x no cartão sem juros\n[4] Pagamento 3x ou mais com 20% de juros\n'))
if formaDePagamento == 1:
    valor = valor * 0.90
    print('O produto \'{}\' ficará com 10% de desconto, sendo valor total de R${:.2f}\n'.format(nomeProduto, valor))
elif formaDePagamento == 2:
    valor = valor * 0.95
    valorTotal = valor
    print('O produto \'{}\' ficará com 5% de desconto, sendo valor total de R${:.2f}\n'.format(nomeProduto, valor))
elif formaDePagamento == 3:
    valorTotal = valor
    valor = valor / 2
    print('O produto \'{}\' ficará em 2 vezes de R${:.2f}\n'.format(nomeProduto, valor),30*' ','Valor total será de: {}'.format(valorTotal))
elif formaDePagamento == 4:
    quantidadeDeParcelamento = int(input('Quantas vezes você prefere?\n'))
    valorTotal = valor * 1.20
    valor = (valor*1.20) / quantidadeDeParcelamento
    print('O produto \'{}\' ficará em {} vezes de R${:.2f} incluído os 20% de juntos\n'.format(nomeProduto, quantidadeDeParcelamento, valor),30*' ','Valor total será de: {}'.format(valorTotal))
else:
    print('Opção incorreta!\nTente novamente seguindo as instruções!')
