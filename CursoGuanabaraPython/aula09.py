#Aula09 - Manipulando texto
'''
Criado como texto para ajudar a relembrar operações quando tiver dificuldades.

frase = ('Curso em Vídeo Python')

=>FATIAMENTO
-Frase[9]                -> V (mostra letra alocada na memória 9.)
-frase[9:13]             -> Víde (mostra 'texto' alocado na memória de 9 à 12. Memória 13 não conta.)
-frase[9:21:2]           -> VDOPTO (mostra letras alocada em memória de 9 à 21 pulando de 2 em 2.)
-frase[:5]               -> Curso (mostra 'texto' da memória 0 à 5.)
-frase[15:]              -> Python (mostra 'texto' da memória 15 até o fim da string.)
-frase[9::3]             -> VEPH (mostra 'texto' da memória 9 até o fim da string pulando de 3 em 3.)

=>ANÁLISE
-len(frase)               -> 21 (mostra a quantidade de caracteres.)
-frase.cont("o")          -> 3 (mostra a quantidade de "o".)
-frase.cont("o", 0, 13)   -> 1 (mostra a quantidade de "o" de memória 0 à 13.)
-frase.find("deo")        -> 11 (mostra a partir de qual memória ele encontrou a string "deo".)
-frase.find("android")    -> -1 (como não há string "android", o programa retornará "-1".)
-"curso" in frase         -> True (Retorna True(se tiver string no texto) ou False (se não tiver string no texto).)

=>TRANSFORMAÇÃO
-frase.replace('Python','Android') -> Curso em Vídeo Android (troca a palavra python por android.)
-frase.upper()                     -> (todas as letras ficaram em maiúscula)
frase.lower()                      -> (todas as letras ficaram em minúscula)
frase.captalize()                  -> (1ª letra ficará em maiúscula)
frase.title()                      -> (1ª letra da palavra ficará em maiúscula)
frase.strip()                      -> (remove os espaços inúteis)
frase.rstrip()                     -> (remove somente os últimos espaços)
frase.lstrip()                     -> (remoce somente os primeiros espaços)

=>DIVISÃO
frase.split()                      -> (divide as palavras (em "memória" diferente) da frase)

=>JUNÇÃO
'-'.join(frase)                    -> (coloca '-' em todos os espaços)
'''
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])