#AULA 12 - MUNDO 02 (MÓDULO 02 DE PYTHON 3)
#Condições Aninhadas
nome = str(input('Qual é o seu nome?\n')).strip()
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Lucas' or nome == 'Igor' or nome == 'Rafael':
    print('Seu nome é bem popular!')
else:
    print('Prazer em te conhecer.')
print('Tenha um bom dia, {}!'.format(nome))