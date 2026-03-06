# Script de Setup Git e GitHub para Windows PowerShell

param(
    [string]$GitHubRepoUrl = ""
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 Setup Git e GitHub - LlamaParse App" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se Git está instalado
Write-Host "📋 Verificando Git..." -ForegroundColor Yellow
git --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git não está instalado!" -ForegroundColor Red
    Write-Host "📥 Instale em: https://git-scm.com/download/win" -ForegroundColor Red
    Exit 1
}
Write-Host "✅ Git encontrado!" -ForegroundColor Green
Write-Host ""

# Pedir informações do usuário
Write-Host "📝 Configurando Git..." -ForegroundColor Yellow
$GitName = git config user.name
$GitEmail = git config user.email

if (-not $GitName) {
    $GitName = Read-Host "👤 Nome de usuário (para commits)"
    git config --global user.name $GitName
}
Write-Host "✓ Nome: $GitName" -ForegroundColor Green

if (-not $GitEmail) {
    $GitEmail = Read-Host "📧 Email (para commits)"
    git config --global user.email $GitEmail
}
Write-Host "✓ Email: $GitEmail" -ForegroundColor Green
Write-Host ""

# Verificar se repositório já existe
Write-Host "🔍 Verificando repositório Git..." -ForegroundColor Yellow
$IsGitRepo = Test-Path .git
if ($IsGitRepo) {
    Write-Host "✅ Repositório Git já inicializado!" -ForegroundColor Green
} else {
    Write-Host "📦 Inicializando repositório Git..." -ForegroundColor Yellow
    git init
    Write-Host "✅ Repositório inicializado!" -ForegroundColor Green
}
Write-Host ""

# Fazer commit
Write-Host "📤 Preparando commit inicial..." -ForegroundColor Yellow
$HasChanges = git status --porcelain
if ($HasChanges) {
    git add .
    git commit -m "Aplicação Streamlit para LlamaParse - Deploy Ready

- Aplicação funcional
- Documentação completa
- Dockerfile e docker-compose configurados
- CI/CD com GitHub Actions
- Pronto para produção"
    Write-Host "✅ Commit criado!" -ForegroundColor Green
} else {
    Write-Host "ℹ️  Sem mudanças para commitar" -ForegroundColor Gray
}
Write-Host ""

# Verificar branch
Write-Host "🌿 Configurando branch..." -ForegroundColor Yellow
$CurrentBranch = git rev-parse --abbrev-ref HEAD
if ($CurrentBranch -ne "main") {
    Write-Host "Renomeando branch $CurrentBranch para main..." -ForegroundColor Yellow
    git branch -M main
    Write-Host "✅ Branch renomeado para main!" -ForegroundColor Green
} else {
    Write-Host "✅ Branch já é main!" -ForegroundColor Green
}
Write-Host ""

# Configurar remote
Write-Host "🔗 Configurando repositório remoto..." -ForegroundColor Yellow

if (-not $GitHubRepoUrl) {
    Write-Host ""
    Write-Host "Para continuar, você precisa de uma URL de repositório GitHub:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Acesse: https://github.com/new" -ForegroundColor White
    Write-Host "2. Preencha:" -ForegroundColor White
    Write-Host "   - Repository name: llama-parse-app" -ForegroundColor White
    Write-Host "   - Description: Aplicação Streamlit para converter PDFs" -ForegroundColor White
    Write-Host "   - Visibility: Public (para Streamlit Cloud)" -ForegroundColor White
    Write-Host "   - NÃO marque: Add README, Add .gitignore, etc" -ForegroundColor White
    Write-Host "3. Copie a URL (exemplo: https://github.com/usuario/llama-parse-app.git)" -ForegroundColor White
    Write-Host ""
    $GitHubRepoUrl = Read-Host "Cole aqui a URL do repositório"
}

if ($GitHubRepoUrl) {
    # Remover origin existente se houver
    $ExistingOrigin = git config --get remote.origin.url
    if ($ExistingOrigin) {
        Write-Host "⚠️  Removendo origin anterior..." -ForegroundColor Yellow
        git remote remove origin
    }
    
    git remote add origin $GitHubRepoUrl
    Write-Host "✅ Repositório remoto configurado!" -ForegroundColor Green
    Write-Host "   URL: $GitHubRepoUrl" -ForegroundColor Gray
    Write-Host ""
    
    # Fazer push
    Write-Host "📤 Fazendo push para GitHub..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "⚠️  Se pedir autenticação:" -ForegroundColor Yellow
    Write-Host "   - Use seu token: https://github.com/settings/tokens/new" -ForegroundColor Gray
    Write-Host "   - Ou configure SSH: https://github.com/settings/ssh/new" -ForegroundColor Gray
    Write-Host ""
    
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "✅ SUCESSO! Seu projeto está no GitHub!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "🌐 Próximo passo: Deploy no Streamlit Cloud" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "1. Acesse: https://streamlit.io/cloud" -ForegroundColor White
        Write-Host "2. Clique 'Sign up' com sua conta GitHub" -ForegroundColor White
        Write-Host "3. Clique 'New app'" -ForegroundColor White
        Write-Host "4. Selecione seu repositório e branch 'main'" -ForegroundColor White
        Write-Host "5. Em Settings → Secrets, adicione:" -ForegroundColor White
        Write-Host "   LLAMA_PARSE_API_KEY = seu-valor" -ForegroundColor White
        Write-Host ""
        Write-Host "✨ Deploy automático ativado!" -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host "❌ Erro ao fazer push!" -ForegroundColor Red
        Write-Host "Verifique sua autenticação no GitHub" -ForegroundColor Red
    }
} else {
    Write-Host "⚠️  URL do repositório não fornecida" -ForegroundColor Yellow
    Write-Host "Execute novamente com: ./setup-github.ps1 -GitHubRepoUrl 'sua-url'" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📚 Para mais informações, veja: GITHUB_SETUP.md" -ForegroundColor Cyan
Write-Host ""
