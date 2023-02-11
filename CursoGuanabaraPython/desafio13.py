# MINHA SOLUÇÃO PARA O DESAFIO 13 PROPOSTO
salario = float(input('Qual seu salário? '))
aumento = (1.00 + 0.15) #SENDO 100% = 1.00
novoSalario = float(salario * aumento)
print ('Seu salário atual é: {:.2f}\nSeu novo salário é: {:.2f}'.format(salario, novoSalario))