# 📋 Pré-Requisitos e Pós-Deployment

## 🔐 Pré-Deployment Checklist

### Segurança
- [ ] Remover todas as API keys do código
- [ ] Usar variáveis de ambiente para secrets
- [ ] `.env` arquivo em `.gitignore`
- [ ] `.streamlit/secrets.toml` em `.gitignore`
- [ ] Repositório é privado? (opcional)

### Código
- [ ] Testes executados com sucesso
- [ ] Sem erros de import
- [ ] `requirements.txt` completo e atualizado
- [ ] Sem arquivos temporários
- [ ] Código com comentários claros

### Documentação
- [ ] README.md completo
- [ ] DEPLOY.md com instruções
- [ ] Como usar a aplicação documentado
- [ ] Problemas conhecidos listados

### Ambiente
- [ ] Python 3.10+ suportado
- [ ] Todas as dependências resolvidas
- [ ] Dockerfile testado localmente
- [ ] Docker Compose funciona

### Arquivos Necessários
- [ ] `.gitignore` configurado
- [ ] `.env.example` criado
- [ ] `requirements.txt` existente
- [ ] `app.py` é arquivo de entrada
- [ ] `Dockerfile` (para Docker)

---

## 🎯 Pré-Deployment Workflow

### 1. Limpar Repositório

```bash
# Remover arquivos desnecessários
rm -rf __pycache__ .pytest_cache build dist *.egg-info

# Remover arquivos sensíveis
rm -f .env .env.local

# Verificar o que será commitado
git status

# Limpar histórico sensível (se necessário)
git filter-branch --force --all
```

### 2. Testar Localmente

```bash
# Criar novo venv limpo
python -m venv test_venv
source test_venv/bin/activate  # venv\Scripts\activate no Windows

# Instalar requirements
pip install -r requirements.txt

# Testar imports
python -c "import streamlit; import llama_parse; print('OK')"

# Testar app
streamlit run app.py

# Testar com Docker
docker build -t test-llama-parse .
docker run -p 8501:8501 test-llama-parse
```

### 3. Verificar Logs

```bash
# Verificar se há erros na inicialização
streamlit run app.py --logger.level=debug

# Buscar por problemas comuns
grep -r "TODO\|FIXME\|XXX" . --include="*.py"

# Verificar tamanho da imagem Docker
docker images | grep llama-parse
```

### 4. Fazer Commit Final

```bash
# Criar branch de release (opcional)
git checkout -b release/v1.0.0

# Adicionar todas as mudanças
git add .

# Commit com mensagem descritiva
git commit -m "Ready for production deployment

- Verified all dependencies
- API keys properly configured
- Documentation complete
- Tested locally with all configurations"

# Tag version (opcional)
git tag -a v1.0.0 -m "Production release v1.0.0"

# Push
git push origin main --follow-tags
```

---

## 🚀 Durante o Deployment

### Streamlit Cloud
```bash
# Apenas verifique se tudo está no GitHub
git log --oneline | head -5
git config --list | grep url
```

### AWS/GCP/Azure
```bash
# Monitorar deploy
eb status  # AWS
gcloud run deployments describe llama-parse-app  # GCP

# Ver logs em tempo real
eb logs --stream  # AWS
gcloud run logs read llama-parse-app  # GCP
```

### Docker
```bash
# Verificar se container está saudável
docker ps
docker logs -f llama-parse-app

# Testar endpoint
curl http://localhost:8501/_stcore/health
```

---

## ✅ Pós-Deployment Checklist

### Acesso
- [ ] Aplicação acessível via URL pública
- [ ] Tempo de carregamento aceitável (<5s)
- [ ] Sem erros 404 ou 500
- [ ] Autenticação/permissões configuradas (se aplicável)

### Funcionalidade
- [ ] Upload de PDFs funciona
- [ ] Processamento funciona
- [ ] Downloads funcionam
- [ ] Nenhuma erro de API key
- [ ] Mensagens de erro claras

### Performance
- [ ] Tempo de resposta aceitável
- [ ] Sem timeout de requisições
- [ ] Uso de memória normal
- [ ] CPU dentro do esperado

### Dados
- [ ] Pasta `docs` acessível
- [ ] Pasta `outputs` acessível
- [ ] Permissões de leitura/escrita corretas
- [ ] Backups configurados

### Segurança
- [ ] HTTPS/SSL ativado (produção)
- [ ] API keys seguras
- [ ] Sem exposição de variáveis sensíveis
- [ ] Logs configurados
- [ ] Rate limiting (se necessário)

---

## 📊 Pós-Deployment Testing

### Teste da Aplicação Completa

```bash
# 1. Testar upload
curl -X POST http://seu-url/upload -F "file=@docs/doc1.pdf"

# 2. Testar processamento
# Use a interface web

# 3. Testar downloads
curl -O http://seu-url/outputs/doc1.md

# 4. Verificar logs
# Veja seção "Monitoramento" de cada plataforma
```

