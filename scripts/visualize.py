import pandas as pd
import matplotlib.pyplot as plt

def run():
    print("📊 Gerando gráfico...")

    df = pd.read_csv("data/processed/dados_tratados.csv")

    plt.figure(figsize=(8, 4))
    plt.bar(df["nome"], df["idade"], color='skyblue')
    plt.title("Idade por Nome")
    plt.xlabel("Nome")
    plt.ylabel("Idade")
    plt.tight_layout()

    # Salvar como imagem
    plt.savefig("data/processed/grafico_idades.png")
    print("✅ Gráfico salvo em 'data/processed/grafico_idades.png'")
if __name__ == "__main__":
    run()
