nome = str(input('Qual é seu nome completo? ')).strip()
nomeCortado = nome.split()
print('Seu primeiro e último nome é: {} {}'.format(nomeCortado[0], nomeCortado[len(nomeCortado)-1]))