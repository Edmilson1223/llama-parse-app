# 🔐 Configuração de Secrets - Streamlit Cloud

## ⚠️ IMPORTANTE: Remova API Keys Hardcoded!

Sua API key **NÃO** deve estar no código. Já corrigimos isso!

---

## 🚀 Próximos Passos:

### 1️⃣ Commit e Push da Mudança

```bash
git add app.py
git commit -m "Security: Remove hardcoded API key, use st.secrets"
git push origin main
```

### 2️⃣ Configurar no Streamlit Cloud

1. Acesse seu app no Streamlit Cloud
2. Clique no menu **⋮** (canto superior direito)
3. Selecione **"Manage app"**
4. Vá para a aba **"Secrets"**
5. Cole isso no campo:
```
LLAMA_PARSE_API_KEY = "llx-xxxxxxxxxxxxx"
```
6. Salve (Ctrl+S ou clique Save)

### 3️⃣ Redeploye o App

1. Volte para sua app
2. No menu **⋮**, clique **"Rerun"** ou **"Redeploy"**
3. Aguarde 2-5 minutos

---

## ✅ Para Uso Local

Se quiser testar localmente com secrets:

### Opção A: Arquivo .streamlit/secrets.toml

```bash
# Windows PowerShell:
mkdir .streamlit -Force

# Copiar arquivo de exemplo
cp .streamlit\secrets.toml.example .streamlit\secrets.toml

# Editar com seu editor
notepad .streamlit\secrets.toml
```

Adicione:
```toml
LLAMA_PARSE_API_KEY = "llx-seu-valor-aqui"
```

### Opção B: Arquivo .env

```bash
# Instalar python-dotenv (já está em requirements.txt)
pip install python-dotenv

# Criar .env
echo 'LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx' > .env
```

Modifique `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

try:
    default_api_key = st.secrets["LLAMA_PARSE_API_KEY"]
except:
    default_api_key = os.getenv("LLAMA_PARSE_API_KEY", "")
```

---

## 🔒 Segurança

### ✅ Está Correto:
- [ ] API key em `st.secrets` (produção)
- [ ] API key em `.env` (local)
- [ ] `.env` em `.gitignore`
- [ ] `secrets.toml` em `.gitignore`

### ❌ Está Errado:
- [ ] API key no código
- [ ] API key em variável global
- [ ] API key em requirements.txt

---

## 🆘 Se Ainda Tiver Erro

### Verificar Requirements.txt

Certifique-se de que tem:
```
streamlit==1.28.1
llama-parse==0.1.1
python-dotenv==1.0.0
```

### Ver Logs no Streamlit Cloud

1. Clique **Manage app**
2. Role para baixo
3. Veja **"App logs"** ou **"Deployment logs"**
4. Procure por erros específicos

---

## 📋 Checklist Pós-Corrigir

- [ ] Removeu API key hardcoded do app.py
- [ ] Commitou e fez push
- [ ] Configurou secret no Streamlit Cloud
- [ ] Fez rerun/redeploy
- [ ] Testou a app

---

**Resultado esperado**: App carregará pedindo API key (ou pegará de st.secrets se configurado)

Qualquer erro ainda? Me avisa! 🚀
