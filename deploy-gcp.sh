#!/bin/bash
# Script de Deploy para Google Cloud Run

set -e

echo "==================================="
echo "🚀 Deploy Script para Google Cloud"
echo "==================================="

# Verificar se gcloud CLI está instalado
if ! command -v gcloud &> /dev/null; then
    echo "❌ Google Cloud SDK não encontrado!"
    echo "📥 Instale em: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

echo ""
echo "✓ Google Cloud SDK encontrado"

# Fazer login
echo ""
echo "🔐 Fazendo login na Google Cloud..."
gcloud auth login

# Configurar projeto
echo ""
read -p "🆔 Google Cloud Project ID: " PROJECT_ID
gcloud config set project "$PROJECT_ID"

# Configurar aplicação
echo ""
read -p "🏷️  Nome da aplicação (padrão: llama-parse-app): " APP_NAME
APP_NAME=${APP_NAME:-llama-parse-app}

read -p "🌍 Região (padrão: us-central1): " REGION
REGION=${REGION:-us-central1}

# Build e Push para Container Registry
echo ""
echo "🐳 Buildando image Docker..."
gcloud builds submit --tag gcr.io/$PROJECT_ID/$APP_NAME

# Deploy para Cloud Run
echo ""
echo "📤 Fazendo deploy para Cloud Run..."

read -p "🔑 LLAMA_PARSE_API_KEY: " API_KEY

gcloud run deploy "$APP_NAME" \
  --image gcr.io/$PROJECT_ID/$APP_NAME \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars LLAMA_PARSE_API_KEY="$API_KEY" \
  --memory 1Gi \
  --cpu 1 \
  --timeout 3600

echo ""
echo "✅ Deploy concluído com sucesso!"
echo "🌐 Acesse a URL fornecida acima"
