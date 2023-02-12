# MINHA SOLUÇÃO PARA O DESAFIO 12 PROPOSTO
precoNormal = float(input('Qual é o valor normal do produto?'))
desconto = (1.00 - 0.05) #SENDO 100% = 1.00
precoComDesconto = float(precoNormal * desconto)
print ('Preço normal do produto: R${:.2f}\nPreço com desconto de 5%: R${:.2f}'.format(precoNormal, precoComDesconto))

# OU PODEMOS FAZER DA SEGUINTE FORMA:
#porcentagem = 5
#desconto = precoNormal - (precoNormal * porcentagem / 100)
