#!/bin/bash
# Script de Deploy para Railway.app

set -e

echo "==================================="
echo "🚀 Deploy Script para Railway.app"
echo "==================================="

# Verificar se railway CLI está instalado
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI não encontrado!"
    echo "📥 Instale em: https://docs.railway.app/guides/cli"
    exit 1
fi

echo ""
echo "✓ Railway CLI encontrado"

# Fazer login
echo ""
echo "🔐 Fazendo login no Railway..."
railway login

# Identificar projeto
echo ""
echo "📦 Identificando projeto..."
railway init

# Deploy
echo ""
echo "📤 Fazendo deploy da aplicação..."
railway up

echo ""
echo "✅ Deploy concluído com sucesso!"
echo "🌐 Acesse: $(railway run echo \$RAILWAY_PUBLIC_DOMAIN)"
