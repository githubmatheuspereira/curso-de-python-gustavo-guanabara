from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for contador in range(0,6):
    nascimento = int(input('Qual ano de nascimento da {}ª pessoa? '.format(contador + 1)))
    if (hoje - nascimento) >= 18:
        maior = maior + 1
    elif (hoje - nascimento) < 18:
        menor = menor + 1
print('{} pessoas são maior de idade.\n{} pessoas são menor de idade.'.format(maior, menor))