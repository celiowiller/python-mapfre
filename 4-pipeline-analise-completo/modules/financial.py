# ESTE ARQUIVO DEFINE AS REGRAS DE NEGOCIO PARA A INTEGRAÇÃO DAS AREAS DE CONTABILIDADE E TESOURARIA

# 1. importar os recursos necessarios
import pandas as pd
import numpy as np

# 2. função para calculo de juros compostos 
def calcular_juros_compostos(capital: float, taxa_anual: float, periodos_meses: int) -> float:
    """ Calcular o montante final acumulado com juros compostos"""
    taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1 # esta é a formula de conversão de equivalencia de juros compostos 
    montante = capital * ((1 + taxa_mensal) ** periodos_meses) # esta é a formula classica do calculo dos juros compostos

    return round(montante, 2)

# 3. função para retorno sobre o investimento ROI
def calcular_roi(ganho: float, custo: float) -> float:
    """ Calcular o retorno sobre o invetimento (ROI) em percentagem"""
    if custo == 0: # se esta condição for verdadeira o retorno é zero -> 0.0. Indicamos esta verificação por ser um tratamento de segurança; se o custo for igual a 0, a função retorno 0.0% para evitar o erro de divisão por zero (0)
        return 0.0
    
    # caso o contrario ocorra....
    return round(((ganho - custo) / custo) * 100, 2)

# 4. função para aplicar a automatização de impostos em transações
# neste casso o parametro df nada mais é do qi+ue a tabela que será composta pelas transações 

# coluna_valor: esta é a coluna onde - no df - estarão os valores brutos

# aliquota: este é o percentual do imposto a ser aplicado 
def automatizar_impostos_transacoes(df: pd.DataFrame, coluna_valor: str, aliquota: float) -> pd.DataFrame:
    """ Aplicar o calculo automatizado de impostos retidos sobre uma lista de transações"""
    df_copy = df.copy() # aqui, criamos uma cópia do df original; é uma excelente pratica que pode ser adotada para outras tantas operações com dfs

    df_copy['Valor_Imposto'] = df_copy[coluna_valor] * aliquota # aqui, estamos criando uma nova coluna e será composta com o resultado da operação que calcula o valor bruto correspondente ao imposto retido

    df_copy['Valor_Liquido'] = df_copy[coluna_valor] - df_copy['Valor_Imposto'] # aqui, estamos criando um nova coluna para ser composta com o resultado da seguinte operação: subtraindo o valor do imposto retido do valor bruto da movimentação 
    return df_copy # aqui, retornamos a nova versão da tabela/df com as duas novas colunas incorporadas.

