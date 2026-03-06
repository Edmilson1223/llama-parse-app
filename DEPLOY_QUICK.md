# 🚀 Deploy Rápido - Referência Rápida

## 🌟 Streamlit Cloud (Mais fácil - 5 min)

```bash
# 1. Push para GitHub
git push origin main

# 2. Ir para https://streamlit.io/cloud
# 3. Clique "New app", conecte repo, pronto!
```

**Dashboard Secrets**: ⚙️ Settings → Secrets → Adicione:
```
LLAMA_PARSE_API_KEY = "llx-xxxxxxxxxxxxx"
```

---

## 💜 Railway (Moderno - 5 min)

```bash
# Install
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

---

## ☁️ AWS (Escalável - 15 min)

```bash
pip install awsebcli

# Windows PowerShell:
bash deploy-aws.sh

# Ou manualmente:
eb init -p python-3.11 llama-parse --region us-east-1 --interactive
eb create production
eb deploy
eb setenv LLAMA_PARSE_API_KEY=seu-valor
eb open
```

---

## 🔷 Google Cloud (Serverless - 20 min)

```bash
# Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

bash deploy-gcp.sh

# Ou manualmente:
gcloud auth login
gcloud config set project SEU-PROJECT-ID
gcloud builds submit --tag gcr.io/SET-PROJECT/llama-parse-app
gcloud run deploy llama-parse-app \
  --image gcr.io/SEU-PROJECT/llama-parse-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars LLAMA_PARSE_API_KEY=seu-valor
```

---

## 🐳 Docker (Qualquer lugar - 10 min)

```bash
# Build
docker build -t llama-parse-app .

# Run
docker run -p 8501:8501 \
  -e LLAMA_PARSE_API_KEY=seu-valor \
  -v $(pwd)/docs:/app/docs \
  -v $(pwd)/outputs:/app/outputs \
  llama-parse-app

# Docker Compose
docker-compose up -d
```

---

## 🏠 VPS (DigitalOcean, Linode - 30 min)

```bash
# SSH
ssh root@seu-ip

# Setup
apt update && apt upgrade -y
apt install -y python3 python3-pip git nginx

# Clone
git clone seu-repo
cd seu-repo

# Venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create /etc/systemd/system/llama-parse.service:
[Unit]
Description=LlamaParse App
After=network.target

[Service]
User=www-data
WorkingDirectory=/home/seu-usuario/seu-repo
Environment="LLAMA_PARSE_API_KEY=llx-xxx"
ExecStart=/home/seu-usuario/seu-repo/venv/bin/streamlit run app.py \
  --server.port=8501 \
  --server.address=0.0.0.0 \
  --server.headless=true
Restart=always

[Install]
WantedBy=multi-user.target

# Enable
systemctl daemon-reload
systemctl enable llama-parse
systemctl start llama-parse

# Nginx proxy
cat > /etc/nginx/sites-available/llama-parse << EOF
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

ln -s /etc/nginx/sites-available/llama-parse /etc/nginx/sites-enabled/
nginx -t && systemctl restart nginx

# SSL (Let's Encrypt)
apt install -y certbot python3-certbot-nginx
certbot --nginx -d seu-dominio.com
```

---

## ✅ Checklist Antes de Deploy

- [ ] `requirements.txt` atualizado
- [ ] `.env` em `.gitignore`
- [ ] `app.py` testado localmente
- [ ] API key funciona
- [ ] `Dockerfile` existe
- [ ] Repository no GitHub
- [ ] README.md completo

---

## 📊 Qual Escolher?

| Caso | Opção | Razão |
|------|-------|-------|
| Prototipagem rápida | Streamlit Cloud | Grátis, fácil |
| Produção simples | Railway/Heroku | Barato, automático |
| Escalável | AWS/GCP | Muitos recursos |
| Controle total | VPS | Tudo customizável |
| Demo estável | DigitalOcean | $5/mês, confiável |

---

## 🔗 Links Úteis

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Railway](https://railway.app)
- [Heroku Alternative: Railway](https://docs.railway.app)
- [AWS EB](https://aws.amazon.com/elasticbeanstalk)
- [Google Cloud Run](https://cloud.google.com/run)
- [DigitalOcean](https://www.digitalocean.com)

---

## 📞 Suporte

Veja [DEPLOY.md](DEPLOY.md) para instruções detalhadas de cada opção.

**Dúvida? Ver:** `DEPLOY.md` ou `README.md`
