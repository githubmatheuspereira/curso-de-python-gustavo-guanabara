"""

Listas python
parte 1

Reestabelecer um valor
lanche=['A','B','C','F']
lanche=[3]='D'
fica:
lanche=['A','B','C','D']

Adicionar um valor
lanche=['A','B','C','D']
lanche.append('F')
fica:
lanche=['A','B','C','D','F']

Adicionar um valor em qualquer lugar
lache.insert(0,'1')
fica:
lanche=['1','A','B','C','D','F']

Apagando um valor
del lanche[3] - elimina o valor 3
lanche.pop(3) - normalmente o método pop é para apagar o último elemento (sem parâmetro)
lanche.remove('C') - Deleta o valor pelo o conteúdo (indíce 3, conteúdo 'C')
Para não dar error:
    if 'C' in lanche:
        lanche.remove('C')

valores=[8,2,5,4,9,3,0]
valores.sort()
fica:
[0,2,3,4,5,8,9]
Caso queira o inverso:
valores.sort(reverse=True)

valores=[8,2,5,4,9,3,0]
len(valores)
fica:
7


"""
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
    num.remove(5)
else:
    print('Não achamos o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')
"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for posicao, valor in enumerate(valores):
    print(f'na posicão {posicao} encontrei o valor {valor}! ', end='')
"""
valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite o valor: ')))
for posicao, valor in enumerate(valores):
    print(f'na posicão {posicao} encontrei o valor {valor}! ', end='')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'\nlista A: {a}\nlista B: {b}') #Se tentar mudar valor de uma lista, mudará das duas.

