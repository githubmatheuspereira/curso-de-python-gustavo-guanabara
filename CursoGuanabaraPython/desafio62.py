# MINHA SOLUÇÃO PARA O DESAFIO 62 PROPOSTO

termo = int(input('Qual é o primeiro termo?\n'))
razao = int(input('Qual é a razão?\n'))
contador = 0
contador2 = 1
denovo = 1
print('-'*10,'Resutado abaixo','-'*10)
while contador != 10:
    print(termo)
    termo += razao
    contador +=1
while denovo != 0:
    denovo = int(input('Quer ver mais quantos termos? [0] para sair do programa. '))
    if denovo == 0:
        print('Ok, até mais!')
    else:
        while contador2 != denovo + 1:
            print(termo)
            termo += razao
            contador2 +=1
    contador2 = 1
print('Desligando...')