# MINHA SOLUÇÃO PARA O DESAFIO 47 PROPOSTO

soma = 0
for contador in range(1,501):
    if contador % 3 == 0:
        if contador % 2 != 0:
            print(contador)
            soma += contador
print(soma)