'''
UDF -> User Defined Function (Funções definidas pelo Usuario), ou seja, blocos de codigo reutilizaveis - com o menor numero de linhas possivel - definidos por nós, os programadores e programadoras

Qual é a definição de função? em Python, uma função é definida a partir do uso da palavra reservada/comando def!

função nada mais é do que blocos de codigo reutilizaveis. Estes blocos de codigo podem cumprir uma ou mais tarefas para um determinado proposito.

descrição de uma função 

def -> nome_da_função -> ():
    aqui, descrevemos alguma(s) instrução(ões) que compõe(m) a função, ou seja, as tarefas que a função irá cumprir

    return -> expressão de retorno/resposta da função 
    podemos considerar que a expressão return é opcional; posso criar uma função e não, necessariamente, fazer uso dela
'''

# abaixo, a definição da função exibir() terá um parametro. Um parametro, nada mais é do que uma variavel **** esta variavel/parametro será "enxergada/existirá" somente para a função 
def exibir(umTexto): # umTexto -> é o parametro/variavel local/pertencente unica e exclusivamente a esta função; em algum momento este parametro receberá algum valor que será associado á ele;

    print(umTexto) # aqui, a função print() é a descrição da tarefa que queremos que a função exibir() cumpra para nós. Nesta caso, a função exibirá o valor dado ao parametro umTexto
# print()
# acima, a função exibir() foi definida; agora, precisamos chamar esta função à sua execução; para fazer isso, precisamos criar o CALLER -> é o objeto chamador da função 

exibir('Essa é a 1ª chamada da função!') # aqui está o objeto chamador da função -> CALLER
exibir('Essa é a 2ª chamada da função')
exibir(9898565653231215454545452)
exibir(268.741)


print()
print('-------------- função com uso de keyword/palavra-chave -------------- ')

# var global


# definir a nova função 
def dados(nome, idade = 45): # parametro/valor default
    prefixo = 'nome :' + nome
    # ! 1ª tarefa: exibir o valor associado ao prametro nome
    # print(prefixo)
    # exibir('nome: ', nome) este contexto de chamada da função não funciona! Porque nossa função exibir() tema apenas 1 parametro. Se indicarmos o lietarl de string temos de definir um novo parametro para a função e, consequentemente, ao chamar a função à sua execução, precisamos dar à ela 2 argumentos.
    exibir(prefixo)

    # 2ª tarefa que a função irá cumprir: exibir o valor associado ao parametro idade
    # print(idade)
    exibir(idade) # passagem por referencia de valor 

    # 3ª tarefa: é fazer a verificação do valor da idade e exibir uma mensagem 
    # para este proposito vamos fazer uso da isntrução if/else -> estrutura de decisão a partir de uma condição 
    if idade >= 18: # esta expressão de teste; portanto se a expressão for considerada verdadeira, o print exibirá a mensagem abaixo.
        print('Pode entrar.')

    else: # mas, SE A AVALIAÇÃO FOR CONSIDERADA FALSA, a taerfa executada será esta, abaixo - elif
        print('Sai fora de-menor!')
    # ESTA ESTRUTURA - if/else - ÉM CONHECIDA COMO ESTRUTURA DE DECISÃO.

    return # EXPRESSÃO DE RETORNO PAR AO ENCERRAMENTO DA FUNÇÃO 

print('Função dados() será chamada...')

# definir o objeto chamador da função 
dados('Ecler', 80) # valores default
dados(idade = 89, nome = 'Saul Goodman')
# toda e qualquer obedece a ordem posicional dos argumentos dados aos parametros

print()
print('-------------- função lambda -------------- ')

'''
LAMBDA: em python, a função lambda é uma função sem nome - anônima!

como uma função lambda não tem nome, precisamos associa-la a um elemento que possa ser identificado/referenciado pelos eu nome -> isso significa que: uma função lambda deve compor uma EXPRESSÃO DE FUNÇÃO; nada mais é que uma variavel que recebe como valor uma função; assim, a função lambda/anonima pode ser eventualmente executada.
'''
# vamos definir nossa função lambda
soma = lambda valor1, valor2 : valor1 + valor2

# agora, precisamos chamar a função a sua execução 
print('O valor da soma da função lambda é: ', soma(100, 150))

'''
soma: variavel que recebe como valor a função lambda

lambda: palavra reservada/comando que define a função 

valor1, valor2: são os parametros da função lambda

valor1 + valor2: operação/tarefa que a função lambda irá cumprir
'''

