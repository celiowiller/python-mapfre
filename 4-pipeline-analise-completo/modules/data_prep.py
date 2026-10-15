# ESTE ARQUIVO TEM COMO OBJETIVO: REALIZAR O "CRUZAMENTO" DAS NOSSAS BASES DE DADOS, CLASSIFICAÇÃO - FAZENDO USO DE EXPRESSÕES REGULARES - E, POR FIM, SALVAR OS ARQUIVOS "PROCESSADOS" PARA O RESTANTES DAS OPERAÇÕES COM OS DADOS 

# 1. importar os recursos necessarios 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. definir uma função para classificar o centro de custos 
def classificar_centro_custos(descricao: str):
    """  Categorizar a transação num centro de custo com base em palavras-chave."""
    desc = str(descricao).lower()

    # 2.1. vamos definir os centros de custo
    # 2.1.1. FINANCEIRO
    depto_financeiro = ['emprestimo', 'financiamento', 'juros', 'banco', 'credit', 'credito']

    # 2.1.2 RECURSOS HUMANOS
    depto_rh = ['salario', 'folha', 'beneficio', 'rh']

    # 2.1.3 TECNOLOGIA
    depto_ti = ['nuvem', 'aws', 'software', 'ti', 'hardware']

    # 2.1.4 OPERAÇÕES 
    depto_operacoes = ['aluguel', 'energia', 'agua', 'manutencao']

    # definir uma estrutura de decisão aninhada 
    if any(k in desc for k in depto_financeiro):
        return 'CC_1001_FINANCEIRO'
    elif any(k in desc for k in depto_rh):
        return 'CC_2001_RECURSO_HUMANOS'
    elif any(k in desc for k in depto_ti):
        return 'CC_3001_TECNOLOGIA'
    elif any(k in desc for k in depto_operacoes):
        return 'CC_4001_OPERACOES'
    else:
        return 'CC_9001_GERAL' # caso nenhuma das ocorrencias anteriores sejam obtidas

# 3. definir uma nova função para fazer a integração de dois dos nossos tres datasets
def integrar_contabilidade_tesouraria(caminho_raw, caminho_processed):
    """ Unificar os ados de Tesouraria e Contabilidade usando MERGE"""

    # 3.1. definir duas vars para receberem, como valor, os arquivos de dados de contabilidade e tesouraria
    df_tes = pd.read_csv(caminho_raw / 'tesouraria.csv')
    df_cont = pd.read_csv(caminho_raw / 'contabilidade.csv')
    
    # 3.2. fazer uso do merge para integrar os dados 
    df_integrado = pd.merge(df_tes, df_cont, on = 'ID_Transacao', how = 'inner')
    df_integrado['Centro_de_Custo'] = df_integrado['Descricao'].apply(classificar_centro_custos)

    # 3.3. fazer o armazenamento dentro da pasta data/processed
    df_integrado.to_csv(caminho_processed / 'tesouraria_contabilidade_processado.csv')

    # 3.4. retorno da função 
    return df_integrado

# 4. gerar a função para mostrar os graficos financeiros
def gerar_dashboard_financeiro(df_financeiro, pasta_saida_img):
    """ gerar visualizações de custos consolidados """
    plt.figure(figsize=(10, 5))

    # 4.1. fazer uso do seaborn para o grafico
    sns.barplot(
        data=df_financeiro,
        x = 'Centro de Custo',
        y = ' valor Movimentado',
        estimator=sum,
        errorbar = None,
        pallete = 'Blues_d'
    )

    # 4.2. configurar o restante da plotagem
    plt.title('Total Movimentado por centro de custo')
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Valor total em (R$)')
    plt.tight_layout()
    plt.savefig(pasta_saida_img / 'gastos_por_centro_custo.jpg', dpi = 300)
    plt.close()