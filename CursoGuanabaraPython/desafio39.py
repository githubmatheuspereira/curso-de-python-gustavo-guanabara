# MINHA SOLUÇÃO PARA O DESAFIO 39 PROPOSTO

nome = str(input('Qual é o seu nome?\n'))
idade = int(input('Qual é a sua idade?\n'))
if idade <= 17:
    print('Prazer, {}!\nVocê ainda não está com idade para se alista. Volte com 18 anos ou mais.'.format(nome))
elif idade > 17 and idade < 19:
     print('Prazer, {}!\nJá é hora de se alistar. Não perca o tempo!'.format(nome))
else:
     print('Prazer, {}!\nJá passsou da hora de você se alistar. Vá até uma base do exército o quanto antes.'.format(nome))

"""
Solução Guanabara

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual))

if idade == 18:
     print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
     saldo = 18 - idade
     print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento.'.format(saldo))
     ano = atual + saldo
     print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
     saldo = idade - 18
     print('Você já deveria ter se alistado há {} anos.'.format(saldo))
     ano = atual - saldo
     print('Seu alistamento foi em {}.'.format(ano))
"""