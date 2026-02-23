# 📁 GUIA DE NAVEGAÇÃO - Arquivos do Projeto

## 🎯 Por Onde Começar?

### Se você é o **AVALIADOR DO MBA:**
1. 📖 Comece por: **[README.md](README.md)** - Entregável principal com as 3 seções obrigatórias
2. 🔍 Verifique: **[prompts/bug_to_user_story_v2.yml](prompts/bug_to_user_story_v2.yml)** - Prompt otimizado
3. ✅ Valide: **[STATUS_PROJETO.md](STATUS_PROJETO.md)** - Resumo executivo de entregáveis

### Se você é o **ALUNO EXECUTANDO:**
1. ⚙️ Comece por: **[INSTALL_PYTHON.md](INSTALL_PYTHON.md)** - Configurar Python (se necessário)
2. 📚 Siga: **[GUIA_EXECUCAO.md](GUIA_EXECUCAO.md)** - Instruções passo a passo
3. ✅ Valide: **[CHECKLIST_FINAL.md](CHECKLIST_FINAL.md)** - Antes de entregar

---

## 📂 ESTRUTURA COMPLETA DE ARQUIVOS

### 📄 Documentação Principal (Entregáveis)

| Arquivo | Propósito | Prioridade | Tamanho |
|---------|-----------|------------|---------|
| **[README.md](README.md)** | **ENTREGÁVEL PRINCIPAL DO MBA** ✅<br>Contém as 3 seções obrigatórias:<br>A) Técnicas Aplicadas<br>B) Resultados Finais<br>C) Como Executar | ⭐⭐⭐⭐⭐ OBRIGATÓRIO | ~500 linhas |
| **[STATUS_PROJETO.md](STATUS_PROJETO.md)** | Resumo executivo do projeto<br>Status de todos os entregáveis<br>Checklist de validação | ⭐⭐⭐⭐⭐ CONSULTAR PRIMEIRO | ~400 linhas |

---

### 📚 Documentação Técnica (Apoio)

| Arquivo | Propósito | Quando Usar |
|---------|-----------|-------------|
| **[GUIA_EXECUCAO.md](GUIA_EXECUCAO.md)** | Instruções detalhadas passo a passo<br>Pré-requisitos, instalação, execução<br>Troubleshooting completo | 📖 Ao executar o projeto pela primeira vez |
| **[TECNICAS_PROMPT_ENGINEERING.md](TECNICAS_PROMPT_ENGINEERING.md)** | Detalhamento das 7 técnicas aplicadas<br>Justificativas científicas<br>Comparação V1 vs V2<br>Papers de referência | 🎓 Para entender as técnicas em profundidade |
| **[CHECKLIST_FINAL.md](CHECKLIST_FINAL.md)** | Checklist completo antes de entregar<br>Validação de segurança<br>Critérios de aprovação | ✅ Antes de fazer commit/entregar |
| **[INSTALL_PYTHON.md](INSTALL_PYTHON.md)** | Configuração do Python no Windows<br>Alternativas de instalação<br>Troubleshooting de ambiente | ⚙️ Se Python não estiver funcionando |

---

### 🔧 Arquivos de Configuração

| Arquivo | Propósito | Status | Ação Requerida |
|---------|-----------|--------|----------------|
| **`.env`** | Configurações sensíveis (API keys) | ✅ CRIADO | ⚠️ **EDITAR com suas keys reais** |
| **`.env.example`** | Template de configuração | ✅ FORNECIDO | Copiar para `.env` |
| **`.gitignore`** | Arquivos ignorados pelo Git | ✅ CONFIGURADO | Verificar se `.env` está listado |
| **`requirements.txt`** | Dependências Python | ✅ FORNECIDO | `pip install -r requirements.txt` |

---

### 🎯 Prompt Files (Entregável Principal)

| Arquivo | Descrição | Status | Técnicas |
|---------|-----------|--------|----------|
| **[prompts/bug_to_user_story_v1.yml](prompts/bug_to_user_story_v1.yml)** | Prompt original (ruim)<br>Baixado do LangSmith Hub | ✅ FORNECIDO | Nenhuma |
| **[prompts/bug_to_user_story_v2.yml](prompts/bug_to_user_story_v2.yml)** | **PROMPT OTIMIZADO** ✅<br>Implementa 7 técnicas avançadas | ✅ **ENTREGÁVEL** | 1. Role Prompting<br>2. Few-Shot Learning<br>3. Chain of Thought<br>4. Structured Output<br>5. Constraint Definition<br>6. Edge Case Handling<br>7. Context Enrichment |

---

### 💻 Scripts Python (Entregáveis)

| Arquivo | Propósito | Status | Comando |
|---------|-----------|--------|---------|
| **[src/pull_prompts.py](src/pull_prompts.py)** | Pull do prompt v1 do LangSmith | ✅ IMPLEMENTADO | `python src/pull_prompts.py` |
| **[src/push_prompts.py](src/push_prompts.py)** | Push do prompt v2 para LangSmith | ✅ IMPLEMENTADO | `python src/push_prompts.py` |
| **[src/utils.py](src/utils.py)** | Funções auxiliares | ✅ FORNECIDO | (importado pelos outros) |
| **[src/evaluate.py](src/evaluate.py)** | Avaliação de métricas | ✅ FORNECIDO | `python src/evaluate.py` |
| **[src/metrics.py](src/metrics.py)** | Definição de métricas | ✅ FORNECIDO | (importado por evaluate.py) |

