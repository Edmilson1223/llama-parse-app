import streamlit as st
import os
from pathlib import Path
from llama_parse import LlamaParse
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="LlamaParse PDF Converter",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'parser' not in st.session_state:
    st.session_state.parser = None
if 'processing_log' not in st.session_state:
    st.session_state.processing_log = []

def get_parser():
    """Initialize LlamaParse with API key from sidebar"""
    api_key = st.session_state.get('api_key')
    if not api_key:
        return None
    
    return LlamaParse(
        api_key=api_key,
        result_type="markdown",
        extract_charts=True,
        auto_mode=True,
        auto_mode_trigger_on_image_in_page=True,
        auto_mode_trigger_on_table_in_page=True,
    )

def ensure_folders():
    """Ensure necessary folders exist"""
    Path("docs").mkdir(exist_ok=True)
    Path("outputs").mkdir(exist_ok=True)

def get_processed_files():
    """Get list of already processed markdown files"""
    outputs_folder = "outputs"
    if os.path.exists(outputs_folder):
        return set(os.listdir(outputs_folder))
    return set()

def get_unprocessed_files():
    """Get list of PDF files that haven't been processed yet"""
    ensure_folders()
    docs_folder = "docs"
    pdf_files = [f for f in os.listdir(docs_folder) if f.endswith('.pdf')]
    processed = get_processed_files()
    
    unprocessed = []
    for pdf_file in pdf_files:
        output_file = pdf_file.replace('.pdf', '.md')
        if output_file not in processed:
            unprocessed.append(pdf_file)
    
    return unprocessed

def process_pdf(file_path, output_path, parser):
    """Process a single PDF file"""
    try:
        with open(file_path, "rb") as f:
            extra_info = {"file_name": file_path}
            documents = parser.load_data(f, extra_info=extra_info)
        
        # Write to markdown file
        with open(output_path, "w", encoding="utf-8") as f:
            for doc in documents:
                f.write(doc.text)
        
        return True, "Processado com sucesso"
    except Exception as e:
        return False, str(e)

# Header
st.title("📄 LlamaParse PDF Converter")
st.markdown("Converta seus PDFs em Markdown usando IA avançada")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configurações")
    
    # Tentar obter API key de st.secrets (produção) ou input (desenvolvimento)
    try:
        default_api_key = st.secrets["LLAMA_PARSE_API_KEY"]
    except:
        default_api_key = ""
    
    api_key = st.text_input(
        "API Key LlamaParse",
        value=default_api_key,
        type="password",
        help="Insira sua chave API do LlamaParse (ou configure em Secrets)"
    )
    st.session_state.api_key = api_key
    
    st.markdown("---")
    
    st.markdown("""
    ### 📖 Sobre
    - **Processamento**: Extrai texto, tabelas e gráficos de PDFs
    - **Formato Saída**: Markdown (.md)
    - **Auto Mode**: Ativado para melhor detecção
    """)

# Main tabs
tab1, tab2, tab3 = st.tabs(["📤 Upload & Processar", "📊 Gerenciar Arquivos", "📥 Downloads"])

