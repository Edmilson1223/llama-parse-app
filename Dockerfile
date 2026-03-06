FROM python:3.10-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos do projeto
COPY requirements.txt .
COPY app.py .
COPY config.py .
COPY utils.py .
COPY parseteste.py .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Cria diretórios necessários
RUN mkdir -p docs outputs

# Expõe porta do Streamlit
EXPOSE 8501

# Variáveis de ambiente para Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_LOGGER_LEVEL=info

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "app.py"]
