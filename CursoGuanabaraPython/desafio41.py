# MINHA SOLUÇÃO PARA O DESAFIO 41 PROPOSTO

nome = str(input('Qual seu nome?\n'))
idade = int(input('Qual sua idade?\n'))
if idade <= 9:
    print('{},\nDe acordo com sua idade({} anos), você é considerado um atleta MIRIM!'.format(nome, idade))
elif idade <= 14:
    print('{},\nDe acordo com sua idade({} anos), você é considerado um atleta INFANTIL!'.format(nome, idade))
elif idade < 19:
    print('{},\nDe acordo com sua idade({} anos), você é considerado um atleta JUNIOR!'.format(nome, idade))
elif idade <= 20:
    print('{},\nDe acordo com sua idade({} anos), você é considerado um atleta SÊNIOR!'.format(nome, idade))
else:
    print('{},\nDe acordo com sua idade({} anos), você é considerado um atleta MASTER!'.format(nome, idade))