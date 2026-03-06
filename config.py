"""
Configurações da aplicação LlamaParse Streamlit
"""

import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# ===== CONFIGURAÇÕES DE DIRETÓRIOS =====
DOCS_FOLDER = "docs"
OUTPUTS_FOLDER = "outputs"

# ===== CONFIGURAÇÕES LLAMA PARSE =====
LLAMA_PARSE_API_KEY = os.getenv(
    "LLAMA_PARSE_API_KEY",
    "llx-5Fq2oMo4Q43L6W69bCq5EEMxn57FT573OHfnVjhNF527N6us"
)

LLAMA_PARSE_CONFIG = {
    "result_type": "markdown",
    "extract_charts": True,
    "extract_tables": True,
    "auto_mode": True,
    "auto_mode_trigger_on_image_in_page": True,
    "auto_mode_trigger_on_table_in_page": True,
}

# ===== CONFIGURAÇÕES STREAMLIT =====
PAGE_TITLE = "LlamaParse PDF Converter"
PAGE_ICON = "📄"
LAYOUT = "wide"

# ===== CONFIGURAÇÕES DE UPLOAD =====
MAX_UPLOAD_SIZE_MB = 100  # Tamanho máximo de arquivo para upload
ALLOWED_FILE_TYPES = ["pdf"]

# ===== CONFIGURAÇÕES DE INTERFACE =====
SHOW_FOOTER = True
ENABLE_DARK_MODE = True

# ===== CONFIGURAÇÕES DE CACHE =====
CACHE_PROCESSED_FILES = True

# ===== MENSAGENS =====
MESSAGES = {
    "success": "✅ Processado com sucesso",
    "error": "❌ Erro ao processar",
    "empty": "📭 Nenhum arquivo encontrado",
    "processing": "⏳ Processando...",
    "completed": "✅ Processamento concluído",
}
