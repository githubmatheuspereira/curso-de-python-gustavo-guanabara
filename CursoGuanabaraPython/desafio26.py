frase = str(input('Escreva sua frase abaixo.\n')).strip().upper()
print('Seu texto foi:\n {}'.format(frase))
print('A letra "''A''" aparece {} vezes\nA letra "''A''" apareceu a 1ª vez na memória {}\nA última vez na memória {}'.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
