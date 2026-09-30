# PYTHON LIST - listas com python

'''
Uma lista, em python, nada mais é do que um conjunto de dados - robusto, flexivel e extremamente util. Pode ser composto por dados de qualquer "natureza"/tipo. Para definir uma lista usamos os caracteres de contexto [] - colchete; o caractere colchete, atribuido a, uma variavel, define uma lista em python

Toda e qualquer lista, em python, tambem obedece as regras observadas a partir da string - ou seja - são organizadas e manipuladas a partir de seus indices posicionais.
'''
#           0      1       2                 3                    4
umaLista = [1, 'palavra', 'c', 'DSHUSAFIUASHFIASDHFISAUDHFIOA', 256.78]
print(umaLista)

# definir uma nova lista
#          0        1                          2
#                                0         1             2                 3   
#                                                  0        1     2                        
listona = [74, 'Sopranos', ['The Office', 123, ['Xanadu', 532.90, '?'], 'power']]
print(listona)

print()
print('=============== MANIPULANDO AS LISTAS ================')
print('------------ operações com listas ---------------')
print()
print('listona no index 2: ', listona[2])
print()
print('umaLista no index 3: ', umaLista[3])
print()
print('acessar 123 de listona: ', listona[2][1])
print()
print('acessar o caractere ?: ', listona[2][2][2])

# ----------------------------------------------------------------------
print()
print('------------ outras operações com listas ---------------')

#             0      1         2            3         4        5
lingProg = ['Java', 'C', 'Visual Basic', 'Python', 'Cobol', 'Fortran', 'Clipper', 'Javascript', 'Objective-C e Swift', 'Rust']

print(lingProg)
print(lingProg[4]) # saida: Cobol
print(lingProg[5: 8]) # saida: Fortran, Clipper, javascript - aqui esta sendo praticado o intervalo semi-aberto

print('qual será esta saida lingProg[-1]: ', lingProg[-1]) # saida: Rust
print('qual será esta saida lingProg[-2]: ', lingProg[-2]) # saida: Objective-C e Swift

print('qual será esta saida lingProg[5::-1]: ', lingProg[5::-1])
print('qual será esta saida lingProg[5::-1]: ', lingProg[8:5:-1])
print('e esta lingProg[::-1]: ', lingProg[::-1])
print('e esta lingProg[::-1]: ', lingProg[5:8:1])

'''
qual será esta saida lingProg[1::-1]: ', lingProg[1::-1] -> esta instrução lê-se da seguinte forma:

1º VALOR: start -> significa que este é o "ponto" onde o fatiamento começa;

2º VALOR: entre os dois pontos :--: stop -> neste caso, esta vazio; aqui é onde o fatiamento termina! portanto, ainda neste caso, não temos indice posicional

3º VALOR: step -> o "passo", ou seja, o intervalo entre os elementos -> significa que vamos "de traz para frente" percorrendo a lista

*** ou seja, estamos invertendo o fatiamento
'''
# ------------------------------------------------------------------------

print()
print('------------ funções nativas python par amanipualr listas ---------------')
print(len(lingProg)) # função para obter o numero total de dados dentro do conjunto 

print(max(lingProg)) # função para observar a lista e encontrar o valor maximo dentro dela 

print(min(lingProg)) # função para observar a lista e encontrar o valor minimo dentro dela 
print('função diferentaça')
# nova lista
diferentaça = ['768sadgfa', '%teet', '-hjdsafhkj5', ')mnfTre4', '&avascript', 'C#', '4', 8]

print(min(diferentaça))
print(max(diferentaça))

# python para concluir quais sao valores min() e max() usa o conceito matematico < >; ou seja, para que o python consiga fazer esta comparação é necessario que os dados sejam de mesma natureza;



