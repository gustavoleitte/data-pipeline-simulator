from scripts import extract, transform, load

def main():
    print("🚀 Iniciando pipeline ETL...")

    # Extração
    df_raw = extract.run()

    # Transformação
    df_transformed = transform.run(df_raw)

    # Carregamento
    load.run(df_transformed)

    print("✅ Pipeline executada com sucesso!")

if __name__ == "__main__":
    main()

