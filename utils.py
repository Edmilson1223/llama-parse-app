"""
Funções utilitárias para a aplicação LlamaParse
"""

import os
from pathlib import Path
from llama_parse import LlamaParse
from config import DOCS_FOLDER, OUTPUTS_FOLDER, LLAMA_PARSE_CONFIG


def ensure_folders():
    """Garante que as pastas docs e outputs existem"""
    Path(DOCS_FOLDER).mkdir(exist_ok=True)
    Path(OUTPUTS_FOLDER).mkdir(exist_ok=True)


def get_parser(api_key: str) -> LlamaParse:
    """
    Instancia o parser LlamaParse com a API key fornecida
    
    Args:
        api_key: Chave API do LlamaParse
        
    Returns:
        Instância do LlamaParse
    """
    if not api_key:
        raise ValueError("API Key não fornecida")
    
    return LlamaParse(api_key=api_key, **LLAMA_PARSE_CONFIG)


def get_pdf_files() -> list:
    """Retorna lista de arquivos PDF na pasta docs"""
    ensure_folders()
    docs_folder = DOCS_FOLDER
    return [f for f in os.listdir(docs_folder) if f.endswith('.pdf')]


def get_processed_files() -> set:
    """Retorna conjunto de arquivos já processados"""
    ensure_folders()
    if os.path.exists(OUTPUTS_FOLDER):
        return set(os.listdir(OUTPUTS_FOLDER))
    return set()


def get_unprocessed_files() -> list:
    """Retorna lista de PDFs que ainda não foram processados"""
    ensure_folders()
    pdf_files = get_pdf_files()
    processed = get_processed_files()
    
    unprocessed = []
    for pdf_file in pdf_files:
        output_file = pdf_file.replace('.pdf', '.md')
        if output_file not in processed:
            unprocessed.append(pdf_file)
    
    return unprocessed


def process_pdf(file_path: str, output_path: str, parser: LlamaParse) -> tuple:
    """
    Processa um arquivo PDF e salva como Markdown
    
    Args:
        file_path: Caminho do arquivo PDF
        output_path: Caminho de saída do arquivo Markdown
        parser: Instância do LlamaParse
        
    Returns:
        Tupla (sucesso: bool, mensagem: str)
    """
    try:
        with open(file_path, "rb") as f:
            extra_info = {"file_name": file_path}
            documents = parser.load_data(f, extra_info=extra_info)
        
        # Escreve arquivo markdown
        with open(output_path, "w", encoding="utf-8") as f:
            for doc in documents:
                f.write(doc.text)
        
        return True, "Processado com sucesso"
    
    except Exception as e:
        return False, str(e)


def delete_file(file_path: str) -> tuple:
    """
    Deleta um arquivo
    
    Args:
        file_path: Caminho do arquivo a deletar
        
    Returns:
        Tupla (sucesso: bool, mensagem: str)
    """
    try:
        os.remove(file_path)
        return True, "Arquivo removido com sucesso"
    except Exception as e:
        return False, str(e)


def get_file_size_kb(file_path: str) -> float:
    """Retorna tamanho do arquivo em KB"""
    try:
        return os.path.getsize(file_path) / 1024
    except:
        return 0


def get_file_info(file_path: str) -> dict:
    """Retorna informações do arquivo"""
    import os.path
    from datetime import datetime
    
    try:
        stat = os.stat(file_path)
        return {
            "size_kb": stat.st_size / 1024,
            "size_bytes": stat.st_size,
            "created": datetime.fromtimestamp(stat.st_ctime).strftime("%d/%m/%Y %H:%M"),
            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M"),
            "exists": True
        }
    except:
        return {"exists": False}


def read_file_content(file_path: str, max_chars: int = None) -> str:
    """
    Lê conteúdo de um arquivo
    
    Args:
        file_path: Caminho do arquivo
        max_chars: Número máximo de caracteres a ler (None = tudo)
        
    Returns:
        Conteúdo do arquivo
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if max_chars and len(content) > max_chars:
            return content[:max_chars]
        
        return content
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"


def validate_api_key(api_key: str) -> bool:
    """Valida se a API key tem o formato correto"""
    if not api_key:
        return False
    return api_key.startswith("llx-") and len(api_key) > 10


def get_statistics() -> dict:
    """Retorna estatísticas da aplicação"""
    ensure_folders()
    pdf_files = get_pdf_files()
    processed = get_processed_files()
    
    return {
        "total_pdfs": len(pdf_files),
        "processed": len(processed),
        "unprocessed": len(pdf_files) - len(processed),
        "processing_percentage": (len(processed) / len(pdf_files) * 100) if pdf_files else 0
    }
