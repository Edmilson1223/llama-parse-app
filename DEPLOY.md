# 🚀 Guia de Deploy - LlamaParse Streamlit App

Escolha uma opção abaixo para fazer deploy da sua aplicação:

---

## 📊 Comparativa de Opções

| Plataforma | Custo | Facilidade | Setup | Melhor Para |
|-----------|-------|-----------|-------|-----------|
| **Streamlit Cloud** | Grátis | ⭐⭐⭐⭐⭐ | 5 min | Início rápido |
| **Heroku** | $7-50/mês | ⭐⭐⭐⭐ | 10 min | Protyping |
| **AWS** | $0-100+/mês | ⭐⭐⭐ | 20 min | Escalável |
| **Google Cloud** | $0-100+/mês | ⭐⭐⭐ | 20 min | Escalável |
| **Railway** | $5-20/mês | ⭐⭐⭐⭐ | 10 min | Alternativa Heroku |
| **VPS** | $5-20/mês | ⭐⭐⭐ | 30 min | Controle total |

---

## 🌟 OPÇÃO 1: Streamlit Cloud (RECOMENDADO - Mais Fácil)

### ✅ Pros:
- Grátis para uso público
- Deploy automático do GitHub
- Suporta secrets nativas
- Muito fácil

### ❌ Contras:
- Recursos limitados (RAM ~1GB)
- Sem banco de dados
- Sem processamento paralelo

### 📋 Passo a Passo:

#### 1️⃣ Preparar Repositório GitHub

```bash
# Inicializar Git (se não tiver)
git init
git add .
git commit -m "Initial commit"

# Criar repositório no GitHub
# https://github.com/new

# Fazer push
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-repo.git
git push -u origin main
```

#### 2️⃣ Criar Conta em Streamlit Cloud

1. Acesse https://streamlit.io/cloud
2. Clique "Sign up" com sua conta GitHub
3. Autorize a conexão

#### 3️⃣ Deploy a Aplicação

1. Clique "New app"
2. Conecte seu repositório GitHub
3. Selecione:
   - Repository: seu-usuario/seu-repo
   - Branch: main
   - File path: app.py

#### 4️⃣ Configurar Secrets

Na página da aplicação:
1. Clique ⚙️ **Settings** (canto superior direito)
2. Vá para **Secrets**
3. Adicione sua API key:
```
LLAMA_PARSE_API_KEY = "llx-xxxxxxxxxxxxx"
```

#### 5️⃣ Acessar Aplicação

Sua app estará em:
```
https://seu-usuario-seu-repo-xxxxx.streamlit.app
```

### 📝 Arquivo Necessário: `.streamlit/secrets.toml`

Crie a pasta `.streamlit` com um arquivo `secrets.toml` localmente:

```bash
mkdir -p .streamlit
echo 'LLAMA_PARSE_API_KEY = "llx-xxxxxxxxxxxxx"' > .streamlit/secrets.toml
```

Acesse em `app.py`:
```python
import streamlit as st
api_key = st.secrets["LLAMA_PARSE_API_KEY"]
```

---

## 💜 OPÇÃO 2: Railway (Alternativa Moderno)

### ✅ Pros:
- Substitui bem o Heroku
- Grátis primeiros $5
- Fácil de usar
- Deploy automático

### ❌ Contras:
- Créditos limitados
- Começa a cobrar depois

### 📋 Passo a Passo:

#### 1️⃣ Preparar Repositório

```bash
git add .
git commit -m "Ready for Railway"
git push
```

#### 2️⃣ Criar Conta Railway

1. Acesse https://railway.app
2. Clique "Login with GitHub"
3. Autorize

#### 3️⃣ Deploy a Aplicação

1. Clique "New Project"
2. Clique "Deploy from GitHub repo"
3. Selecione seu repositório
4. Railway detectará automaticamente

#### 4️⃣ Configurar Variáveis de Ambiente

1. Vá para **Variables**
2. Adicione:
```
LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx
```

#### 5️⃣ Deploy Automático

Railroad fará deploy automaticamente do seu GitHub!

---

## ☁️ OPÇÃO 3: AWS (Para Escalabilidade)

### ✅ Pros:
- Muito escalável
- Muitos serviços disponíveis
- Camada grátis generosa (12 meses)

### ❌ Contras:
- Mais complexo de configurar
- Muitas opções (pode ser confuso)

### 📋 Passo a Passo usando Elastic Beanstalk:

#### 1️⃣ Preparar Aplicação

Crie arquivo `Procfile`:
```
web: streamlit run app.py --server.port=5000 --server.address=0.0.0.0
```

Crie arquivo `.ebignore`:
```
venv/
__pycache__/
*.pyc
.env
.git/
docs/*.pdf
outputs/*.md
```

#### 2️⃣ Criar Conta AWS

1. Acesse https://aws.amazon.com
2. Crie conta e ative free tier

#### 3️⃣ Instalar EB CLI

```bash
pip install awsebcli
```

#### 4️⃣ Deploy

```bash
# Autenticar
eb init -p python-3.11 llama-parse --region us-east-1 --interactive

# Criar ambiente
eb create production

# Deploy
eb deploy

# Abrir no navegador
eb open
```

#### 5️⃣ Configurar Variáveis

```bash
eb setenv LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx
```

---

## 🔷 OPÇÃO 4: Google Cloud Run

### ✅ Pros:
- Muito barato
- Serverless
- Grátis (até limites)

### ❌ Contras:
- Cold starts (demora um pouco na primeira requisição)
- Pode ser mais caro se uso for alto

### 📋 Passo a Passo:

#### 1️⃣ Preparar Dockerfile

Já temos! (`Dockerfile` já existe no projeto)

#### 2️⃣ Criar Conta Google Cloud

1. Acesse https://cloud.google.com
2. Crie projeto
3. Ative Cloud Run API

#### 3️⃣ Instalar CLI

```bash
# Windows
# Baixe em https://cloud.google.com/sdk/docs/install-sdk

# Linux/Mac
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

#### 4️⃣ Deploy

```bash
# Autenticar
gcloud auth login

# Deploy
gcloud run deploy llama-parse-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx

# Sua URL aparecerá no output!
```

---

## 🏠 OPÇÃO 5: VPS Próprio (DigitalOcean, Linode, Vultr)

### ✅ Pros:
- Controle total
- Preço fixo ($5-20/mês)
- Sem limites de recursos

### ❌ Contras:
- Precisa administrar servidor
- Mantém rodando 24/7
- Mais técnico

### 📋 Passo a Passo DigitalOcean:

#### 1️⃣ Criar Droplet

1. Acesse https://digitalocean.com
2. Crie conta
3. Clique "Create" → "Droplets"
4. Escolha:
   - Image: Ubuntu 22.04 LTS
   - Size: $5/mês é suficiente
   - Region: Escolha próxima de você
   - SSH key: Crie uma nova

#### 2️⃣ Conectar ao Servidor

```bash
# Windows: Use PuTTY ou WSL
ssh root@seu-ip-do-droplet

# Atualizar sistema
apt update && apt upgrade -y

# Instalar dependências
apt install -y python3 python3-pip python3-venv git
```

#### 3️⃣ Clonar e Configurar

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

#### 4️⃣ Configurar com Systemd

Crie arquivo `/etc/systemd/system/llama-parse.service`:

```ini
[Unit]
Description=LlamaParse Streamlit App
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/home/seu-usuario/seu-repo
Environment="LLAMA_PARSE_API_KEY=llx-xxxxxxxxxxxxx"
ExecStart=/home/seu-usuario/seu-repo/venv/bin/streamlit run app.py \
  --server.port=8501 \
  --server.address=0.0.0.0 \
  --server.headless=true
Restart=always

[Install]
WantedBy=multi-user.target
```

Ativar:
```bash
systemctl daemon-reload
systemctl enable llama-parse
systemctl start llama-parse
```

#### 5️⃣ Configurar Nginx (Proxy Reverso)

```bash
apt install -y nginx

# Criar config
cat > /etc/nginx/sites-available/llama-parse << EOF
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Ativar
ln -s /etc/nginx/sites-available/llama-parse /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

#### 6️⃣ SSL/HTTPS (Let's Encrypt)

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d seu-dominio.com
```

---

## 🐳 OPÇÃO 6: Docker com Composição em Produção

### Preparar para Produção

Crie arquivo `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  llama-parse-app:
    image: seu-usuario/llama-parse-app:latest
    container_name: llama-parse-prod
    ports:
      - "8501:8501"
    environment:
      - LLAMA_PARSE_API_KEY=${LLAMA_PARSE_API_KEY}
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    volumes:
      - ./docs:/app/docs
      - ./outputs:/app/outputs
      - ./streamlit_logs:/app/.streamlit
    restart: always
    networks:
      - prod-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

networks:
  prod-network:
    driver: bridge
```

Executar:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

## ✅ Checklist Pré-Deploy

- [ ] API key funciona localmente
- [ ] Arquivo requirements.txt está completo
- [ ] `.env` está em `.gitignore`
- [ ] `Dockerfile` está pronto
- [ ] Repositório Git está limpo
- [ ] Documentação atualizada
- [ ] Testes executados com sucesso
- [ ] README tem instruções de uso

---

## 🔐 Checklist de Segurança

- [ ] API keys em variáveis de ambiente (nunca hardcoded)
- [ ] `.env` arquivo não enviado para Git
- [ ] HTTPS/SSL ativado em produção
- [ ] Logs monitorados
- [ ] Acessos restritos se necessário
- [ ] Backups configurados

---

## 📊 Monitoramento em Produção

### Streamlit Cloud
Acesse dashboard da aplicação para ver logs

### AWS/GCP/Azure
Use CloudWatch/Logs nativas

### VPS
```bash
# Ver logs (systemd)
journalctl -u llama-parse -f

# Ver uso de resources
top
htop

# Ver portas abertas
netstat -tuln
```

---

## 🆘 Troubleshooting Comum

### Aplicação não inicia
```bash
# Verificar logs
docker logs llama-parse-prod

# Ou em VPS:
systemctl status llama-parse
journalctl -u llama-parse -n 50
```

### Erro: "Connection refused"
- Verifique se porta está aberta
- Verifique firewall
- Verifique se aplicação está rodando

### Erro: "API Key inválida"
- Verifique se variável está configurada
- Verifique se tem "llx-" no início
- Verifique se chave não expirou

### Lentidão
- Verifique CPU/RAM (comando `top`)
- Aumente recursos se possível
- Reduza timeout

---

## 🚀 Próximas Etapas

1. **Escolha plataforma** baseada no seu caso de uso
2. **Siga guia passo a passo** da opção escolhida
3. **Teste a aplicação** em produção
4. **Configure monitoramento** e alertas
5. **Configure backups** se necessário
6. **Estabeleça rotation de API keys** periodicamente

---

**Recomendação Final**: Comece com **Streamlit Cloud** para prototipagem, migre para **Railway ou DigitalOcean** quando precisar de mais controle.

Qual opção você gostaria de usar? Posso criar arquivos específicos para sua escolha! 🚀