### Teste de Carga (Opcional)

```bash
# Instalar ferramenta
pip install locust

# Criar locustfile.py
cat > locustfile.py << 'EOF'
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def health_check(self):
        self.client.get("/_stcore/health")
EOF

# Executar teste
locust -f locustfile.py --host=http://seu-url --users 10 --spawn-rate 1
```

---

## 🔧 Pós-Deployment Configuration

### 1. Monitoramento e Alertas

**Streamlit Cloud**:
- Acesse Dashboard da sua app
- Clique "App settings"
- Configure notificações

**AWS**:
```bash
# CloudWatch alarms
aws cloudwatch put-metric-alarm \
  --alarm-name llama-parse-cpu \
  --alarm-description "Alert if CPU > 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/ElasticBeanstalk \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
```

**Google Cloud**:
```bash
gcloud monitoring policies create --notification-channels CHANNEL_ID
```

### 2. Backups

**DigitalOcean/VPS**:
```bash
# Criar backup automático
# Cron job para backup diário dos outputs
0 2 * * * tar -czf /backups/llama-parse-$(date +\%Y\%m\%d).tar.gz /home/seu-usuario/seu-repo/outputs/
```

**AWS**:
- Use S3 para backup de arquivos processados
- Use RDS se adicionar banco de dados

### 3. Logging

**Configurar logging centralizado**:
```python
# Em app.py ou utils.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
```

### 4. Health Checks

**Crie endpoint de health check**:
```python
# Em app.py
@app.route('/health')
def health():
    return {'status': 'ok'}, 200
```

---

## 🆘 Troubleshooting Pós-Deploy

### Aplicação não inicia
```bash
# Verificar logs
# Streamlit Cloud: Veja "App analytics"
# AWS: eb logs
# GCP: gcloud run logs read
# Docker: docker logs container-name

# Verificar variáveis de ambiente
# Confirme LLAMA_PARSE_API_KEY está configurada
```

### Lentidão
```bash
# Ver uso de recursos
# AWS: CloudWatch
# GCP: Cloud Console
# Docker: docker stats

# Aumentar recursos se necessário
# Streamlit Cloud: Upgrade plan
# AWS: eb scale -i <instances>
# GCP: gcloud run update --memory 2Gi
```

### Erro "Connection refused"
```bash
# Verificar se serviço está rodando
systemctl status llama-parse  # VPS

# Verificar portas
netstat -tuln | grep 8501  # Linux
netstat -ano | findstr :8501  # Windows

# Reiniciar serviço
systemctl restart llama-parse  # Linux
# ou docker restart container
```

### API Key Inválida
```bash
# Verificar se variável está configurada
echo $LLAMA_PARSE_API_KEY  # Linux
echo %LLAMA_PARSE_API_KEY%  # Windows

# Ver valor em Docker
docker inspect container-name | grep LLAMA_PARSE

# Atualizar valor
# Streamlit Cloud: Settings → Secrets
# AWS: eb setenv LLAMA_PARSE_API_KEY=novo-valor
# GCP: gcloud run update ... --set-env-vars...
```

---

## 📈 Métricas para Monitorar

### Críticas
- ✅ Tempo de resposta < 5s
- ✅ Uptime > 99%
- ✅ CPU < 75%
- ✅ Memória < 80%

### Importantes
- 📊 Taxa de erros < 1%
- 📊 Requisições por minuto
- 📊 Tamanho da fila de processamento
- 📊 Tempo médio de processamento

### Informativas
- 📝 Total de arquivos processados
- 📝 Total de espaço em disco usado
- 📝 Últimos erros
- 📝 Histórico de deployments

---

## 🔄 Manutenção Regular

### Diária
- [ ] Verificar logs de erros
- [ ] Confirmar aplicação está respondendo
- [ ] Monitorar uso de disco

### Semanal
- [ ] Review de performance
- [ ] Backup manual de arquivos importantes
- [ ] Atualização de dependências (se patches críticos)

### Mensal
- [ ] Análise completa de logs
- [ ] Limpeza de arquivos antigos
- [ ] Atualização das dependências
- [ ] Teste de backup/restore

### Trimestral
- [ ] Major updates das dependências
- [ ] Review de segurança
- [ ] Otimizações de performance
- [ ] Rotação de chaves de segurança

---

## 🚀 Próximos Passos Pós-Deploy

1. **Monitorar**: Configure alertas
2. **Documentar**: Crie playbook de operações
3. **Escalar**: Prepare plano para crescimento
4. **Otimizar**: Melhore performance conforme necessário
5. **Evoluir**: Adicione features baseado em feedback

---

**Lembrete**: Após deployment, continue monitorando e ajustando a configuração conforme necessário!
