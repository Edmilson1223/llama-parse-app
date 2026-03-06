# 🚀 Guia: Publicar no GitHub

## Passo 1️⃣: Criar Novo Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `llama-parse-app` (ou qualquer outro nome)
   - **Description**: `Aplicação Streamlit para converter PDFs em Markdown com LlamaParse`
   - **Visibility**: Selecione "Public" (para Streamlit Cloud) ou "Private"
   - ✅ Deixe **desmarcado**: "Add a README file", "Add .gitignore", "Choose a license"
3. Clique "Create repository"
4. **Copie a URL**: Vai parecer `https://github.com/Edmilson1223/llama-parse-app.git`

---

## Passo 2️⃣: Configurar Git Localmente

### No PowerShell (seu projeto):

```powershell
cd c:\Users\edmil\Downloads\TesteLama

# 1. Configurar usuário Git
git config user.name "Edmilson1223"
git config user.email "seu-email@example.com"

# 2. Verificar configuração
git config --list

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer commit inicial
git commit -m "Aplicação Streamlit para LlamaParse - Inicial"

# 5. Renomear branch para main (se necessário)
git branch -M main

# 6. Adicionar remote (SUBSTITUA com sua URL)
git remote add origin https://github.com/Edmilson1223/llama-parse-app.git

# 7. Fazer push
git push -u origin main
```

---

## ⚠️ Autenticação GitHub (Importante!)

Se pedir senha, use um **Personal Access Token**:

1. Vá para: https://github.com/settings/tokens/new
2. Crie um token com permissões:
   - ✅ repo (full control)
   - ✅ workflow
3. Copie o token (aparece uma única vez!)
4. Cole quando pedir "Password"

### Ou Configure SSH (Melhor):

```powershell
# 1. Gerar chave SSH
ssh-keygen -t ed25519 -C "seu-email@example.com"
# Pressione Enter 2x (sem senha)

# 2. Copiar chave pública
cat $env:USERPROFILE\.ssh\id_ed25519.pub

# 3. Ir para: https://github.com/settings/ssh/new
# 4. Colar a chave como "New SSH key"

# 5. Testar conexão
ssh -T git@github.com
# Deve aparecer: "Hi Edmilson1223! You've successfully authenticated"

# 6. Mudar URL remota para SSH
git remote set-url origin git@github.com:Edmilson1223/llama-parse-app.git

# 7. Fazer push novamente
git push -u origin main
```

---

## ✅ Verificar se Funcionou

```powershell
# Ver status
git status
# Deve aparecer: "nothing to commit, working tree clean"

# Ver historico
git log
# Deve aparecer seu commit

# Ver remote
git remote -v
# Deve mostrar origin com sua URL
```

---

## 🎯 Próximo: Deploy no Streamlit Cloud

Depois que fizer push:

1. Acesse: https://streamlit.io/cloud
2. Clique "Sign up" com sua conta GitHub
3. Autorize o acesso aos repositórios
4. Clique "New app"
5. Selecione:
   - Repository: `Edmilson1223/llama-parse-app`
   - Branch: `main`
   - File path: `app.py`
6. Deploy automático!

---

## 🔗 Links Úteis

- [GitHub New Repo](https://github.com/new)
- [GitHub SSH Keys](https://github.com/settings/ssh/new)
- [GitHub Tokens](https://github.com/settings/tokens/new)
- [Streamlit Cloud](https://streamlit.io/cloud)

---

## ❓ Problemas Comuns

### Erro: "fatal: not a git repository"
✅ Solução: Você já está pronto! Apenas execute o passo 2

### Erro: "authentication failed"
✅ Solução: Use SSH em vez de HTTPS (ver seção acima)

### Erro: "No commits yet"
✅ Solução: Execute `git add .` e `git commit -m "Initial"` antes do push

### Repositório já existe
✅ Solução: Use um nome diferente, ou deleta o existente e cria novo

---

**Qualquer dúvida? Me avise!** 🚀
