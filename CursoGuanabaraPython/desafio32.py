# MINHA SOLUÇÃO PARA O DESAFIO 30 PROPOSTO

#ADICIONADO BIBLIOTECA DATETIME E INCLUÍDO 'and ano % 100 != 0 or ano % 400 == 0' APÓS ASSISTIR VIDEO AULA GUANABARA
from datetime import date
ano = int(input('Digíte um ano:\n'))
if ano == 0:
    ano = date.today().year
print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'O ano {} não é bissexto'.format(ano))