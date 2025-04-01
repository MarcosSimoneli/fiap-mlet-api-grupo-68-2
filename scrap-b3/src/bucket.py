from datetime import datetime
import boto3

s3_client = boto3.client('s3')

def salvar_em_particao_diaria(nome_arquivo, diretorio_base):
    """
    Move um arquivo Parquet para uma partição diária organizada em pastas de ano, mês e dia.

    Parâmetros:
    nome_arquivo (str): Nome do arquivo Parquet a ser movido.
    diretorio_base (str): Diretório base onde as partições serão criadas.

    Retorno:
    str: Caminho completo do arquivo na partição diária.
    """
    try:
        # Obtendo a data atual
        data_atual = datetime.now()
        ano = data_atual.strftime('%Y')
        mes = data_atual.strftime('%m')
        dia = data_atual.strftime('%d')

        # Criando a estrutura de pastas
        bucket_name = "fiap-mlet-60-2025"  # Substitua pelo nome do seu bucket S3
        caminho_s3 = f"b3-data/{ano}/{mes}/{dia}/{nome_arquivo}"

        # Movendo o arquivo para a partição diária
        s3_client.upload_file(caminho_s3, bucket_name, caminho_s3)

        print(f"Arquivo salvo com sucesso no S3: s3://{bucket_name}/{caminho_s3}")
        return caminho_s3
    except Exception as e:
        print(f"Erro ao mover o arquivo para a partição diária: {e}")
        return None