import pandas as pd

def run():
    try:
        print("📥 Extraindo dados do arquivo CSV...")
        df = pd.read_csv("data/raw/dados.csv")
        print("✅ Dados extraídos com sucesso!")
        return df
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o caminho.")
        return pd.DataFrame()
if __name__ == "__main__":
    df = run()
    print(df.head())

