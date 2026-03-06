# 📄 LlamaParse PDF Converter

Uma aplicação web moderna construída com Streamlit para converter PDFs em Markdown usando IA avançada através da API LlamaParse.

## ✨ Funcionalidades

- **Upload de PDFs**: Faça upload de um ou vários arquivos PDF por vez
- **Processamento Inteligente**: 
  - Extração de texto
  - Detecção e extração de tabelas
  - Detecção e extração de gráficos
  - Modo automático com detecção de imagens
- **Gerenciamento de Arquivos**: Visualize, organize e delete arquivos processados
- **Downloads**: Baixe os arquivos Markdown processados com pré-visualização
- **Status em Tempo Real**: Acompanhe o progresso do processamento

## 🚀 Como Usar

### 1. Instalação de Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar API Key

Você precisa de uma chave API válida do LlamaParse:
1. Acesse [LlamaParse](https://www.llamaparse.com/)
2. Obtenha sua API key
3. A chave pode ser configurada na barra lateral da aplicação

### 3. Executar a Aplicação

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no seu navegador padrão em `http://localhost:8501`

## 📁 Estrutura de Pastas

```
TesteLama/
├── app.py                 # Aplicação principal Streamlit
├── parseteste.py          # Script original de processamento
├── requirements.txt       # Dependências Python
├── README.md              # Este arquivo
├── docs/                  # 📂 PDFs para processar
│   ├── doc1.pdf
│   ├── doc2.pdf
│   └── ...
└── outputs/               # 📝 Markdown processados
    ├── doc1.md
    ├── doc2.md
    └── ...
```

## 🎯 Abas da Aplicação

### 📤 Upload & Processar
- Faça upload de PDFs
- Acompanhe o progresso em tempo real
- Veja resultados imediatos (sucesso/falha)
- Dashboard com estatísticas

### 📊 Gerenciar Arquivos
- Liste todos os PDFs importados
- Veja status de processamento (✅/⏳)
- Visualize arquivos Markdown processados com tamanho
- Delete arquivos processados em lote

### 📥 Downloads
- Selecione e baixe arquivos Markdown
- Pré-visualização do conteúdo
- Informações de tamanho e data

## ⚙️ Configurações Avançadas

### Variáveis de Ambiente

Você pode usar um arquivo `.env` para armazenar sua API key de forma segura:

```
LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx
```

Modifique o código se desejar ler da variável de ambiente:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('LLAMA_PARSE_API_KEY')
```

### Customizar Processamento

Edite a função `get_parser()` em `app.py` para ajustar parâmetros:

```python
def get_parser():
    return LlamaParse(
        api_key=api_key,
        result_type="markdown",      # ou "text", "json"
        extract_charts=True,         # Extrair gráficos
        extract_tables=True,         # Extrair tabelas
        auto_mode=True,              # Modo automático
        auto_mode_trigger_on_image_in_page=True,
        auto_mode_trigger_on_table_in_page=True,
    )
```

## 🔧 Troubleshooting

### Erro: "API Key não configurada"
- Verifique se você inseriu a API key corretamente na barra lateral
- A chave deve começar com `llx-`

### Erro ao processar PDF
- Verifique se o PDF não está corrompido
- Tente processar um PDF de teste primeiro
- Aumente o tempo de timeout se o PDF for muito grande

### Pasta `outputs` não carrega
- Certifique-se de que a pasta existe (criada automaticamente)
- Verifique permissões de leitura/escrita

## 📊 Exemplo de Uso

1. **Primeiro Uso**:
   ```bash
   streamlit run app.py
   ```

2. **Na Aba "Upload & Processar"**:
   - Clique em "Browse files"
   - Selecione um ou vários PDFs
   - Configure a API key se necessário
   - Clique em "🚀 Processar Arquivos"

3. **Acompanhe**:
   - Veja a barra de progresso
   - Resultados aparecem em tempo real

4. **Download**:
   - Vá para a aba "📥 Downloads"
   - Selecione o arquivo
   - Clique no botão de download

## 🛠️ Personalização

### Mudar Cores do Tema

Edite as cores nos estilos CSS no início de `app.py`:

```python
st.markdown("""
    <style>
    .success-box {
        background-color: #d4edda;  /* Mude a cor aqui */
    }
    </style>
""", unsafe_allow_html=True)
```

### Adicionar Mais Abas

Modifique a seção de tabs:

```python
tab1, tab2, tab3, tab4 = st.tabs(["Tab 1", "Tab 2", "Tab 3", "Tab 4"])

with tab4:
    st.write("Seu conteúdo aqui")
```

## 📚 Recursos

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LlamaParse Documentation](https://www.llamaparse.com/docs)
- [Markdown Guide](https://www.markdownguide.org/)

## 📝 Licença

Este projeto usa a API LlamaParse. Verifique os termos de serviço em https://www.llamaparse.com/

## 🤝 Suporte

Para problemas ou dúvidas:
1. Verifique a documentação acima
2. Consulte os logs do Streamlit
3. Verifique a status da API LlamaParse

---

**Versão**: 1.0.0  
**Atualizado**: Março 2026  
**Desenvolvido com** ❤️ **Streamlit & LlamaParse**
