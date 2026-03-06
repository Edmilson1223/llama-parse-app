@echo off
REM Startup script para a aplicação LlamaParse Streamlit
REM Este script verifica as dependências e inicia a aplicação

echo.
echo ========================================
echo LlamaParse PDF Converter - Startup
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Erro: Python não encontrado!
    echo Por favor, instale Python 3.8+ de https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python encontrado

REM Verifica e instala dependências
echo.
echo Verificando dependências...
pip install -r requirements.txt

echo.
echo ✓ Dependências instaladas com sucesso!

REM Inicia a aplicação
echo.
echo ========================================
echo Iniciando aplicação Streamlit...
echo ========================================
echo.
echo 🌐 A aplicação abrirá em: http://localhost:8501
echo.
echo Pressione Ctrl+C para parar a aplicação
echo.

streamlit run app.py
