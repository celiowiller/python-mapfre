# ESTE É O "ORQUESTADOR" DO PIPELINE. CONECTA TODOS OS "PEDAÇOS"/MODULOS DO PROJETO

# 1. importar os arquivos necessarios
import config
from modules.financial import  automatizar_impostos_transacoes
from modules.data_prep import (
    integrar_contabilidade_tesouraria,
    gerar_dashboard_financeiro
)
from modules.ml_pipeline import treinar_modelo_emprestimos
from modules.file_manager import (
    organizar_diretorios,
    exportar_excel_formatado,
    enviar_alerta_execucao,
    registrar_logs
)

# 2. definir a função do orquestrador - "coração da execução"
def executar_pipeline():
    print('=' * 60)
    print('INICIANDO PIPELINE DE DATA SCIENCE & AUTOMAÇÃO FINANCEIRA')
    print('=' * 60)

    # 2.1. definir a sequencia de execuções dos modulos do pipeline

    try:
        # se tudo correr bem, aquilo que, aqui, implmentarmos, será executado
        # 2.1.1 organizar os diretorios
        pasta_execucao =  organizar_diretorios(config.OUTPUT_DIR)
        pasta_logs = pasta_execucao / 'logs'
        pasta_ml = pasta_execucao / 'machine_learning'
        pasta_fin = pasta_execucao / 'financeiro'

        registrar_logs(pasta_logs, 'Iniciando pipeline de processamento')
        print(f'[PASSO 1] Estrutura de pastas criada em: {pasta_execucao}')

        # 2.1.2. junção dos datasets 
        df_integrado = integrar_contabilidade_tesouraria(config.DATA_RAW_DIR, config.DATA_PROCESSED_DIR)
        registrar_logs(pasta_logs, 'Bases de tesouraria e contabilidade unidas e salvas em data/processed.')
        print('[PASSO 2] Bases unidas e salvas em data/processed')

        # 2.1.3. impostos, centro de custos e dashboard financeiro
        df_financeiro = automatizar_impostos_transacoes(
            df_integrado,
            coluna_valor='Valor_Movimentado',
            aliquota = config.ALIQUOTA_IMPOSTO
        )
        gerar_dashboard_financeiro(df_financeiro, pasta_fin)
        registrar_logs(pasta_logs, 'Impostos calculados e grafico gerado.')
        print('[PASSO 3] Impostos automatizados e grafico financeiro gerado e salvo.')

        # 2.1.4. treinamento do ML e salvamento das saidas
        caminho_loan = config.DATA_RAW_DIR / 'loan.csv'
        modelo, metricas, df_ml_resultados = treinar_modelo_emprestimos(
            caminho_loan,
            pasta_ml,
            config.DATA_PROCESSED_DIR
        )
        registrar_logs(pasta_logs, f"Modelo Treinado. ROC-AUC: {metricas['roc_auc']: .4f}. Todos os artefatos foram salvos.")

        print(f"[PASSO 4] ML Treinado. ROC-AUC: {metricas['roc_auc']: .4f}. Todos os artefatos foram salvos.")

        # 2.1.5. exportação do relatorio final
        caminho_excel = pasta_fin / 'Relatorio_Consolidade.xlsx'
        exportar_excel_formatado(df_financeiro, df_ml_resultados, caminho_excel)
        registrar_logs(pasta_logs, f'Relatorio Excel gerado em: {caminho_excel}')

        # 2.1.6. simulação de notificação
        enviar_alerta_execucao(
            status='SUCESSO',
            detalhes = 'Pipeline finalizado. Tudo correu muito bem!'
        )

    except Exception as e :
        # caso o contrario ocorra, teremos uma exeção (erro) lançado
        if 'pasta_logs' in locals():
            registrar_logs(pasta_logs, f'ERRO CRITICO: {str(e)}')
        enviar_alerta_execucao(status='ERRO', detalhes=str(e))
        raise e

if __name__ == "__main__":
    executar_pipeline()