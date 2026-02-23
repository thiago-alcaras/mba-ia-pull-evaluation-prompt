# ⚠️ CONFIGURAÇÃO DO PYTHON NO WINDOWS

## Problema Detectado

O comando `python` não está disponível no seu sistema Windows. Você precisa:

1. **Instalar Python 3.9+**, OU
2. **Configurar o alias do Python**

---

## Opção 1: Instalar Python (Recomendado)

### Passo 1: Download
Baixe Python 3.9+ de: https://www.python.org/downloads/

### Passo 2: Instalação
- ✅ **MARQUE "Add Python to PATH"** durante a instalação
- Escolha "Install Now"
- Aguarde a instalação

### Passo 3: Verificar
Abra um **novo** terminal PowerShell e execute:
```powershell
python --version
```

Deve mostrar: `Python 3.9.x` ou superior

---

## Opção 2: Usar Python via Microsoft Store

### Passo 1: Instalar
```powershell
# Abrir Microsoft Store e instalar Python 3.9+
# OU executar:
python
# Isso abrirá a Microsoft Store automaticamente
```

### Passo 2: Instalar da Store
- Clique em "Instalar"
- Aguarde
- Abra novo terminal

### Passo 3: Verificar
```powershell
python --version
```

---

## Opção 3: Usar py (se já tem Python instalado)

Se você já tem Python instalado mas o comando `python` não funciona:

### Testar py:
```powershell
py --version
```

### Se funcionar, use `py` ao invés de `python`:
```powershell
# Ao invés de:
python check_environment.py

# Use:
py check_environment.py
```

---

## Depois de Instalar Python

### 1. Abra um NOVO terminal PowerShell

### 2. Navegue até o projeto:
```powershell
cd D:\Repos\mba-ia-pull-evaluation-prompt
```

### 3. Verifique o ambiente:
```powershell
python check_environment.py
```

### 4. Instale as dependências:
```powershell
pip install -r requirements.txt
```

### 5. Configure o .env:
Edite o arquivo `.env` e adicione suas API keys

### 6. Execute o pipeline:
```powershell
python run_pipeline.py
```

---

## Troubleshooting

### "python: command not found" mesmo após instalar
**Solução:** Reinicie o computador e abra um novo terminal

### "pip: command not found"
**Solução:**
```powershell
python -m pip install --upgrade pip
```

### Permissão negada ao instalar pacotes
**Solução:** Abra PowerShell como Administrador

### Erro SSL ao instalar pacotes
**Solução:**
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

---

## Alternativa: Ambiente Virtual (Recomendado para projetos)

### Criar ambiente virtual:
```powershell
python -m venv venv
```

### Ativar:
```powershell
.\venv\Scripts\activate
```

### Instalar dependências:
```powershell
pip install -r requirements.txt
```

### Verificar:
```powershell
python check_environment.py
```

---

## Versões Requeridas

| Dependência | Versão Mínima |
|-------------|---------------|
| Python | 3.9+ |
| langchain | 0.3.13 |
| langsmith | 0.2.7 |
| langchain-google-genai | 2.0.8 |
| pytest | 8.3.4 |

---

## Após Configurar Python

Continue com as instruções do README.md:

1. ✅ Python instalado e funcionando
2. ⏭️ Instalar dependências: `pip install -r requirements.txt`
3. ⏭️ Configurar `.env` com suas API keys
4. ⏭️ Executar: `python run_pipeline.py`

---

**Documentação completa em:** [README.md](README.md)
