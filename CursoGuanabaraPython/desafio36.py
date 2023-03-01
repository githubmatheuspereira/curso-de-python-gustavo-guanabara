# MINHA SOLUÇÃO PARA O DESAFIO 36 PROPOSTO
"""
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, senão, o empréstimo será negado.
"""

valorDaCasa = float(input('Qual o valor da casa?\n'))
salario = float(input('Qual o valor do seu salário?\n'))
meses = int(input('Com quantos meses pretende pagar?\n'))

prestacao = valorDaCasa / meses
if prestacao > salario - (salario * 0.70):
    print('Desculpe, seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado.\nO valor da sua mensalidade será de R${:.2f} em {}x'.format(prestacao, meses))
