# MINHA SOLUÇÃO PARA O DESAFIO 72 PROPOSTO
numeroExtenso = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZNOVE','VINTE',)
numero = int(input('Digite um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    print('='*36)
    print('=== APENAS O NÚMERO ENTRE 0 E 20 ===')
    print('='*36)
    numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeroExtenso[numero]}')