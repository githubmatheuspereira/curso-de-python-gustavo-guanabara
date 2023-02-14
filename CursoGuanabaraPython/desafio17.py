from math import sqrt, trunc
catetoOposto = int(input('Qual o valor do cateto oposto? '))
catetoAdjacente = int(input('Qual o valor do cateto adjacente? '))
hipotenusa = int((catetoOposto**2 + catetoAdjacente**2))
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(catetoOposto, catetoAdjacente, trunc(sqrt(hipotenusa))))