# ===== TAB 1: Upload & Process =====
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Fazer Upload de PDFs")
        
        uploaded_files = st.file_uploader(
            "Selecione um ou mais arquivos PDF para processar",
            type="pdf",
            accept_multiple_files=True,
            help="Você pode enviar um ou vários arquivos de uma vez"
        )
        
        if uploaded_files:
            ensure_folders()
            st.markdown(f"**{len(uploaded_files)} arquivo(s) selecionado(s)**")
            
            if st.button("🚀 Processar Arquivos", key="process_upload"):
                parser = get_parser()
                
                if not parser:
                    st.error("❌ Erro: API Key não configurada!")
                else:
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    results_container = st.container()
                    
                    successful = 0
                    failed = 0
                    
                    for idx, uploaded_file in enumerate(uploaded_files):
                        # Update progress
                        progress = (idx + 1) / len(uploaded_files)
                        progress_bar.progress(progress)
                        status_text.text(f"Processando {idx + 1}/{len(uploaded_files)}: {uploaded_file.name}")
                        
                        try:
                            # Save uploaded file to docs folder
                            docs_folder = "docs"
                            file_path = os.path.join(docs_folder, uploaded_file.name)
                            
                            with open(file_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            
                            # Process the file
                            output_file = uploaded_file.name.replace('.pdf', '.md')
                            output_path = os.path.join("outputs", output_file)
                            
                            success, message = process_pdf(file_path, output_path, parser)
                            
                            if success:
                                with results_container.container():
                                    st.markdown(f'<div class="success-box">✓ <b>{uploaded_file.name}</b> → salvo como {output_file}</div>', unsafe_allow_html=True)
                                successful += 1
                            else:
                                with results_container.container():
                                    st.markdown(f'<div class="error-box">✗ Erro ao processar <b>{uploaded_file.name}</b>: {message}</div>', unsafe_allow_html=True)
                                failed += 1
                        
                        except Exception as e:
                            with results_container.container():
                                st.markdown(f'<div class="error-box">✗ Erro ao processar <b>{uploaded_file.name}</b>: {str(e)}</div>', unsafe_allow_html=True)
                            failed += 1
                    
                    status_text.empty()
                    progress_bar.empty()
                    
                    st.markdown("---")
                    col_success, col_failed = st.columns(2)
                    with col_success:
                        st.metric("✅ Sucesso", successful)
                    with col_failed:
                        st.metric("❌ Falhas", failed)
    
    with col2:
        st.subheader("📈 Status")
        ensure_folders()
        
        unprocessed = get_unprocessed_files()
        processed = get_processed_files()
        
        st.metric("Processados", len(processed))
        st.metric("Pendentes", len(unprocessed))
        
        if unprocessed:
            st.write("**Pendentes:**")
            for file in unprocessed[:5]:
                st.write(f"• {file}")
            if len(unprocessed) > 5:
                st.write(f"... e mais {len(unprocessed) - 5}")

# ===== TAB 2: Manage Files =====
with tab2:
    ensure_folders()
    
    docs_folder = "docs"
    outputs_folder = "outputs"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📂 PDFs na Pasta docs/")
        pdf_files = [f for f in os.listdir(docs_folder) if f.endswith('.pdf')]
        processed = get_processed_files()
        
        if pdf_files:
            for pdf_file in pdf_files:
                output_file = pdf_file.replace('.pdf', '.md')
                is_processed = output_file in processed
                
                col_name, col_status = st.columns([4, 1])
                with col_name:
                    st.write(f"📄 {pdf_file}")
                with col_status:
                    if is_processed:
                        st.write("✅")
                    else:
                        status = st.empty()
        else:
            st.info("Nenhum PDF encontrado na pasta docs/")
    
    with col2:
        st.subheader("📝 Markdown Processados")
        
        if processed:
            for output_file in sorted(processed):
                output_path = os.path.join(outputs_folder, output_file)
                file_size = os.path.getsize(output_path) / 1024  # KB
                
                col_name, col_size = st.columns([4, 1])
                with col_name:
                    st.write(f"📝 {output_file}")
                with col_size:
                    st.caption(f"{file_size:.1f} KB")
        else:
            st.info("Nenhum arquivo processado ainda")
    
    # Delete processed files
    st.markdown("---")
    st.subheader("🗑️ Deletar Arquivos Processados")
    
    if processed:
        files_to_delete = st.multiselect(
            "Selecione arquivos para deletar:",
            sorted(processed),
            help="Selecione os arquivos .md que deseja remover"
        )
        
        if files_to_delete and st.button("🗑️ Confirmar Deleção"):
            for file in files_to_delete:
                file_path = os.path.join(outputs_folder, file)
                try:
                    os.remove(file_path)
                    st.success(f"✓ Deletado: {file}")
                except Exception as e:
                    st.error(f"❌ Erro ao deletar {file}: {str(e)}")
            st.rerun()

# ===== TAB 3: Downloads =====
with tab3:
    st.subheader("📥 Baixar Arquivos Processados")
    
    ensure_folders()
    outputs_folder = "outputs"
    processed = get_processed_files()
    
    if processed:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Arquivos disponíveis:**")
            selected_file = st.selectbox(
                "Selecione um arquivo:",
                sorted(processed),
                label_visibility="collapsed"
            )
            
            if selected_file:
                file_path = os.path.join(outputs_folder, selected_file)
                
                with open(file_path, "rb") as f:
                    file_content = f.read()
                
                st.download_button(
                    label=f"📥 Baixar {selected_file}",
                    data=file_content,
                    file_name=selected_file,
                    mime="text/markdown",
                    use_container_width=True,
                    key=f"download_{selected_file}"
                )
                
                # Show preview
                st.markdown("**📋 Pré-visualização:**")
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                st.markdown(content[:2000] + "..." if len(content) > 2000 else content)
        
        with col2:
            st.markdown("**Informações:**")
            
            for file in sorted(processed):
                file_path = os.path.join(outputs_folder, file)
                file_size = os.path.getsize(file_path) / 1024
                file_mtime = os.path.getmtime(file_path)
                file_date = datetime.fromtimestamp(file_mtime).strftime("%d/%m/%Y %H:%M")
                
                st.write(f"""
                **{file}**
                - Tamanho: {file_size:.1f} KB
                - Data: {file_date}
                """)
    else:
        st.info("Nenhum arquivo para baixar. Processe alguns PDFs primeiro!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    🔧 Powered by LlamaParse | Streamlit
</div>
""", unsafe_allow_html=True)
