'''
 agora, vamos começar a lidar com elementos de maior complexidade. Portanto, vamos iniciar nossos codigos fazendo a "importação" - para dentro do nosos projeto - dos recursos necessarios para o pleno funcionamento das aplicações. Estes recursos devem, necessariamente, serem instalados junto do python core.
'''

import numpy as np  # aqui, a lib/recurso/biblioteca/modulo... recebe um "apelido", portanto, quando precisarmos referenciar este recurso basta escrever as letras np

# NUMPY É UMA BIBLIOTECA, ESTRITAMENTE NUMERICA, DO PYTHON; OU SEJA, QUALQUER RECURSO QUE FOR USADO - A PARTIR DE NUMPY - PRECISA SER NUMERICOS - CASOS CONTRARIO PODEMOS TER PROBLEMAS NA EXECUÇÃO DO CODIGO 

import pandas as pd # aqui, a lib/recurso/biblioteca/modulo... recebe um "apelido", portanto, quando precisarmos referenciar este recurso basta escrever as letras pd

# criar duas matrizes numéricas - ambas receberão valores distintos
matriz1 = np.array([[2, 4], [5, -6]]) # esta éa função array(), com origem no numpy, especificamente usada para criar arrays.

matriz2 = np.array([[9, -4], [3, 5]])

# definir a operação de soma de matrizes
matrizResultante = matriz1 + matriz2

# exibir o resultado da soma das matrizes
print('O resultado da operação é: ', matrizResultante)

print()
print('==================== OPERAÇÕES/ANALISES COM NUMPY & PANDAS================ ')

# definir uma Series - uma Series nda mais do que uma matriz unidimensional
umaSerie = pd.Series([1, 2, 3, np.nan, 6, 8, 'Hello'])

# acima, temos um valor chamada 'np.nan' -> este é o recurso com origem no numpy que nos oferece a possiblidade de trabalhar com um valor não-numerico(not-a-number); para a nossa Series, basicamente, temos uma lista de valores e, todos os elementos, são atribuidos como valor da var umaSerie

print(umaSerie)

print()
print('==================== MANIPULANDO DATAFRAMES ================ ')
print() 
print('------------------ criando o DataFrame 1 ---------------')

# neste passo, será definida uma nova variavel para receber um conjunto de dados para compor o dataframe
algumasDatas = pd.date_range('20260901', periods = 6)
print(algumasDatas)

'''
para criar o conjunto de dados do tipo DateTimeIndex tivemos de fazer uso destes recursos:

pd -> lib pandas

date_range(): esta é a função usada para criar o intervalo de valores baseados em datas

parametros: '20260901' -> parametro string que dá como referencia o ponto inicial  de data para a construção do intervalo de valores 

parametros: periods = 6 -> esta é a quantidade de valores que queremos que seja gerado para o intervalo que definimos; 

por padrão,, o pandas - com o uso da função date_range(), gera um intervalo de datas com uma 'freq' - frequency - diaria -> freq ='D'

DatetimeIndex(['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04',
               '2026-09-05', '2026-09-06'],
              dtype='datetime64[ns]', freq='D')
'''

# agora, vamos definir o DataFrame
df1 = pd.DataFrame(np.random.randn(6, 4), index = algumasDatas, columns = list('ABCD'))

'''
DataFrame: classe do pandas para gerar o df1

np.random.randn(6, 4): recurso do numpuy para gerar valores randomicos; os valores 6, 4 significam que os valores gerados irão "popular" 6 linhas e 4 colunas de dados 

index = algumasDatas: aqui, estamos usando a nossa var algumasDatas para atuarem como indice de linha do df1

columns = list('ABCD'): aqui, definimos os nomes/labels das colunas do df1
'''
print()
print('Este é o nosso 1º DataFrame')
print(df1)
print()

print('------------------ criando o DataFrame 2 ---------------')
# agora, para criar o df2 usaremos um dicionario
df2 = pd.DataFrame({
    'A': 1., # valor constante repetido para todas as linhas do df2

    'B': pd.Series(1, index = list(range(4)), dtype = 'float64') , # Series com 4 elementos do tipo float que resulta no numero 1.0

    'C': pd.Timestamp('20260908'), # aqui, o valor de data é replicado para todas as linhas 

    'D': np.array([3.0] * 4, dtype = 'int32'), # array com 4 valores - indicado na equação [3.0] * 4 - devemos lembrar o valor é do tipo float - mas o resultado, teoricamente, deve ser tipo int

    'E': pd.Categorical(['teste', 234, 'novo teste', 7563.9]), # categoria com valores variados/flexiveis

    'F': 'esta é uma string' # string "populando" todas as linhas do df2
})

