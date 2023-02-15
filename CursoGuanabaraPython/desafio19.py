from random import choice
aluno1 = str(input('Escreva o nome do 1° aluno: '))
aluno2 = str(input('Escreva o nome do 2° aluno: '))
aluno3 = str(input('Escreva o nome do 3° aluno: '))
aluno4 = str(input('Escreva o nome do 4° aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(alunos)
print ('O aluno {} foi sorteado!'.format(sorteado))