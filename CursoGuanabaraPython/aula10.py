'''
nome = str(input('Olá, qual é o seu nome?\n'))
if nome == 'Matheus':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))
'''
numero1 = float(input('Digite sua primeira nota:\n'))
numero2 = float(input('Digite sua segunda nota:\n'))
media = (numero1 + numero2) / 2
print('A sua média foi de {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim, estude mais!')

'''
print('Sua média foi boa! Parabéns!' if media >= 6.0 else 'Sua média foi ruim, estude mais!')
'''