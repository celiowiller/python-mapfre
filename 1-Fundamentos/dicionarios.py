'''
    um dicionario tambem é um conjunto de dados - da mesma forma que listas e strings; mas com algumas diferenças:

    1. para definirmos um dicionario é necessario usar os caracteres { } chaves

    2. um dicionario é composto por pares key:value / chave:valor 

    3. o conceito de indice posicional NÃO EXISTE para um dicionario 
'''

# definir um dicionario 
d = {
#   chave  : valor
#   key    : value
    'Nome' : 'Florinda',
    'idade': 37,
    'Curso': 'Python',
    20     : 'reais'   
}

# exibir o dicionario
print('Este é o conteudo do dicionario: ', d)

print('================= OPERAÇÕES COM DICIONARIOS ==================')
print()

print('Imprimir o valor da key/chave [Nome]: ', d['Nome'])
print('Imprimir o valor da key/chave [idade]: ', d['idade'])
print('Imprimir os valores de todos os elementos key/chave do dicionario: ', 
        d['Nome'], d['idade'], d['Curso'], d[20]
      )
print('Teste: ', 
        d['Nome']
      )

#print('Teste: ', 
        # d['endereco']
      # )

#----------------------------------------------------------
# até aqui, fizemos uso do processo de seleção de elementos - a partir de suas chaves;
# também podemos fazer uso da função get()
print('------------------ uso da função get ---------------------')
print(d.get('idade')) # aqui, com uso da função get() temos um processo de seleção INDIRETA.
print(d.get('endereco')) # aqui, a saida é None.

#----------------------------------------------------------
print('------------------ processos de manipulação ---------------------')
# observar a possibilidade de alterar valores de um dicionario
d['Nome'] = 'Clotilde'
d['Curso'] = 'Mecanica Industrial'

# criar um novo para key:value / chave:valor
d['Sobrenome'] = 'Lalala'

print('Dicionario com novos valores: ', d)

#----------------------------------------------------------
print('------------------ novas formas de criar um dicionario ---------------------')

# definir um novo dicionario
disciplinas = {}.fromkeys(['Filosofia', 'Lingua Protuguesa', 'Fisica'], 0)
print(disciplinas)

# neste passo vamos criar uma estrutura de repetição - loop - para iterar sobre todos os valores do dicionario e exibir seus itens
for r in disciplinas.items():
    print(r)


'''
    loop nada mais é do que uma estrutura de repetição; repetição de que? repetição de algo que queremos que seja executado mais de uma vez; portanto este pode ser considerado um processo de automação. Neste caso, a tarefa repetida será a impressão da letra (r)

    aqui, estamos usando o loop for... in -> isso significa que: estamos dizemos que PARA um determinado conjunto de dados queremos que aconteça algo; este algo é a impressão do valor encontra pela variavel r; o loop FOR...IN faz uso de uma variavel auxiliar/iteradora/contagem - > esta variavel deve ser definidas por nós; o python nunca será responsavel pela definição dela 

    então, lemos a instrução da seguinte forma: for r in disciplinas.items() -> lê-se: PARA A VARIAVEL r DENTRO DO CONJUNTO DE DADOS disciplinas - faça algo: o que é este algo? execute a tarefa de imprimir, em tela, todo e qualquer valor que a varaivel r encontrar. Encontrar onde? Dentro do dicionario disciplinas.

   r in  disciplinas {
            'Filosofia': 0, : 1ª iteração 
            'Lingua Protuguesa': 0, 2ª iteração
            'Fisica': 0  3ª iteração
        }

    ao executar o loop, ocorre o seguinte processo:
    print(r)
    1ª iteração resulta em : 'Filosofia': 0 
    2ª iteração resulta em: 'Lingua Protuguesa': 0
    3ª iteração resulta em: 'Fisica': 0

    neste, já encotrados todos os valoeres, a condição de repetição não é mais satisfatoria, portanto, o loop FOR se encerra e segue o fluxo de execução do codigo 
'''

print()

print('----------------------')

# loop para iterar sober o dicionario d
# o uso do "espaço" entre a função print() e a margem esquerda do arquivo é necessario para indicar que : A FUNÇÃO print() PERTENCE AO LOOP FOR; OU SEJA, FAZ PARTE DO CORPO DO LOOP. Caso não consideremos este espaço hierarquico, o loop mostar erro pois sua estrutura demanda esta hierarquia. Esta hierarquia é conhecida, tecnicamente, como INDENTAÇÃO!

for x in d.items(): # função que auxilia no rastreamento do dados que compõem o conjunto
    print(x)
   