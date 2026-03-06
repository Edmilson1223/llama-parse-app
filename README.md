# 📄 LlamaParse PDF Converter

Aplicação Streamlit para converter PDFs em Markdown usando IA com **LlamaParse**.

## ✨ Características

- ✅ Upload de múltiplos PDFs
- ✅ Processamento com IA (texto, tabelas, gráficos)
- ✅ Conversão para Markdown
- ✅ Gestão de ficheiros (lista, elimina, descarrega)
- ✅ Interface intuitiva com Streamlit

## 🚀 Quick Start Local

```bash
# Clone o repositório
git clone https://github.com/Edmilson1223/llama-parse-app.git
cd llama-parse-app

# Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Configure chave API (crie ficheiro .env)
# LLAMA_PARSE_API_KEY=sua_chave_aqui

# Execute
streamlit run app.py
```

Aceda em: `http://localhost:8501`

## 🌐 Deploy em Railway

1. **Crie conta em** https://railway.app
2. **Conecte seu repositório GitHub**
3. **Adicione variável de ambiente:**
   - Key: `LLAMA_PARSE_API_KEY`
   - Value: sua chave LlamaParse
4. **Deploy automático** ao fazer push no `main`

## 📁 Estrutura

```
.
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências
├── railway.toml        # Config Railway
└── .streamlit/
    └── config.toml     # Config Streamlit
```

## 📖 Como Usar

**Aba 1 - Upload & Processar:**
- Selecione um ou mais PDFs
- Clique em "🚀 Processar Arquivos"
- Veja o progresso em tempo real

**Aba 2 - Gerenciar Arquivos:**
- Liste PDFs e Markdown processados
- Elimine ficheiros desnecessários

**Aba 3 - Downloads:**
- Selecione ficheiro Markdown
- Download e pré-visualização

## 🔐 Configuração da Chave API

**Local (ficheiro `.env`):**
```
LLAMA_PARSE_API_KEY=llx-sua_chave_aqui
```

**Railway (Variables):**
1. Aceda ao projeto em railway.app
2. Clique em "Variables"
3. Adicione `LLAMA_PARSE_API_KEY` = sua chave
4. Deploy

## 🐛 Troubleshooting

| Erro | Solução |
|------|---------|
| "API Key não configurada" | Verifique variável de ambiente `LLAMA_PARSE_API_KEY` |
| "Ficheiro vazio" | Re-faça upload do PDF |
| Erro ao processar | Verifique se PDF está em formato válido (máx 200 MB) |

## 🛠️ Tecnologias

- Streamlit 1.28.1
- LlamaParse 0.5.20
- Python 3.11+

## 📚 Recursos

- [Streamlit Docs](https://docs.streamlit.io)
- [LlamaParse API](https://docs.llamaindex.ai)
- [Railway Docs](https://docs.railway.app)

## 👤 Autor

Edmilson Barbosa - [@Edmilson1223](https://github.com/Edmilson1223)

## 📄 Licença

MIT License
