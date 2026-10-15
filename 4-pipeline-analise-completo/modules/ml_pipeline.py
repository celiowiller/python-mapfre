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

from sklearn.metrics import(classification_report, roc_auc_score, confusion_matrix, roc_curve) # respectivamente, são: gera um resumo textual com as metricas de precisão do modelo, entre outras; calcula a área sob a curva ROC(metricas de capacidade de discriminação do modelo); gera uma matriz de confusão(seu objetivo demonstrar acertos e erros do modelo); extrai os pontos ncessarios para desenhar o grafico da curva de comportamento e capacidade do modelo

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
          # este é o nosso modelo ML
          ('classifier', RandomForestClassifier(n_estimators=100, random_state = 42, class_weight='balanced'))
     ])

     # aqui, acima, fizemos uso pleno do recurso Pipeline(): juntamos o preprocessador com o modelo final - RandomForestClassifier e estabelecemos um ciclo de 100 arvores - para aprendizado e decisão do modelo; posteriormente, indicamos o "peso" do algoritmo para 'balanced' para compensar potenciai/eventuais desequilibrios em aprendizados de dados, como por exemplo, categoricos - Loan_Status - Y e N; não pender tanto par aum lado nem par ao outro.

     # 2.8. agora, vamos estabelecer a divisão dos dados num conjunto de treino - para o aprendizado e num conjunto de testes - que será para observarmos se o modelo, realmente, aprendeu algo
     X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42, stratify=y)

     model_pipeline.fit(X_train, y_train) # esta é a dunção que, de fato, treina o modelo -considerando os dados selecionados para o treino

     # 2.9. estabelecendo as previsões
     y_pred = model_pipeline.predict(X_test)
     y_proba = model_pipeline.predict_proba(X_test)[:, 1] # aqui, estamos gerando as classes de normalização - de 0 a 1 para a base de testes; para extrair a probabilidade (de 0.0 a 1.0) de o emprestimo ser aprovado para um cliente do conjunto de dados teste

     roc_auc = roc_auc_score(y_test, y_proba) # aqui, estamos calculando a pontuação da área so a curva de probabilidade - para observar "o quão bom é o modelo"

     report = classification_report(y_test, y_pred, output_dict=True)

     # 2.10. salvar o modelo e as metricas
     joblib.dump(model_pipeline, pasta_ml_output / 'modelo_rf_credito.pkl') # aqui, estamos gerando um arquivo .pkl que, se necessario, pode ser disponibilizado para qualquer outra aplicação - a partir do uso de APIs

     with open(pasta_ml_output / 'metrics_modelo.json', 'w') as f:
          json.dump({'roc_auc': roc_auc, 'report': report}, f, indent=4) # aqui, salvamos o arquivo, com as metricas, no formato .json

     # 2.11. definir e configurar os artefatos de visualização de performace geradas pelo modelo
     fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # aqui, temos um painel com 1 linha e 2 colunas  - de graficos lado-a-lado

     # desenhar a MAtriz de confusão no primeiro grafico mostrando visualmente os erros e acertos do modelo
     cm = confusion_matrix(y_test, y_pred)
     sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", ax=axes[0])
     axes[0].set_title('Matriz de confusão')
     axes[0].set_xlabel('Predito')
     axes[0].set_ylabel('Real')

     # desenhar a Curva Roc no segundo grafico para avaliar a capacidade do modelo em discirminar entre classes ao longo de variados limiares de decisão - ou seja, estamos medindo o quão bom nosso modelo é

     # ROC: significa -> Receiver Operating Characteristic 
     fpr, tpr, _ = roc_curve(y_test, y_proba)
     axes[1].plot(fpr, tpr, label=f'ROC Curve(AUC = {roc_auc: .3f})', color='darkorange')

     axes[1].plot([0, 1], [0, 1], color='navy', linestyle='--')
     axes[1].set_title('Curva ROC - Validação de crédito')
     axes[1].set_xlabel('Taxa de Falso Positivo')
     axes[1].set_ylabel('Taxa de Verdadeiro Positivo')
     axes[1].legend()

     # agora, precisamos ajustar os espaços do grafico; salvar as imagens geradas em alta resolução; me fechar a figura para liberar memoria
     plt.tight_layout()
     plt.savefig(pasta_ml_output / 'desempenho_modelo.jpg', dpi=300)

     # 2.11.1. Consolidação 
     # adicionar ao DataFrame original duas novas colunas de previsão e probabilidade geradas pelo modelo
     df['Previsao_Aprovacao'] = model_pipeline.predict(x)
     df['Probabilidade_Aprovacao'] = model_pipeline.predict_proba(x)[:, 1].round(4)

     # retornar o modelo treinado, o dicionario de metricas e a base completa com as previsões gravadas
     metrics = {'roc_auc': roc_auc, 'report': report}
     return model_pipeline, metrics, df
