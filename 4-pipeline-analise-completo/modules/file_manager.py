# O OBJETIVO DESTE ARQUIVO É: GERENCIAR PASTAS E ARQUIVOS DO SISTEMA OPERACIONAL E, TAMBÉM, GERAR RELATORIOS CONECTANDO AO ORQUSTRADOR (arquivo que vamos, ainda, implementar)

# 1. importar os arquivos necessarios
import os
import shutil # recurso que nos auxiliará em operações avançadas em arquivos e diretorio (por exemplo: mover ou copiar, etc) 
from datetime import datetime
import pandas as pd

# 2. definir a função que irá organizar a dinamica de diretorios do pipeline
def organizar_diretorios(pasta_destino):
    """ função que organiza a dinamica de pastas e arquivos do pipeline"""
    
    # 2.1. definir propriedades que receberão com valor o momento em que a função é executada e o caminho criado para a nova pasta
    data_hoje = datetime.now().strftime('%Y-%m-%d')
    pasta_diaria = pasta_destino / data_hoje

    # 2.2. definir a propriedade/variavel subpastas para que seja possivel criar outras novas pastas para armazenar aquivos 
    subpastas = ['financeiro', 'machine_learning', 'logs']
    for sub in subpastas:
        os.makedirs(pasta_diaria / sub, exist_ok=True)

    # agora, vamos retornar a pasta_diaria
    return pasta_diaria

# 3. definir uma nova função para gravar os logs do pipeline
def registrar_logs(pasta_logs, mensagem):
    """ função para gravar linhas de eventos no arquivo de log da aplicação"""
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    caminho_log = pasta_logs / 'logs_execucao.log'
    with open(caminho_log, 'a', encoding='utf-8') as f:
        f.write(f'[{data_hora}] {mensagem}')

# 4. definir uma nova função para salvar arquivos no formato .xlsx
def exportar_excel_formatado(df_financeiro, df_ml, caminho_saida):
    """ função para exportar relatorio final com multiplas abas """
    with pd.ExcelWriter(caminho_saida, engine='openpyxl') as writer:
        df_financeiro.to_excel(writer, sheet_name="Tesouraria_Contabilidade", index=False)
        df_ml.to_excel(writer, sheet_name="Analise_Credito_ML", index=False)

# 5. definir função de aviso de execução 
def enviar_alerta_execucao(status='SUCESSO', detalhes=''):
    """ função que simula notificações para o usuario ou sistemas de monitoramento """
    print(f'-------- ALERTA PIPELINE [{status}] --\nData/hora: {datetime.now()}\nDetalhes: {detalhes}')