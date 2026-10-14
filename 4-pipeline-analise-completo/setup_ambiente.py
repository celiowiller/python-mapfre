# ESTE ARQUVO É UM ARQUIVO-AUXILIAR: SIGNIFICA QUE SERÁ USADO PARA GERARMOS, A PARTIR DELE, NOVOS DATASETS NECESSARIOS PARA ESTE PIPELINE.PROVAVELMENTE, IREMOS EXECUTAR ESTE ARQUIVO UMA UNICA VEZ; POIS SEU OBJETIVO É GERAR A PASTA data/raw E OS DATASETS SINTETICOS QUE IREMOS USAR PARA A ANALISE DO PIPELINE

# 1. importar os reursos necessarios 
import pandas as pd
import numpy as np
import config

# 2. definir uma função para executar a criação dos datasets
def inicializar_dados_raw():
    np.random.seed(42) # este é o recurso para gerarmos os dados randomicos e, toda a vez que executarmos, os dados gerados serão os mesmos - quem garante este comportamento é a função seed().

    # 2.1
    config.DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

    # 2.2. definir a base lógica para a criação dos datasets completares
    tesouraria = pd.DataFrame({
        'ID_Transacao': [f'TRX_{i:04d}' for i in range(1, 101)], # TRX_0001
        'Loan_ID': [f'LP00{1000 + i}' for i in np.random.randint(10, 50, 100)], # LP001010, LP001045
        'Valor_Movimentado': np.random.uniform(5000, 50000, 100).round(2),
        'Data_Movimento': pd.date_range(start = '2026-01-01', periods = 100, freq = 'D'),
        'Descricao': np.random.choice(['Pagamento Emprestimo', 'Servico Nuvem AWS', 'Folha Salarial', 'Aluguel Escritorio', 'Juros emprestimo'], 100) # função choice() indica escolha/sorteio 
    })

    tesouraria.to_csv(config.DATA_RAW_DIR / 'tesouraria.csv', index = False) # aqui, fechamos a geração dos dados sinteticos gerando o arquivo tesouraria.csv.

    # 3. aqui, nossa nova função irá gerar dados sinteticos para o contexto e analise contabil
    contabilidade = pd.DataFrame({
        'ID_Transacao': [f'TRX_{i: 04d}' for i in range(1, 101)],
        'Conta_Contabil': np.random.choice(['2.1.01_Emprestimos', '3.1.02_Despesas_Ops', '1.1.01_Caixa'], 100),
        'Status_Conciliacao': np.random.choice(['Consolidado', 'Pendente'], 100, p = [0.85, 0.15])  # por causa da relação de valores posicionais na lista estamos dizendo aqui, que: há 85% de chance do valor 'Consolidado' ser sorteado e 15% do valor 'Pendente' ser sorteado.  
    })

    contabilidade.to_csv(config.DATA_RAW_DIR / 'contabilidade.csv', index = False) # aqui, geramos o arquivo - a partir do df -  no formato .csv

    print(f'[OK] Dados de Tesouraria e COntabilidade gerados em: {config.DATA_RAW_DIR}')

if __name__ == '__main__': # esta é uma verificação padrão em Python: aqui, estamos garantindo que a nossa função só será executada se este script for rodado como 'elemento principla', ou seja, diretamente. Se for importado por outro arquivo e, assim, tentarmos executa-lo, não funcionará 
    inicializar_dados_raw()