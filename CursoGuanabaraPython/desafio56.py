# MINHA SOLUÇÃO PARA O DESAFIO 56 PROPOSTO

nome = ''
idade = 0
sexo = ''
media = 0
idadeMaisVelho = 0
nomeMaisVelho = ''
mulheresJovens = 0
for contador in range(0,4):
    nome = str(input('Qual é o nome da {}a pessoa? '.format(contador + 1))).strip()
    idade = int(input('Qual é a idade da {}a pessoa? '.format(contador + 1)))
    sexo = int(input('Qual é o sexo da {}a pessoa? sendo:\n[1] Homem\n[2] Mulher\n[3] Outros\n'.format(contador + 1)))
    media += idade
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo == 2 and idade < 20:
        mulheresJovens += 1
print('A média de idade é: {}\nO homem mais velho é {} e tem {} anos\nE temos {} mulheres com menos de 20 anos.'.format((media / 4),nomeMaisVelho, idadeMaisVelho, mulheresJovens))

