# MINHA SOLUÇÃO PARA O DESAFIO 77 PROPOSTO

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro', 'Sucesso', 'Habilidades', 'Aprendizado')

for contador in palavras:
    print(f'Na palavra {contador.upper()} temos', end=' ')
    for vogal in contador:
        if vogal.upper() in 'AEIOU':
            print(vogal.upper(), end=' ')
    print('')