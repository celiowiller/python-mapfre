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
