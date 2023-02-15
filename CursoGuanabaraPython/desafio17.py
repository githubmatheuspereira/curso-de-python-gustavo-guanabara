from math import sqrt, hypot

catetoOposto = float(input('Qual o valor do cateto oposto? '))
catetoAdjacente = float(input('Qual o valor do cateto adjacente? '))
'''
hipotenusa = ((catetoOposto**2 + catetoAdjacente**2))
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.2f}'.format(catetoOposto, catetoAdjacente, sqrt(hipotenusa)))
'''
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))