D
velocidadeCarro = int(input('Qual a velocidade do carro?\n'))
multa = float((velocidadeCarro - 80) * 7)
print('Passou dentro do permitido!' if velocidadeCarro <= 80 else 'Você foi multado!\nSua multa será de R${:.2f}!'.format(multa))
