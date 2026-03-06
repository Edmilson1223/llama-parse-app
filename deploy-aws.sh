#!/bin/bash
# Script de Deploy para AWS Elastic Beanstalk

set -e

echo "==================================="
echo "🚀 Deploy Script para AWS EB"
echo "==================================="

# Verificar se EB CLI está instalado
if ! command -v eb &> /dev/null; then
    echo "❌ EB CLI não encontrado!"
    echo "📥 Instale: pip install awsebcli"
    exit 1
fi

echo ""
echo "✓ EB CLI encontrado"

# Verificar versão do EB CLI
echo ""
eb --version

# Inicializar (se necessário)
if [ ! -d ".elasticbeanstalk" ]; then
    echo ""
    echo "🔧 Inicializando EB application..."
    
    read -p "🏷️  Nome da aplicação (padrão: llama-parse-app): " APP_NAME
    APP_NAME=${APP_NAME:-llama-parse-app}
    
    read -p "🌍 Região AWS (padrão: us-east-1): " REGION
    REGION=${REGION:-us-east-1}
    
    eb init -p python-3.11 "$APP_NAME" --region "$REGION" --interactive
fi

# Criar ou verificar ambiente
echo ""
echo "🌍 Configurando ambiente..."

if ! eb status &>/dev/null; then
    echo "📦 Criando novo ambiente..."
    
    read -p "🏷️  Nome do ambiente (padrão: production): " ENV_NAME
    ENV_NAME=${ENV_NAME:-production}
    
    eb create "$ENV_NAME"
else
    echo "✓ Ambiente já existe"
fi

# Fazer deploy
echo ""
echo "📤 Fazendo deploy..."
eb deploy

# Configurar variáveis de ambiente
echo ""
read -p "📝 Deseja configurar variáveis de ambiente? (s/n): " CONFIG_VARS

if [ "$CONFIG_VARS" = "s" ] || [ "$CONFIG_VARS" = "S" ]; then
    read -p "🔑 LLAMA_PARSE_API_KEY: " API_KEY
    eb setenv LLAMA_PARSE_API_KEY="$API_KEY"
fi

# Abrir aplicação
echo ""
read -p "🌐 Deseja abrir a aplicação no navegador? (s/n): " OPEN_APP

if [ "$OPEN_APP" = "s" ] || [ "$OPEN_APP" = "S" ]; then
    eb open
fi

echo ""
echo "✅ Deploy concluído com sucesso!"
