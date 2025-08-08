def run(df):
    print("🔧 Transformando dados...")

    # 1. Remove linhas com valores nulos
    df = df.dropna()

    # 2. Padroniza nomes das colunas (minúsculas, sem espaços)
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

    print("✅ Transformação concluída!")
    return df

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("data/raw/dados.csv")
    df_transformado = run(df)
    print(df_transformado)
