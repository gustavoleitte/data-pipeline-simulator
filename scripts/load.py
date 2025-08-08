def run(df):
    print("💾 Salvando dados transformados...")

    try:
        df.to_csv("data/processed/dados_tratados.csv", index=False)
        print("✅ Dados salvos em 'data/processed/dados_tratados.csv'")
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("data/raw/dados.csv")
    df = df.dropna()
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]
    run(df)
