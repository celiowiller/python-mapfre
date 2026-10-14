# AQUI, VAMOS IMPLEMENTAR AS CONFIGURAÇÕES GLOBAIS E PATHS - CAMINHOS DE PASTA E ARQUIVOS - DO PROJETO. ESTE ARQUIVO É UM "PEDAÇO" DA AUTOMAÇÃO E GERENCIAMENTO DA CRIAÇÃO E MANUTENÇÃO DE PASTAS E ARQUIVOS DO PROJETO

# 1. importar os recursos necessarios
import os # recurso que auxiliará na manipulação de elementos que pertencem, naturalmente, ao sistema operacional - SO; irá nos auxiliar na manipulação de pastas e arquivos

from pathlib import Path # auxilia na manipulação dos "caminhos" entre pastas e arquivos do projeto.

# 2. definir os diretorios/folders- base 
BASE_DIR = Path(__file__).resolve().parent
'''
__file__= aqui, estamos "pegando" o caminho do arquivo Python atual que está sendo executado
.resolve(): aqui, estamos convertendo esse caminho obtido num caminho ABSOLUTO(completo desde a raiz até o sistema)
.parent: aqui, estamos obtendo a pasta/folder "pai" o o arquivo será salvo.

Resumindo: estamos, basicamente, atribuindo como valor da variavel o caminho completo para a pasta raiz do nosso projeto
'''
DATA_RAW_DIR = BASE_DIR / "data" / "raw" # cria, para nos, o caminho para a pasta de dados brutos - data/raw - o operador / da classe Path junta os nomes para formar o caminho final, ex.: C:/pipeline_analise_completo/data/raw

DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed" # cria, para nos, o caminho para a pasta de dados processados pelo pipeline; o operador / da classe Path junta os nomes para formar o caminho final, ex.: C:/pipeline_analise_completo/data/processed


OUTPUT_DIR = BASE_DIR / "output" / "relatorios"  # cria, para nos, o caminho para a pasta de resultados obtidos pelo pipeline; o operador / da classe Path junta os nomes para formar o caminho final, ex.: C:/pipeline_analise_completo/data/output/relatorios

# 3. agora, vamos implementar as instruções de automação da criação destes recursos
# uma estrutura de repetição que irá percorrer, um por um, dos 3 elementos de diretoriso definidos nas linhas anteriores 
for diretorio in [DATA_RAW_DIR, DATA_PROCESSED_DIR, OUTPUT_DIR]:
    # aqui, a função makedirs() cria a pasta especificada na variavel iteradora - diretorio.
    os.makedirs(diretorio, exist_ok=True) # exist_ok: este parametro evita qeu o pipeline gere um erro, caso a pasta ja exista.


# -------------------------------------------------------------
# Agora, precisamos indicar, aqui, as constantes de regras de negocio de tributação 
ALIQUOTA_IMPOSTO = 0.06 # aqui, definimos uma constante para a aliquota de 6% sobre movimentação financeira

TAXA_DE_JUROS = 0.12 # aqui, definimos uma constante para a aliquota de 12% AO ANO  




