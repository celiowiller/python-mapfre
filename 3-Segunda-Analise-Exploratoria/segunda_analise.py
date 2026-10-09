# ESTE SERÁ A NOSSA ANÁLISE EXPLORATORIA PARA O PIPELINE(FLUXO) DE DADOS DE VENDA 
# importando os recursos necessarios 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# BLOCO 1
'''
    1. carregar os dados 
    2. ler as primeiras linhas do df
    3. fazer um resumo estatistico 
'''

df = pd.read_excel('vendas.xlsx')
print('Primeiras 5 linhas do df')
print()
print(df.head())

print()

print('RESUMO ESTATISTICO')
print(df.describe())

# ---------------------------------------------------------------------------------

print()
print('OPERAÇÃO 1 - TOTALIZAÇÃO DE PRODUTOS VENDIDOS x REPRESENTANTES')

# definir uma variavel para receber como valor a totalização das vendas por representante
total_vendas_por_rep_colchete = df.groupby('Rep')['Quantity'].sum()
total_vendas_por_rep = df.groupby('Rep')[['Quantity']].sum()
print()
print('Total de vendas de produtos por representante:')
print(total_vendas_por_rep_colchete)
print(total_vendas_por_rep)

'''
total_vendas_por_rep: var que recebe como valor a totalização das vendas por representante

df.groupby('Rep'): este é o trecho de código que está "agrupando" os dados/elemementos/ocorrencias  do df  - tendo como base as colunas Rep e Quantity; cada grupo, agora, contem todas as linhas de vendas feitas por um mesmop vendedor

[['Quantity']]: aqui, estamos selecionando a coluna Qunatity; [[]] ao usar os caracteres colchetes duplos estamos retornando - como saida/resultado de operação - um "novo" dataframe.

.sum(): aplicação da função nativa .sum() sobre a coluna Qunatity assim temos a totalização das vendas de cada representante 

'''
print('------------------------------------------------------------------')
print()
print('OPERAÇÃO 2A - TOTAL de quantidade DE VENDAS REALIZADAS POR REPRESENTANTE *** este numero precisa fazer sentido para nós ')
qtde_vendas_por_rep = df.groupby('Rep').size()
# qtde_vendas_por_rep = df.groupby('Rep').count()
print()
print('Qtde de vendas realizadas para cada representante')
print(qtde_vendas_por_rep)


print('------------------------------------------------------------------')
print()
print('OPERAÇÃO 2B - MEDIA DE PRODUTOS VENDIDOS x REPRESENTANTE')
media_vendas_por_rep = df.groupby('Rep')[['Quantity']].mean()
print()
print('Média de produtos vendidos por representante\n')
print(media_vendas_por_rep)

print('------------------------------------------------------------------')
print()
print('FAIXA DE PREÇO POR PRODUTO (Menor e Maior preço)')

# definir uma nova var para receber como valor a agregação das operações
precos_produtos = df.groupby('Product')['Price'].agg(
    Menor_Preco = 'min',
    Maior_Preco = 'max'
)

# exibir o resultado da operação -  conhecida como: AMPLITUDE DE PREÇOS POR PRODUTO
print('\n----- AMPLITUDE DE PREÇOS POR PRODUTO ------')
print(precos_produtos)

# identificar o PRODUTO de menor e maior valor - VENDIDO POR CADA REPRESENTANTE
min_preco_idx = df.groupby('Rep')['Price'].idxmin() # função que escolhe apenas o produto Maintenance e ignora outra linha
max_preco_idx = df.groupby('Rep')['Price'].idxmax() # função que escolhe apenas o 1ª ocorrencia de produto de maior valor 

# aqui, estamos apenas retornando diretamente o valor numerico "em dinheiros" do menor e do maior 
min_preco = df.groupby('Rep')['Price'].min() 
max_preco = df.groupby('Rep')['Price'].max()
# acima, corremos o risco de sofisma

print('\n----- MENOR PREÇO DE PRODUTO POR REPRESENTANTE ------')
# exibir os valores obitdos, acima
print(df.loc[min_preco_idx, ['Rep', 'Product', 'Price']])
print(min_preco)

print('\n----- MAIOR PREÇO DE PRODUTO POR REPRESENTANTE ------')
print(df.loc[max_preco_idx, ['Rep', 'Product', 'Price']])
print(max_preco)

print()
print('\n----- AMPLITUDE DE PREÇOS por gerente/rep  ------')
# vamos uso, para este proposito, do conceito de PIVOT TABLE

def amplitude(x):
    return x.max() - x.min()

# agora, vamos definir uma nova var para receber ocmo valor a função pivot_table do pandas
pivot_amplitude = pd.pivot_table( # esta é a instrução que executa o pivot_table
    df, 
    index = ['Manager', 'Rep'],
    values = ['Price'], # esta é a coluna na qual a função amplitude será aplicada
    aggfunc = amplitude # esta é a chamada da função que calcula a anplitude de preços
).rename(columns = {'Price': 'Amplitude_Preco'})

# exibir o resultado
print('\n--- AMPLITUDE DE PREÇO POR GERENTE/REPRESENTANTE ---')
print(pivot_amplitude)

