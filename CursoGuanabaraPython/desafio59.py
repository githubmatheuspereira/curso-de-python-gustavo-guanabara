# MINHA SOLUÇÃO PARA O DESAFIO 59 PROPOSTO
novosNumeros = 4

print('_'*10,'Mini Calculadora','_'*10)
while novosNumeros == 4:
    numero1 = int(input('Escreva o primeiro valor: '))
    numero2 = int(input('Escreva o segundo valor: '))
    novosNumeros = 0
    print('_'*9,'O que você deseja?','_'*9)
    funcao = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n'))
    if funcao == 1:
        resultado = ('A soma de {} mais {} é {}.'.format(numero1, numero2, (numero1 + numero2)))
    elif funcao == 2:
        resultado = ('A mutiplicação de {} vezes {} é {}.'.format(numero1, numero2, (numero1 * numero2)))
    elif funcao == 3:
        if numero1 > numero2:
            resultado = ('O número {} é maior que o número {}.'.format(numero1, numero2))
        elif numero1 < numero2:
            resultado = ('O número {} é maior que o número {}.'.format(numero2, numero1))
        elif numero1 == numero2:
            resultado = ('Os números são iguais.')
    elif funcao == 4:
        novosNumeros = 4
    elif funcao == 5:
        print('Ok, estarei a disposição quando precisar!\nTchauuuu!')
    #   AQUI FAZ A FUNÇÃO SE QUER REPETIR O NÚMERO
    if funcao == 1 or funcao == 2 or funcao == 3:
        print(resultado)
        novosNumeros = str(input('Deseja novo resultado?\n[S] SIM\n[N] NÃO\n')).upper()
        if novosNumeros != 'S':
            print('Obrigado. Até mais!')
        else:
            novosNumeros = 4
    