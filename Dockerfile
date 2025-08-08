# Etapa 1: usar imagem base do Python
FROM python:3.12-slim

# Etapa 2: definir a pasta de trabalho dentro do container
WORKDIR /app

# Etapa 3: copiar todos os arquivos do projeto para dentro do container
COPY . .

# Etapa 4: instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: definir o comando padrão quando o container for executado
CMD ["python", "pipeline.py"]
