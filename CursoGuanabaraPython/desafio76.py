# MINHA SOLUÇÃO PARA O DESAFIO 76 PROPOSTO
print(':'*50,f'\n{"LISTA DE COMPRAS":.^50}')
print(':'*50)
lista = ('Arroz', 21.30, 'Feijão', 9.40, 'Óleo', 8.90, 'Sal', 4.75, 'Açúcar', 3.80, 'Café', 19.70, 'Extrato de tomate', 4.99, 'Macarrão', 3.25, 'Atum', 7.90, 'Milho/Ervilha', 2.90, 'Farinha de trigo', 6.40, 'Manteiga', 12.65)
for produto in range(0, len(lista), 2):
    print(f'{lista[produto]:_<40}',f'R$ {lista[produto+1]:>5.2f}')
print('_'*50,f'\n{"Todos direitos reservados":_^50}\n')

"""
Exercício feito por Guanabara:
listagem = ('Arroz', 21.30, 
            'Feijão', 9.40, 
            'Óleo', 8.90, 
            'Sal', 4.75, 
            'Açúcar', 3.80, 
            'Café', 19.70, 
            'Extrato de tomate', 4.99, 
            'Macarrão', 3.25, 
            'Atum', 7.90, 
            'Milho/Ervilha', 2.90, 
            'Farinha de trigo', 6.40, 
            'Manteiga', 12.65)
print('-'*40)
print('{"Listagem de preços":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
"""