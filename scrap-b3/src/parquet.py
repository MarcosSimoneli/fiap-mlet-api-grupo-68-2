import pandas as pd

def salvar_em_parquet(dataframe, nome_arquivo):
    """
    Salva um DataFrame em formato Parquet e retorna o caminho do arquivo.

    Parâmetros:
    dataframe (pd.DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): O nome do arquivo Parquet a ser gerado.

    Retorno:
    str: O caminho do arquivo Parquet gerado.
    """
    try:
        dataframe.to_parquet(nome_arquivo, engine="pyarrow", index=False)
        print(f"Arquivo Parquet '{nome_arquivo}' salvo com sucesso!")
        return nome_arquivo
    except Exception as e:
        print(f"Erro ao salvar o arquivo Parquet: {e}")
        return None