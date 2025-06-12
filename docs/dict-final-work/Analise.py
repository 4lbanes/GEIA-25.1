import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import unicodedata

"""
    Autor: Arthur Mourao
    Descrição: Nessa parte do codigo, sera padronizado o DataFrame que foi lido do arquivo CSV,
    e sera filtrada somente as colunas que desejaremos analizar
"""
#Pegando o DataFrame puro do arquivo CSV
raw_df = pd.read_csv("MICRODADOS_ENEM_2023.csv", encoding='latin1', sep=';')
#Colunas que serao analizadas
#As colunas que serao analisadas podem ser alteradas aqui
colunas_filtradas = ['TP_FAIXA_ETARIA','TP_SEXO','TP_ESTADO_CIVIL','TP_COR_RACA','TP_NACIONALIDADE','TP_ST_CONCLUSAO','TP_ANO_CONCLUIU','TP_ESCOLA']
#definindo o novo df "filtered_raw_df" como o dataframe puro "raw_df" filtrado pelas colunas que serao analisadas
filtered_raw_df = raw_df[colunas_filtradas]

def standardize(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Autor: Arthur Veras

    Descrição:
        Padroniza os nomes das colunas do DataFrame:
        - Converte para minúsculas
        - Substitui espaços por underscores (_)
        - Remove acentos e caracteres especiais

    Parâmetros:
        dataframe (pd.DataFrame): DataFrame cujas colunas serão padronizadas.

    Retorno:
        pd.DataFrame: DataFrame com os nomes das colunas padronizados.
    """
    def remove_accents(text: str) -> str:
        """
       Descrição:
          - Remove todos os acentos (diacríticos) de uma determinada string, convertendo caracteres
            como 'á', 'ç' ou 'ê' em seus equivalentes átonos 'a', 'c' e 'e'.

       Parâmetros:
            text (str): A string de entrada contendo caracteres acentuados.

    Retorna:
         str: Uma nova string com todos os acentos removidos, preservando apenas os caracteres base.
        """
        normalized_text = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in normalized_text if not unicodedata.combining(c)])

    new_columns = [
        remove_accents(columns).lower().replace(" ", "_")
        for columns in dataframe.columns
    ]
    dataframe.columns = new_columns

    return dataframe

standardized_dataframe = standardize(filtered_raw_df)
def analise_estatistica(df):
    """
        Autor: Arthur Mourao
        Descrição: Essa função sera responsavel para calcular os principais parametros estatisticos (como media, moda, desvio padrao, etc.) do DataFrame.
        Além de calcular os outliers pelo metodo Z-Score e pelo metodo Cerca de Tukey.
        Parâmetros:
            df: (Nesse caso o standardized_dataframe).
    """
    def mean(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula a média de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão a média calculada.
        """
        # O .to_string() é usado nesse caso para que nao apareca o tipo do dado no resultado, como "dtype: float64" por exemplo
        return df.mean(numeric_only=True).to_string()
    def median(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula a mediana de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão a mediana calculada.
        """
        return df.median(numeric_only=True).to_string()
    def mode(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula a moda de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão a moda calculada.
        """
        return df.mode(numeric_only=False).iloc[0].to_string()
    def std(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula o desvio padrão de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão o desvio padrão calculado.
        """
        return df.std(numeric_only=True).to_string()
    def variance(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula a variância de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão a variância calculada.
        """
        return df.var(numeric_only=True).to_string()
    def interval(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função mostra o intervalo de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão o intervalo mostrado.
        """
        valor_minimo = df.min(numeric_only=True)
        valor_maximo = df.max(numeric_only=True)
        return pd.DataFrame({'Mínimo': valor_minimo, 'Máximo': valor_maximo}).to_string()
    def z_score(df):
        """
        Autor: Arthur Mourao
        Descrição: Essa função calcula os outliers pelo metodo Z-Score de todas as colunas numéricas do DataFrame.
        Parâmetros:
            df (Nesse caso o standardized_dataframe): DataFrame cujas colunas numéricas terão os outliers detectados pelo Z-Score.
        """
        df_zscore = ((df - df.mean(numeric_only=True))/df.std(numeric_only=True))
        zscore_soma = (abs(df_zscore) > 3).sum().sum()
        return f"Foram encontrados um total de {zscore_soma} outliers pelo metodo Z-Score."
    def cerca_tukey(df):
        pass
    """
    Aqui sera retornado os resultados da analise estatistica do DataFrame calculado pelas funcoes anteriores.
    """
    return( f"\n -----------------Intervalos: -----------------\n{interval(df)}"
            f"\n -----------------Media: -----------------\n{mean(df)}"
            f"\n -----------------Mediana: -----------------\n{median(df)}"
            f"\n -----------------Moda: -----------------\n{mode(df)}"
            f"\n -----------------Desvio Padrao: -----------------\n{std(df)}"
            f"\n -----------------Variancia: -----------------\n{variance(df)}"
            f"\n -----------------Zscore: -----------------\n{z_score(df)}"
          )
# Exibindo a analise estatistica do DataFrame padronizado
print(analise_estatistica(standardized_dataframe))