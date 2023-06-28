# MINHA SOLUÇÃO PARA O DESAFIO 80 PROPOSTO
valores = list()
for contador in range(0,5):
    valor = int(input('Digite um valor: '))
    if contador == 0 or valor > valores[len(valores)-1]:
        valores.append(valor)
        print('Adicionado na ultima posição')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1
print(valores)