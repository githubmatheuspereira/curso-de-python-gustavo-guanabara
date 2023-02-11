# MINHA SOLUÇÃO PARA O DESAFIO 11 PROPOSTO
altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
m2 = float(altura * largura)
qtdTinta = float(m2 / 2)
print('Você tem {:.2f}m2 para pintar\nVocê necessitará de {:.2f} lt(s) de tinta.'.format(m2, qtdTinta))