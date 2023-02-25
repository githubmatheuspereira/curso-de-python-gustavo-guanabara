# MINHA SOLUÇÃO PARA O DESAFIO 34 PROPOSTO

salario = int(input('Quanto que você você ganha?\n'))
print('Você ganhou um aumento de 10%, seu novo salário é R${:.2f}'.format(salario * 1.10) if salario > 1250 else 'Você ganhou um aumento de 15%, seu novo salário é R${:.2f}'.format(salario * 1.15))