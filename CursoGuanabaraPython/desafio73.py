# MINHA SOLUÇÃO PARA O DESAFIO 73 PROPOSTO
classificacao = ('Botafogo','Fortaleza','Palmeiras','Internacional','Fluminense',
                 'Cruzeiro','Gremio','São Paulo','Vasco da Gama','Atlético Mineiro',
                 'Santos','Bragantino','Flamengo','Atlético Paranaense','Bahia','Goiás',
                 'Corinthians','Cuiabá','Coritiba','América Mineiro',)
#COMO CHAPECÓ NÃO ESTÁ NA SERIE A, DECIDI COLOCAR O INTERNACIONAL
index = classificacao.index('Internacional')
print(f'Os 5 primeiros colocados do brasileirão são:\n{classificacao[0:5]}')
print(f'Os 4 ultimos colocados do brasileirão são:\n{classificacao[16:20]}')
print(f'Nomes dos times em ordem alfabética:\n{sorted(classificacao)}')
print(f'O Internacional está na {index + 1}ª posição.')

"""
times = ('Botafogo','Fortaleza','Palmeiras','Internacional','Fluminense',
                 'Cruzeiro','Gremio','São Paulo','Vasco da Gama','Atlético Mineiro',
                 'Santos','Bragantino','Flamengo','Atlético Paranaense','Bahia','Goiás',
                 'Corinthians','Cuiabá','Coritiba','América Mineiro',)
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O internacional está na {times.index("Internacional") + 1} posição')
"""