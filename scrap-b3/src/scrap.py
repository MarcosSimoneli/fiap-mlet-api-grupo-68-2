import requests
import pandas as pd
from io import StringIO
import base64

# URL do website B3
url = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetDownloadPortfolioDay/eyJpbmRleCI6IklCT1YiLCJsYW5ndWFnZSI6InB0LWJyIn0='

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:

    # Lendo o conteúdo do CSV
    content = response.content.decode('utf-8')

    # Decodificando o conteúdo base64
    csv = base64.b64decode(content)
    csv_text = csv.decode('latin1')  # Usando 'latin1' para decodificar corretamente os caracteres especiais
    csv_text = '\n'.join(csv_text.split('\n')[2:])

    # Convertendo o conteúdo do CSV para um DataFrame do pandas
    data = pd.read_csv(StringIO(csv_text), delimiter=';') 

else:
    print(f'Falha na requisição. Status code: {response.status_code}')