print()
print('Este é o df2')
print(df2)

print()
print('==================== OBSERVANDO -  FAZENDO ANALISE PRIMARIA - OS CONTEXTOS DOS DFs  ================ ')
print()

# neste passo, vamos fazer a leitura "resumida" do df
print('primeiras linhas do df1')
print(df1.head(2))
print('primeiras linhas do df2')
print(df2.head(2))

print()

print('ultimas linhas do df1')
print(df1.tail(2))
print('ultimas linhas do df2')
print(df2.tail(2))

print()

# aqui, vamos fazer a "leitura" de indice dos dfs; para este proposito será utilizado o comanod index
print('indices do df1')
print(df1.index)
print('indices do df2')
print(df2.index)

print()
# agora, vamos observar as colunas dos Dfs
print('colunas do df1')
print(df1.columns)
print('colunas do df2')
print(df2.columns)

# vamos fazer uma "leitura" de sumarização/resumo estatico dos DFs; para este proposito vamos fazer da função describe()
print()

print('resumo estatistico do df1')
print(df1.describe())
print('------------------------')
print('resumo estatistico do df2')
print(df2.describe())

print()
print('==================== OPERADORES .loc, .iloc, .at, .iat  ================ ')
print()

'''
.loc: este operador funciona através de elementos - do df - nomeados (como nomes/valores) labels - PARA ESPECIFICAR UM INTERVALO DE VALORES EXTRAIDOS DO DF

.iloc: este operador funciona, aplicado ao df, acessando valores a partir de indices posicionais de linha e coluna de qualquer df - PARA ESPECIFICAR UM INTERVALO DE VALORES EXTRAIDOS DO DF

.at: este operador funciona, aplicado ao df, acessando valores a partir de indices posicionais de linha e coluna de qualquer df - PARA ESPECIFICAR O ACESSO E SELEÇÃO DE UM ÚNICO VALOR DO DF

.iat: este operador funciona, aplicado ao df, acessando valores a partir de indices posicionais de linha e coluna de qualquer df - PARA ESPECIFICAR O ACESSO E SELEÇÃO DE UM ÚNICO VALOR DO DF
'''

print(df1)
print()
print(algumasDatas)
print()
print(df1.loc[algumasDatas[-1]]) # indice negatiov sugere a contagem de valores no sentido "inverso" do padrão de leitura

print()

print(df1.loc['2026-09-05', ['A', 'B']])
print()

# agora, vamos observar o comportamento do .iloc 
print(df1.iloc[:4, :3]) # intervalo semi-aberto [ ....[ (-1)
print()

print(df1.iloc[1:5, :])

print()
print('------------------- operadores .at e .iat ---------------')
print()

print('operador .at')
print(df1.at['2026-09-02', 'A'])

print()

print('operador .iat')
print(df1.iat[1, 3])

# --------------------------------------------------------------------
print()
print('==================== GRÁFICOS/MATPLOTLIB ================ ')
print()

'''
Matplotlib: biblioteca/modulo/recurso, do python, que nos dá a possibilidade de criar graficos 2D para a visualização de dados.
'''

# vamos importar a biblioteca
import matplotlib.pyplot as plt

# acima, o pyplot atua como uma "área de desenho" para exibir o grafico

# agora, vamos gerar um novo df
dS = pd.Series(np.random.randn(1000), index = pd.date_range('20120101', periods = 1000))

# o recurso de dados gerado, acima, é uma TIME SERIES (SERIE TEMPORAL); significa que: foi uma Series com indices posicionais e suas linhas de dados baseadas em datas.

print(dS)

# definir uma soma acumulada 
# a soma acumulada é importante pois nos dá a possibilidade de obervarmos as oscilações dos dados e suas transformações/evolução 

somaAcumulada = dS.cumsum()
print('resultado da soma acumulativa: ', somaAcumulada)

# ---------------------------------------------------------------

# agoa, vamos definir o grafico para observavr as variações dos dados ao longo do periodo de 1.000 dias
dfGraf = pd.DataFrame(
        np.random.randn(1000, 4), 
        index = dS.index, 
        columns=['Ola mundo', 'limitada função', 'lista é ruim', 'provocando'] 
        )
print(dfGraf)

# plotar o Grafico
oGrafico = dfGraf.cumsum()
oGrafico.plot()
plt.show()
