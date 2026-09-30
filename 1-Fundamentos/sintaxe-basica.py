# AULA 1 -- esta é um comentario dentro da linguagem de programação Python

''' este é um comentario
 de bloco. Seja lá 
 o que eu escrever aqui, não será exibido na tela.
 Desde que, na estrutura do código, exista uma instrução lógica qualquer!
 Caso não exista o python exibe este texto como uma string raw (bruta)
'''

# para quem estiver usando o VSCode 
# abrir o terminal do VSCode e escrever:
# comando de execução: python sintaxe-basica.py - pressione Enter 

# esta, abaixo, é a função print() - nativa do python - que tem o objetivo de "imprimir" 
# qualquer coisa que queremos exibir em tela.
print('Ola Mundo Python! Chegamos!')

print('================= ESTUDO DE VARIAVEIS ==================')

# passo 1: vamos definir duas variaveis - e vamos chama-las de a e b

a = 3 # declaramos uma var com o nome (a) e ATRIBUIMOS à ela o valor 3; para que pudesse ocorrer esta atribuição de valor, fizemos o uso do operador = (igual) (operador de atribuição)

b = 2 # declaramos uma var com o nome (B) e ATRIBUIMOS à ela o valor 2; para que pudesse ocorrer esta atribuição de valor, fizemos o uso do operador = (igual) (operador de atribuição)

print('Valor da variavel a: ', a) # nesta instrução estamos fazendo o seguinte: "imprimindo/exibindo", na tela, um texto e o valor atribuido a var (a) - fazendo referencia a variavel.

print('Valor da variavel b: ', b) # portanto, estamos "ACESSANDO"  as variaveis dentro da função print()

print()

c = a + b # aqui, temos uma operação de soma bem simples; a variavel declarada (c) recebe, como valor, a soma dos valores atribuidos as vars a & b

# agora, vamos exibir o valor da var (c)
print('O valor da variavel c é: ', c)

print()
print('----------------- outros operadores python (subtração, multiplicação, divisão) -')

# abaixo, serão implementadas algumas novas operações com uso dos operadores aritmeticos
print('Resultado da subtração de a - b = ', a - b)
print('Resultado da multiplicação de a * b = ', a * b)
print('Resultado da divisão de a / b = ', a / b)

# ==========================================================================

print()
print('================= INFERENCIA TIPO ==================')

# declarar 3 variaveis
numUm = 560 # numUm - convenção de declaração de variavel de nome composto. 
NumDois = 458.56
NOME = 'Chilindrina'

# fazer uso da função print() para exibir os valores das variaves
print('--------------- valores das variaveis ------------')
print(numUm)
print(NumDois)
print(NOME)

print()
print('--------------- tipos das variaveis ------------')
print(type(numUm)) # função type tem origem no python core - sua tarefa é exibir o data type, ou seja, o tipo de dado inferido para a variavel
print(type(NumDois))
print(type(NOME))

print('================= MANIPULAÇÃO DE STRINGS ==================')
print()

umaFrase = 'Hoje é um dia excelente!' # esta é uma string atribuida como valor para a varaivel umaFrase; string nada mais é do que um conjunto de caracteres

# nos proximos passos vamos manipular a string e exibir os valores dasa manipulações
print('----------------- manipulando a string ------------------')

print(umaFrase) # aqui estamos exibindo o valor da variavel umaFrase
print(type(umaFrase)) # aqui, estamos observando seu data type

print(umaFrase[0]) # aqui, nesta instrução, estamos fazendo uso do caractere [](colchete); nesta instrução, este caracter assume um "papel" interessante para a nossa manipulação da string; ele se torna o "slice operator", ou seja, o operador de fatiamento da string. Neste caso, estamos selecionando/fatiando/cortando o valor da varravel umaFrase - a partir da indicação de um INDICE POSICIONAL OCUPADO POR ALGUM VALOR. Aqui, o indice posicional indicado é 0 (zero)

'''
 abaixo, temos uma sequencia numerica associada a cada um dos caracteres que compõem a nossa string; esta sequencia composta por estes numeros é, naturalmente/tecnicamente, chamado de INDICES POSICIONAIS DE CONJUNTO DE VALORES/DADOS  


    0   1   2   3  4   5   6   7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 
    H   o   j   e      é       u  m      d  i  a     e  x  c  e  l  e  n  t  e  !

'''

print(umaFrase[2:12]) # aqui, estamos fazendo a seleção não só de um valor mas de um INTERVALO DE VALORES; neste caso, o intervalo de valores inicia no indice posicional 2 e se encerra no indice posicional 12. Este subconjunto/substring é definido por três parametros: 2 - indice onde o intervalo começa; 12 - indice onde o intervalo termina; (:) em temos simples o caratere dois pontos significa: "me dê estes valor que começão aqui e termina ali! - de 2 ate 12";

# [ .............[ - intervalo semi-aberto: intervalo semi-aberta é um conceito matematico que determina - dentro do subconjunto - que o 1º valor do intervalo seja inserido no subconjunto e o ultimo valor seja excluido. Essa exclusão se dá a partir da seguinte operação - executada via python core -> [2:12] (-1) = [2:11]

print(umaFrase[:8])
# [ .............[ - intervalo semi-aberto: intervalo semi-aberta é um conceito matematico que determina - dentro do subconjunto - que o 1º valor do intervalo seja inserido no subconjunto e o ultimo valor seja excluido. Essa exclusão se dá a partir da seguinte operação - executada via python core -> [:8] (-1) = [:7]

print(umaFrase[3:]) # aqui, temos mais um intervalo. Neste caso, o novo intervalo inica-se no indice posicional 3 e será encerrado no ultimo caractere da string; portanto o conceito de intervalo semi-aberto, aqui, não se aplica;