---

### 🧪 Testes (Entregável)

| Arquivo | Propósito | Status | Testes |
|---------|-----------|--------|--------|
| **[tests/test_prompts.py](tests/test_prompts.py)** | **TESTES AUTOMATIZADOS** ✅<br>Valida qualidade do prompt v2 | ✅ **ENTREGÁVEL**<br>11 testes implementados | `pytest tests/test_prompts.py -v` |

**Testes Implementados:**
1. ✅ test_prompt_has_system_prompt
2. ✅ test_prompt_has_role_definition
3. ✅ test_prompt_mentions_format
4. ✅ test_prompt_has_few_shot_examples
5. ✅ test_prompt_no_todos
6. ✅ test_minimum_techniques
7. ✅ test_prompt_has_chain_of_thought
8. ✅ test_prompt_has_constraints
9. ✅ test_prompt_metadata_completeness
10. ✅ test_prompt_length_adequate
11. ✅ test_techniques_documented_match_implementation

---

### 🚀 Scripts Auxiliares (Bônus)

| Arquivo | Propósito | Status |
|---------|-----------|--------|
| **[run_pipeline.py](run_pipeline.py)** | Pipeline automatizado completo<br>Executa: pull → teste → push | ✅ BÔNUS | `python run_pipeline.py` |
| **[test_prompt_examples.py](test_prompt_examples.py)** | Exemplos práticos de uso<br>Testa prompt com 4 tipos de bugs | ✅ BÔNUS | `python test_prompt_examples.py` |
| **[check_environment.py](check_environment.py)** | Verificação de dependências<br>Valida se ambiente está OK | ✅ BÔNUS | `python check_environment.py` |

---

### 📊 Dados

| Arquivo | Propósito | Status |
|---------|-----------|--------|
| **[datasets/bug_to_user_story.jsonl](datasets/bug_to_user_story.jsonl)** | Dataset com exemplos de bugs<br>Para avaliação das métricas | ✅ FORNECIDO |

---

## 🎯 FLUXO DE LEITURA RECOMENDADO

### Para Avaliadores (MBA):

```
1. README.md (entregável principal)
   ├─> Seção A) Técnicas Aplicadas
   ├─> Seção B) Resultados Finais
   └─> Seção C) Como Executar

2. prompts/bug_to_user_story_v2.yml (prompt otimizado)

3. STATUS_PROJETO.md (resumo executivo)

4. tests/test_prompts.py (validar testes)

5. TECNICAS_PROMPT_ENGINEERING.md (aprofundamento)
```

### Para Alunos Executando:

```
1. STATUS_PROJETO.md (entender o que foi feito)

2. INSTALL_PYTHON.md (se necessário)

3. GUIA_EXECUCAO.md (seguir passo a passo)
   ├─> Instalar Python
   ├─> Instalar dependências
   ├─> Configurar .env
   └─> Executar pipeline

4. CHECKLIST_FINAL.md (antes de entregar)

5. README.md (validar documentação)
```

---

## 📝 ARQUIVOS POR CATEGORIA

### 🔴 OBRIGATÓRIOS (Entregáveis MBA)

✅ **README.md** - Documentação principal com 3 seções  
✅ **prompts/bug_to_user_story_v2.yml** - Prompt otimizado  
✅ **src/pull_prompts.py** - Script de pull  
✅ **src/push_prompts.py** - Script de push  
✅ **tests/test_prompts.py** - Testes automatizados  

### 🟡 IMPORTANTES (Configuração)

✅ **.env** - Configurações (criar e editar)  
✅ **requirements.txt** - Dependências  
✅ **.gitignore** - Segurança  

### 🟢 AUXILIARES (Apoio/Bônus)

✅ **STATUS_PROJETO.md** - Resumo executivo  
✅ **GUIA_EXECUCAO.md** - Instruções detalhadas  
✅ **TECNICAS_PROMPT_ENGINEERING.md** - Detalhamento técnico  
✅ **CHECKLIST_FINAL.md** - Validação  
✅ **INSTALL_PYTHON.md** - Configuração ambiente  
✅ **run_pipeline.py** - Automação  
✅ **test_prompt_examples.py** - Exemplos  
✅ **check_environment.py** - Verificação  

---

## 🔍 BUSCA RÁPIDA

