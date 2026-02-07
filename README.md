# 📊 LinkedIn Post Metrics Bot

Automação para coletar métricas de um post do LinkedIn a cada minuto  
Impressões • Curtidas • Comentários • Compartilhamentos  

PROJETO VAI SE DIVIDIR EM 3 PARTES:
- PARTE 1: EXTRAIR DADOS DE METRICAS HISTORICAS COM SELENIUM E REALIZAR UMA ANÁLISE EM CIMA DISSO
- PARTE 2: CRIAR AUTOMAÇÃO QUE EXTRAI E ARMAZENA DADOS A CADA 5 MINUTOS DOS POSTS (VERIFICAR EVOLUÇÃO)
- PARTE 3: ESTUDO APROFUNDADO E MACHINE LEARNING PARA PREVISÃO E AVALIAÇÃO

Os dados são armazenados em memória, viram um **DataFrame**, e podem ser salvos em **CSV** ou enviados para um **banco de dados**.

---

# 🚀 1. Instalar o **uv** (gerenciador de ambiente Python ultra rápido)

### Linux / Mac
```bash
curl -Ls https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Testar instalação:

```bash
uv --version
```

---

# 📁 2. Criar pasta do projeto

```bash
mkdir linkedin-metrics-bot
cd linkedin-metrics-bot
```

---

# 🧪 3. Criar ambiente virtual com uv

```bash
uv venv
```

Ativar o ambiente:

### Linux / Mac
```bash
source .venv/bin/activate
```

### Windows
```powershell
.venv\Scripts\activate
```

---

# 📦 4. Instalar dependências

```bash
uv pip install selenium pandas python-dotenv sqlalchemy psycopg2-binary
```

### O que cada biblioteca faz

| Biblioteca | Função |
|-----------|-------|
| selenium | Automação do navegador |
| pandas | Estrutura DataFrame e CSV |
| python-dotenv | Carrega variáveis de ambiente do `.env` |
| sqlalchemy | Conexão genérica com banco |
| psycopg2-binary | Driver para PostgreSQL |

---

# 🌐 5. ChromeDriver

As versões recentes do Selenium já incluem o **Selenium Manager**, então não é necessário baixar o ChromeDriver manualmente.  
Apenas garanta que o **Google Chrome esteja instalado**.

Teste rápido:

```bash
python -c "from selenium import webdriver; print('Selenium OK')"
```

---

# 🔐 6. Criar arquivo `.env`

```bash
touch .env
```

Conteúdo:

```
LINKEDIN_EMAIL=seuemail@dominio.com
LINKEDIN_PASSWORD=suasenha
LINKEDIN_POST_URL=https://www.linkedin.com/feed/update/xxxx

METRICS_CSV_PATH=linkedin_metrics.csv
INTERVAL_SECONDS=60

# opcional banco
DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/db
DB_TABLE=linkedin_post_metrics
```

---

# 🧪 7. Testar ambiente

```bash
python
```

Dentro do Python:

```python
import selenium, pandas, sqlalchemy
print("Ambiente pronto 🚀")
```

---

# ✅ Ambiente configurado

Agora o ambiente está pronto para rodar o script que:

1. Faz login no LinkedIn  
2. Acessa o post  
3. Coleta métricas a cada minuto  
4. Armazena em lista  
5. Converte para DataFrame  
6. Salva em CSV ou banco  

Você acaba de montar um pequeno pipeline de engenharia de dados local.
