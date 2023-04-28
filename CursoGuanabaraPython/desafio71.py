# MINHA SOLUÇÃO PARA O DESAFIO 71 PROPOSTO

cedula100 = 0
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0

print(':'*15, ' BANCO ', ':'*15)
valorDeSaque = int(input('Qual o valor desejado à sacar?\n'))
if valorDeSaque != 0:
    while valorDeSaque >= 100:
        valorDeSaque = valorDeSaque - 100
        cedula100 += 1
        print(valorDeSaque)
    while valorDeSaque >= 50:
        valorDeSaque = valorDeSaque -  50
        cedula50 += 1
    while valorDeSaque >= 20:
        valorDeSaque = valorDeSaque -  20
        cedula20 += 1
    while valorDeSaque >= 10:
        valorDeSaque = valorDeSaque -  10
        cedula10 += 1
    while valorDeSaque >= 1:
        valorDeSaque = valorDeSaque -  1
        cedula1 += 1
print(f'Daremos {cedula100} cédulas de R$ 100\nDaremos {cedula50} cédulas de R$ 50\nDaremos {cedula20} cédulas de R$ 20\nDaremos {cedula10} cédulas de R$ 10\nDaremos {cedula1} cédulas de R$ 1\n')