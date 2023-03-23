# MINHA SOLUÇÃO PARA O DESAFIO 56 PROPOSTO

sexo = ''
while sexo != 'M' and sexo != 'F' and sexo != 'O':
    sexo = str(input('Qual seu sexo?\n[M] Masculino\n[F] Feminino\n[O] Outros\n')).upper()
    if sexo == 'M':
        print('Ok, você escolheu o sexo masculino.')
    elif sexo == 'F':
        print('Ok, você escolheu o sexo feminino.')
    elif sexo == 'O':
        print('Ok, você não se indentifica como masculino ou feminino.')
print('Muito obrigado!')