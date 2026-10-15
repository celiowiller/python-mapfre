# ESTE ARQUIVO TEM COMO OBJETIVO: OPERAR COM ENGENHARIA DE DADOS - COM OS DADOS PRE-PROCESSADOS - E OPERAR UM MODELO ML (Machine Learning)

# 1. importar os recursos necessarios 
# ----- parte 1: recursos-base
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import joblib

# ----- parte 2: recursos-sklearn
from sklearn.model_selection import train_test_split # este é o recurso que divide os dados em 2 cojuntos: treino do modelo e, posteriormente, teste deste modelo depois de treinado

from sklearn.compose import ColumnTransformer # recurso que auxilia na manipulação e trasnformação de dados de uma unica coluna no contexto necessario para uso no modelo ML

from sklearn.pipeline import Pipeline # este é o recurso que "encadeia" varias etapas de pré-processamento e o modelo final num unico fluxo devidamente organizado. Dessa forma, é possivel evitar qualquer "vazamento" de dados durante todo o processo

from sklearn.impute import SimpleImputer # nos auxilia no tratamento de dados ausentes, por exemplo: (NaN ou null)

from sklearn.preprocessing import StandardScaler, OneHotEncoder # os dois recursos são, respectivamente: recurso usado para padronização de variaveis numericas para ficar com desvio padrão 1 e média 0; recurso usado para trasnformar variaveis categoricas (textos) em combinações binarias - 1 e 0

from sklearn.ensemble import RandomForestClassifier # modelo de classificação supervisionada - significa que teremos de oferecer para o modelo algum aprametro para ele aprenda a classificar qualquer coisa que necessitamos - 

from sklearn.metrics import(classsification_report, roc_auc_score, confusion_matrix, roc_curve) # respectivamente, são: gera um resumo textual com as metricas de precisão do modelo, entre outras; calcula a área sob a curva ROC(metricas de capacidade de discriminação do modelo); gera uma matriz de confusão(seu objetivo demonstrar acertos e erros do modelo); extrai os pontos ncessarios para desenhar o grafico da curva de comportamento e capacidade do modelo

# 2. definir uma função para treinar o modelo para observar os emprestimos 
def treinar_modelo_emprestimos(caminho_loan_csv, pasta_ml_output, caminho_processed):
     # 2.1. carregar os dados necessarios
     df = pd.read_csv(caminho_loan_csv)

     # 2.2. Feature Engineering =  processo de trasnformação, criação, seleção, e extração de dados brutos que possam, posteriormente, facilitar o aprendizado do modelo ML
     df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome'] # coluna que recebe como valor a soma da rendo do solicitante e do co-solicitante do emprestimo

     df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median()) # aqui, estamos selecionando a coluna de montante de emprestimo e preenchendo potencias valores ausentes com o valor calculado pela mediana.

     df['Income_to_Loan_Ratio'] = df['Total_Income'] / (df['LoanAmount'] + 1) # esta coluna recebe como valor a razão renda/emprestimo (CAPACIDADE DE PAGAMENTO). O +1 no denominador previne uma eventual divisão por zero.

     # 2.3. Tratamento da variavel "Alvo"
     df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
     df = df.dropna(subset=['Loan_Status'])

     # 2.4. persistir o dataset processado
     df.to_csv(caminho_processed / 'loan_features_processadas.csv', index = False)

     # 2.5. definir duas variaveis 
     x = df.drop(columns=['Loan_ID', 'Loan_Status'])
     y = df['Loan_Status']

     # 2.6. definindo, dividindo e organizando quais são as colunas numericas e categoricas
     num_features = x.select_dtypes(include = ['int64', 'float64']).columns.tolist()
     cat_features = x.select_dtypes(include=['object']).columns.tolist()

     # 2.7. iniciar o pipeline de trasnformação e pré-processamento
     num_transformer = Pipeline([
          ('imputer', SimpleImputer(strategy='median')),
          ('scaler', StandardScaler())
     ])
     # acima, foram definidas as etapas de processamento de dados numéricos: preenchendo com a mediana calculada - para valores ausentes - e, na sequencai aplicando a padronização(escala)

     cat_transformer = Pipeline([
          ('imputer', SimpleImputer(strategy='most_frequent')),
          ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
     ])
    # acima, foram definidas as etapas de processamento de dados categoricos: preenchendo com moda calculada - para valores ausentes: significa que estamos preenchendo com valores que aparecem com maior frequencia - e, na sequencia, fazemos a conversão para variaveis binarias (One-HotEncoding)

     preprocessador = ColumnTransformer([
          ('num', num_transformer, num_features),
          ('cat', cat_transformer, cat_features)
     ])
    # acima, combinamos os dois transformers para que cada tipo de coluna passe pela sua respectiva pipeline ao mesmo

     model_pipeline = Pipeline([
          ('preprocessador', preprocessador),
          ('classifier', RandomForestClassifier(n_estimators=100, random_state = 42, class_weight='balanced'))
     ])

     # aqui, acima, fizemos uso pleno do recurso Pipeline(): juntamos o preprocessador com o modelo final - RandomForestClassifier e estabelecemos um ciclo de 100 arvores - para aprendizado e decisão do modelo; posteriormente, indicamos o "peso" do algoritmo para 'balanced' para compensar potenciai/eventuais desequilibrios em aprendizados de dados, como por exemplo, categoricos - Loan_Status - Y e N; não pender tanto par aum lado nem par ao outro.