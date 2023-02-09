entrada = input('Digite algo e vamos saber o seu tipo primitivo: ')
print('Você dígitou \'{}\' '.format(entrada))                    
print('\'{}\' é numérico? -'.format(entrada), entrada.isnumeric())
print('\'{}\' é alpha? -'.format(entrada), entrada.isalpha())
print('\'{}\' é alphanumérico? -'.format(entrada), entrada.isalnum())
print('\'{}\' é printável? -'.format(entrada), entrada.isprintable())
print('\'{}\' é decímal? -'.format(entrada), entrada.isdecimal())
\