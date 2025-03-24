import pandas as pd

# Exemplo de DataFrame
data = {
    "coluna1": [1, 2, 3],
    "coluna2": ["A", "B", "C"]
}
df = pd.DataFrame(data)

# Salvando o DataFrame como um arquivo Parquet
df.to_parquet("output.parquet", engine="pyarrow", index=False)

print("Arquivo Parquet salvo com sucesso!")