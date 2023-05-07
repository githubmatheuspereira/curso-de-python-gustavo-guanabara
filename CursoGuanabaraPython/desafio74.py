# MINHA SOLUÇÃO PARA O DESAFIO 74 PROPOSTO
from random import randint
numeroSorteado = (randint(1,10,), randint(1,10,), randint(1,10,), randint(1,10,), randint(1,10,))
print('Numeros sorteados foram:')
for numero in numeroSorteado:
    print(f'{numero}', end=' ')
numeroSorteadoOrdenado = sorted(numeroSorteado)
print(f'\nO maior número foi {numeroSorteadoOrdenado[-1]}\nO menor número foi {numeroSorteadoOrdenado[0]}')