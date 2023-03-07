# MINHA SOLUÇÃO PARA O DESAFIO 37 PROPOSTO

numero = int(input('Qual número inteiro você quer transformar?\n'))

conversao = str(input('Para qual conversão você gostaria?\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n'))

if conversao == '1':
    numeroConvertido = bin(numero)
    print('O número {} em binário é {}'.format(numero, numeroConvertido[2:]))
elif conversao == '2':
    numeroConvertido = oct(numero)
    print('O número {} em octal é {}'.format(numero, numeroConvertido[2:]))
elif conversao == '3':
    numeroConvertido = hex(numero)
    print('O número {} em hexadecimal é {}'.format(numero, numeroConvertido[2:]))
else:
    print('ERROR - OPÇÃO NÃO ENCONTRADA!')