import json
import uuid
from scrap import obter_dataframe_b3
from parquet import salvar_em_parquet
from bucket import salvar_em_particao_diaria

def lambda_handler(event, context):
    """
    Função Lambda que é acionada por um evento de agendamento (schedule event).
    Faz o download dos dados da B3, salva em formato Parquet e organiza em partições diárias.

    Parâmetros:
    event (dict): Evento recebido pelo Lambda (espera-se um schedule event).
    context (object): Contexto de execução do Lambda.

    Retorno:
    dict: Mensagem de sucesso ou erro.
    """
    try:
        # Obtendo o DataFrame da B3
        dataframe = obter_dataframe_b3()
        if dataframe is None:
            return {
                "statusCode": 500,
                "body": json.dumps("Erro ao obter os dados da B3.")
            }

        # Salvando o DataFrame em formato Parquet
        nome_arquivo_parquet = f"{uuid.uuid4()}.parquet"  # Diretório temporário no ambiente Lambda
        salvar_em_parquet(dataframe, nome_arquivo_parquet)

        # Movendo o arquivo Parquet para a partição diária
        diretorio_base = "./dados_parquet"  # Diretório base temporário
        caminho_final = salvar_em_particao_diaria(nome_arquivo_parquet, diretorio_base)

        return {
            "statusCode": 200,
            "body": json.dumps(f"Arquivo salvo com sucesso em: {caminho_final}")
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Erro ao processar o evento: {str(e)}")
        }