print()
print('\n--- ANALISE MULTIVARIADA - FATURAMENTO DE VENDAS E QUANTIDADE ---')

# criando a coluna Total_Vendas
df['Total_Vendas'] = df['Quantity'] * df['Price']

# exibindo dados de auxilio
print('valores da coluna Total_Vendas')
print(df['Total_Vendas'])

pivot_multivariada = pd.pivot_table(
    df, 
    index = ['Manager', 'Rep'],
    columns = 'Product',
    values = ['Total_Vendas', 'Quantity'],
    aggfunc = {'Total_Vendas':'sum', 'Quantity': 'sum'},
    fill_value = 0
)

print(pivot_multivariada)

print()
print('\n--- MATRIZ DE CORRELAÇÃO ---')
correlacao = df[['Price', 'Quantity', 'Total_Vendas']].corr()
print()
print(correlacao)


print()
print('\n--- TAXA DE CONVERSÃO POR REPRESENTANTE ---')

# definir uma nova var
funil_rep = df.groupby('Rep').apply(
    lambda x: pd.Series({
        'Total_Oportunidades': len(x),
        'Ops_Ganhas': (x['Status'] == 'won').sum(),
        'Taxa_Conversao_%': round( ( (x['Status'] == 'won').sum() / len(x)) * 100, 1),
        'Fat_Fechado_R$': x[x['Status'] == 'won']['Total_Vendas'].sum(),
        'Fat_Em_Risco_R$':x[x['Status'].isin(['pending', 'presented'])]['Total_Vendas'].sum(),
        'Fat_Perdido_R$': x[x['Status'] == 'declined']['Total_Vendas'].sum()
    })).reset_index()
print(funil_rep)


print()
print('\n--- TICKET MEDIO POR STATUS ---')

ticket_medio = df.groupby('Status').agg(
    Qtd_Oportunidades = ('Total_Vendas', 'count'),
    Faturamento_Total = ('Total_Vendas', 'sum'),
    Ticket_Medio = ('Total_Vendas', 'mean')
)

# exibir o resultado
print(ticket_medio)

print()
print('\n--- MATRIZ DE PRODUTO x STATUS VENDA ---')

matriz_produto_status = pd.pivot_table(
    df,
    index = 'Product',
    values = 'Total_Vendas',
    aggfunc = 'sum',
    fill_value = 0
)

# exibir os resultados
print(matriz_produto_status)

print()
print('\n--- DASHBOARD EXECUTIVO ---')

# vamos, neste 1º passo para criar o dash, verificar se existe uma coluna de datas no df; se existir, usaremos - caso contrario, criaremos

if 'Date' not in df.columns and 'Data' not in df.columns:
    start = pd.Timestamp('2025-06-01')
    end = start + pd.DateOffset(months = 12)
    df['Date'] = pd.date_range(start = start, end = end, periods = len(df))

# para finalizar a coluna Date, precisamos converter - diretamente - os valores gerados para o formato de data
df['Date'] = pd.to_datetime(df['Date'])

# DESENHAR O "CANVAS" - ESPAÇO DEFINIDO PARA O SURGIMETO DO DASHBOARD
fig, axes = plt.subplots(2, 2, figsize =(16, 20))


# Grafico 1: faturamento Efetivado (won) vs Em Risco vs Perdido

df.groupby(['Rep', 'Status'])['Total_Vendas'].sum().unstack(fill_value = 0).plot(kind='bar', stacked=True, ax=axes[0, 0], colormap = 'viridis')

# definindo o "eixo"/axes do Grafico 1
axes[0, 0].set_title('Composição do Pipeline por Representante')
axes[0, 0].set_ylabel('Total em R$')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Grafico 2: Evolução Trimestral de vendas Fechadas (Status == won)
vendas_ganhas_trimestre = df[df['Status'] == 'won'].resample('Q', on='Date')['Total_Vendas'].sum()

# acessar a var para plot o grafico
vendas_ganhas_trimestre.plot(kind='line', marker='o', color='skyblue', linewidth='2', ax=axes[0, 1])

axes[0, 1].set_title('Evolução Trimestral - Apenas Vendas Fechadas (R$)')
axes[0, 1].set_ylabel('Total Efetivado R$')
axes[0, 1].grid(True)

# Grafico 3 Ticket medio por Produto
df.groupby('Product')['Total_Vendas'].mean().plot(kind='barh', color='skyblue', ax=axes[1, 0])

axes[1, 0].set_title('Ticket Medio por Produto')
axes[1, 0].set_xlabel('Valor Médio R$')
axes[1, 0].grid(axis='x', linestyle='--', alpha=0.7)


# Grafico 4. Distribuição das Oportunidades pos Status
df['Status'].value_counts().plot(
    kind='pie', autopct = '%1.1f%%', colors=['#5cb85c', '#5bc0de', '#f0ad4e', '#d9534f'], ax=axes[1, 1]
)

axes[1, 1].set_title('Distribuição Percentual de Status das Negociações')
axes[1, 1].set_ylabel('')

# exibir o dashboard
plt.tight_layout()
plt.show()
