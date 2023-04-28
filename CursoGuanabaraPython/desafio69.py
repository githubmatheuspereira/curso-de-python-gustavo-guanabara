# MINHA SOLUÇÃO PARA O DESAFIO 69 PROPOSTO

continuar = 'S'
genero = ''
feminino = 0
masculino = 0
menor = 0
maior = 0
totalPessoas = 0

while continuar == 'S':
    idade = int(input('Qual à idade: '))
    while genero != 'F' and genero != 'M':
        genero = str(input('Qual o sexo:\n[F] Feminino\n[M] Masculino\n')).upper()
        if genero != 'F' and genero != 'M':
            print('Siga às instruções e tente novamente!')
    if genero == 'F':
        feminino += 1
    if genero == 'M':
        masculino += 1
    if idade <= 18:
        menor += 1
    else:
        maior += 1 
    totalPessoas += 1
    genero = ''
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = (str(input('Deseja continuar?\n[S] Sim\n[N] Não\n'))).upper()
print(f'Temos total de {totalPessoas} pessoas cadastradas.\n{feminino} delas é do sexo feminino.\n{masculino} delas é do sexo masculino.\n{menor} das pessoas cadastradas são menores de idade!')