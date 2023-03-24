# MINHA SOLUÇÃO PARA O DESAFIO 59 PROPOSTO

numero = int(input('Qual será o número?\n'))
divisor = numero
multiplicacao = 1
contador = 1
while numero >= contador:
    if divisor != 1:
        print(divisor,end='x')
    else:
        print(divisor,end='=')
    multiplicacao *= contador
    contador += 1
    divisor -= 1
print(multiplicacao)
