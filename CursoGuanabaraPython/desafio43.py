# MINHA SOLUÇÃO PARA O DESAFIO 43 PROPOSTO

nome = str(input('Qual seu nome?\n'))
peso = float(input('{}, qual seu peso?\n'.format(nome)))
altura = float(input('{}, agora me informa sua altura.\n'.format(nome)))
imc = peso / (altura**2)
if imc > 40:
    print('{},\nSeu IMC é {:.1f}, você está com obesidade mórbida!'.format(nome, imc))
elif imc > 30:
    print('{},\nSeu IMC é {:.1f}, você está com obesidade!'.format(nome, imc))
elif imc > 25:
    print('{},\nSeu IMC é {:.1f}, você está com sobrepeso!'.format(nome, imc))
elif imc >= 18.5:
    print('{},\nSeu IMC é {:.1f}, você está no peso ideal!'.format(nome, imc))
elif imc < 18.5:
    print('{},\nSeu IMC é {:.1f}, você está abaixo do peso!'.format(nome, imc))