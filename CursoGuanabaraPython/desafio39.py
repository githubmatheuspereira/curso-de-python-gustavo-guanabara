# MINHA SOLUÇÃO PARA O DESAFIO 39 PROPOSTO

nome = str(input('Qual é o seu nome?\n'))
idade = int(input('Qual é a sua idade?\n'))
if idade <= 17:
    print('Prazer, {}!\nVocê ainda não está com idade para se alista. Volte com 18 anos ou mais.'.format(nome))
elif idade > 17 and idade < 19:
     print('Prazer, {}!\nJá é hora de se alistar. Não perca o tempo!'.format(nome))
else:
     print('Prazer, {}!\nJá passsou da hora de você se alistar. Vá até uma base do exército o quanto antes.'.format(nome))