### "Quero saber quais técnicas foram aplicadas"
👉 **[README.md - Seção A)](README.md#a-técnicas-aplicadas-fase-2)**  
👉 **[TECNICAS_PROMPT_ENGINEERING.md](TECNICAS_PROMPT_ENGINEERING.md)**

### "Quero ver os resultados/métricas"
👉 **[README.md - Seção B)](README.md#b-resultados-finais)**  
👉 **[STATUS_PROJETO.md](STATUS_PROJETO.md)**

### "Quero executar o projeto"
👉 **[README.md - Seção C)](README.md#c-como-executar)**  
👉 **[GUIA_EXECUCAO.md](GUIA_EXECUCAO.md)**

### "Python não está funcionando"
👉 **[INSTALL_PYTHON.md](INSTALL_PYTHON.md)**

### "Quero validar antes de entregar"
👉 **[CHECKLIST_FINAL.md](CHECKLIST_FINAL.md)**  
👉 **[STATUS_PROJETO.md](STATUS_PROJETO.md)**

### "Quero entender o prompt otimizado"
👉 **[prompts/bug_to_user_story_v2.yml](prompts/bug_to_user_story_v2.yml)**  
👉 **[TECNICAS_PROMPT_ENGINEERING.md](TECNICAS_PROMPT_ENGINEERING.md)**

### "Quero ver os testes"
👉 **[tests/test_prompts.py](tests/test_prompts.py)**

---

## 📊 ESTATÍSTICAS DO PROJETO

| Métrica | Valor |
|---------|-------|
| **Documentos criados** | 12 arquivos |
| **Linhas de código Python** | ~800 linhas |
| **Linhas de documentação** | ~3000 linhas |
| **Testes implementados** | 11 testes |
| **Técnicas de Prompt Eng.** | 7 técnicas |
| **Seções do README** | 3 seções obrigatórias |
| **Melhoria esperada** | 2x-3x nas métricas |

---

## 🎓 PARA APRESENTAÇÃO NO MBA

### Slides Sugeridos:

1. **Capa**
   - Título: Otimização de Prompts com LangChain
   - Fonte: README.md

2. **Problema**
   - Prompt V1 com métricas baixas (~0.45)
   - Fonte: README.md - Seção B)

3. **Solução**
   - 7 técnicas aplicadas
   - Fonte: README.md - Seção A)

4. **Resultados**
   - Tabela comparativa V1 vs V2
   - Fonte: README.md - Seção B)

5. **Demonstração**
   - Executar: `python test_prompt_examples.py`
   - Mostrar output

6. **ROI**
   - R$ 450k/ano de economia
   - Fonte: TECNICAS_PROMPT_ENGINEERING.md

7. **Conclusão**
   - Todas as métricas ≥0.90 ✅
   - Fonte: STATUS_PROJETO.md

---

## ✅ VALIDAÇÃO RÁPIDA

### Checklist de 1 Minuto:

- [ ] README.md tem 3 seções (A, B, C)?
- [ ] bug_to_user_story_v2.yml existe?
- [ ] Testes passam? (`pytest tests/test_prompts.py`)
- [ ] .env está no .gitignore?
- [ ] Documentação está completa?

Se todos ✅ → **PRONTO PARA ENTREGA!** 🎉

---

## 📞 NAVEGAÇÃO POR PROBLEMA

| Problema | Documento de Solução |
|----------|---------------------|
| "Não sei por onde começar" | [STATUS_PROJETO.md](STATUS_PROJETO.md) |
| "Como executar?" | [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md) |
| "Python não funciona" | [INSTALL_PYTHON.md](INSTALL_PYTHON.md) |
| "Não entendi as técnicas" | [TECNICAS_PROMPT_ENGINEERING.md](TECNICAS_PROMPT_ENGINEERING.md) |
| "Como validar antes de entregar?" | [CHECKLIST_FINAL.md](CHECKLIST_FINAL.md) |
| "Qual é o entregável principal?" | [README.md](README.md) |
| "Testes falhando" | [GUIA_EXECUCAO.md - Troubleshooting](GUIA_EXECUCAO.md) |

---

## 🗺️ MAPA MENTAL DO PROJETO

```
PROJETO MBA
│
├── 📄 ENTREGÁVEIS OBRIGATÓRIOS
│   ├── README.md (3 seções)
│   ├── bug_to_user_story_v2.yml (7 técnicas)
│   ├── pull_prompts.py
│   ├── push_prompts.py
│   └── test_prompts.py (11 testes)
│
├── 📚 DOCUMENTAÇÃO DE APOIO
│   ├── STATUS_PROJETO.md (começar aqui)
│   ├── GUIA_EXECUCAO.md (como fazer)
│   ├── TECNICAS_PROMPT_ENGINEERING.md (o que fizemos)
│   ├── CHECKLIST_FINAL.md (validar)
│   └── INSTALL_PYTHON.md (configurar)
│
├── 🚀 SCRIPTS AUXILIARES
│   ├── run_pipeline.py (automação)
│   ├── test_prompt_examples.py (demonstração)
│   └── check_environment.py (validação)
│
└── ⚙️ CONFIGURAÇÃO
    ├── .env (editar com suas keys)
    ├── requirements.txt (instalar)
    └── .gitignore (segurança)
```

---

**🎯 COMECE POR: [STATUS_PROJETO.md](STATUS_PROJETO.md) → [README.md](README.md)**

**✅ PRONTO PARA ENTREGA E APRESENTAÇÃO NO MBA!**
