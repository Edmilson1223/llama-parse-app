#!/bin/bash
# Startup script para a aplicação LlamaParse Streamlit
# Este script verifica as dependências e inicia a aplicação

echo ""
echo "========================================"
echo "LlamaParse PDF Converter - Startup"
echo "========================================"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Erro: Python 3 não encontrado!"
    echo "Por favor, instale Python 3.8+ de https://www.python.org/"
    exit 1
fi

echo "✓ Python encontrado"
python3 --version

# Verifica e instala dependências
echo ""
echo "Verificando dependências..."
pip install -r requirements.txt

echo ""
echo "✓ Dependências instaladas com sucesso!"

# Inicia a aplicação
echo ""
echo "========================================"
echo "Iniciando aplicação Streamlit..."
echo "========================================"
echo ""
echo "🌐 A aplicação abrirá em: http://localhost:8501"
echo ""
echo "Pressione Ctrl+C para parar a aplicação"
echo ""

streamlit run app.py
