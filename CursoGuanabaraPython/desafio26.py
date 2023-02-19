frase = str(input('Escreva sua frase abaixo.\n'))
print('Seu texto foi:\n'.format(frase))
print('A letra "''A''" aparece {} vezes\nA letra "''A''" apareceu a 1ª vez na memória {}'.format(frase.count('a'), frase.find('a')))