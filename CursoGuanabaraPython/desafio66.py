# MINHA SOLUÇÃO PARA O DESAFIO 66 PROPOSTO

contador = 0
soma = 0
print('Bem vindo ao contador de número. Dígite 0 para sair/parar!')
while True:
    numero = int(input('Digite um valor: '))
    if numero == 0:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} valores foi {soma}')