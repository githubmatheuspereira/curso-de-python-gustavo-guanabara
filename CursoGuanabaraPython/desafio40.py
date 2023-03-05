# MINHA SOLUÇÃO PARA O DESAFIO 40 PROPOSTO

nome = str(input('Qual seu nome?\n'))
nota1 = float(input('Qual sua primeira nota?'))
nota2 = float(input('Qual sua segunda nota?'))
media = (nota1 + nota2) / 2
if media < 5:
    print('{},\nSua média foi: {}\nVocê foi reprovado!'.format(nome, media))
elif media >= 5 and media <= 6.9:
    print('{},\nSua média foi: {}\nVocê está de recuperação!'.format(nome, media))
else:
    print('{},\nSua média foi: {}\nParabéns!\nVocê foi aprovado!'.format(nome, media))