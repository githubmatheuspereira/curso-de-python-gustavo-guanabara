nome = str(input('Qual é o seu nome completo?\n')).strip()
nomeSemEspacos = len(nome) - nome.count(' ')
primeiroNome = nome.split()
print('Seu nome com todas às letras maiúisculas e minúsculas:\n{}\n{}'.format(nome.upper(), nome.lower()))
print('Seu nome tem {} letras'.format(nomeSemEspacos))
print('Seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))


