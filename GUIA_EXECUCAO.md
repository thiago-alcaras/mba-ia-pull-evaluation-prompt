# 🚀 Guia de Execução - Projeto MBA: Pull, Otimização e Avaliação de Prompts

## ✅ Status da Implementação

Todos os 5 passos foram implementados com sucesso:

- ✅ **PASSO 1**: Arquivo `.env` criado com configurações
- ✅ **PASSO 2**: Script `src/pull_prompts.py` implementado
- ✅ **PASSO 3**: Prompt otimizado `prompts/bug_to_user_story_v2.yml` criado
- ✅ **PASSO 4**: Script `src/push_prompts.py` implementado
- ✅ **PASSO 5**: Testes `tests/test_prompts.py` implementados

---

## 📋 Pré-requisitos

1. **Python 3.9+** instalado
2. **Dependências instaladas**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variáveis no arquivo `.env`**:
   - Substitua `<MINHA_CHAVE_LANGSMITH>` pela sua chave real do LangSmith
   - A chave do Google Gemini já está configurada

---

## 🔧 Configuração do Ambiente

### 1. Editar o arquivo `.env`

Abra o arquivo `.env` e substitua:

```env
LANGCHAIN_API_KEY=<MINHA_CHAVE_LANGSMITH>
```

Por sua chave real do LangSmith que você pode obter em: https://smith.langchain.com/settings

Verifique também se o `USERNAME_LANGSMITH_HUB` está correto:

```env
USERNAME_LANGSMITH_HUB=leonanluppi
```

---

## 🎯 Como Executar o Projeto

### **Passo 1: Fazer Pull do Prompt V1 do LangSmith**

```bash
python src/pull_prompts.py
```

Isso irá:
- Conectar ao LangSmith Hub
- Baixar o prompt `leonanluppi/bug_to_user_story_v1`
- Salvar em `prompts/bug_to_user_story_v1.yml`

### **Passo 2: Validar o Prompt V2 Otimizado**

Execute os testes para validar a qualidade do prompt otimizado:

```bash
pytest tests/test_prompts.py -v
```

Ou, se o comando acima não funcionar:

```bash
python -m pytest tests/test_prompts.py -v
```

Os testes verificam:
- ✅ `test_prompt_has_system_prompt` - System prompt existe e não está vazio
- ✅ `test_prompt_has_role_definition` - Define persona (Product Owner)
- ✅ `test_prompt_mentions_format` - Exige formato Markdown/User Story
- ✅ `test_prompt_has_few_shot_examples` - Contém exemplos few-shot
- ✅ `test_prompt_no_todos` - Não contém TODOs
- ✅ `test_minimum_techniques` - Pelo menos 2 técnicas nos metadados
- ✅ `test_prompt_has_chain_of_thought` - Implementa CoT
- ✅ `test_prompt_has_constraints` - Define restrições claras
- ✅ `test_prompt_metadata_completeness` - Metadados completos
- ✅ `test_prompt_length_adequate` - Tamanho adequado
- ✅ `test_techniques_documented_match_implementation` - Técnicas implementadas

### **Passo 3: Fazer Push do Prompt V2 para o LangSmith**

```bash
python src/push_prompts.py
```

Isso irá:
- Ler o arquivo `prompts/bug_to_user_story_v2.yml`
- Validar a estrutura
- Fazer push PÚBLICO para `leonanluppi/bug_to_user_story_v2`
- Exibir URL do prompt no LangSmith Hub

---

## 📊 Técnicas de Prompt Engineering Aplicadas

O prompt V2 implementa **7 técnicas avançadas**:

### 1. **Role Prompting**
- Define a IA como "Product Owner Senior com 10+ anos de experiência"
- **Impacto**: Aumenta qualidade e consistência das respostas

### 2. **Few-Shot Learning**
- Inclui 3 exemplos completos (performance, UI, lógica de negócio)
- **Impacto**: Ensina formato desejado através de exemplos

### 3. **Chain of Thought (CoT)**
- Força raciocínio explícito em 4 passos antes da resposta final
- **Impacto**: Melhora precisão e reduz alucinações

### 4. **Structured Output**
- Define template exato: "Como/Quero/Para que" + Critérios
- **Impacto**: Garante consistência e facilita parsing

### 5. **Constraint Definition**
- Regras claras: mínimo 3 critérios, verbos de ação, testabilidade
- **Impacto**: Previne outputs vagos ou incompletos

### 6. **Edge Case Handling**
- Instruções para bugs vagos, múltiplos problemas ou muito técnicos
- **Impacto**: Aumenta robustez em cenários reais

### 7. **Context Enrichment**
- Adiciona frameworks: INVEST, SMART, boas práticas ágeis
- **Impacto**: Alinha output com padrões da indústria

---

## 🧪 Estrutura do Prompt V2

```yaml
bug_to_user_story_v2:
  description: "Prompt otimizado para converter relatos de bugs..."
  
  system_prompt: |
    # Papel e Contexto (Role Prompting)
    Você é um Product Owner Senior...
    
    # Processo de Raciocínio (Chain of Thought)
    Passo 1 - Análise...
    Passo 2 - Estruturação...
    Passo 3 - Critérios de Aceite...
    Passo 4 - Validação...
    
    # Exemplos Few-Shot
    Exemplo 1: Bug de Performance...
    Exemplo 2: Bug de Interface...
    Exemplo 3: Bug de Lógica de Negócio...
    
    # Restrições e Diretrizes
    1. Formato: Markdown
    2. Estrutura: Como/Quero/Para que
    3. Mínimo: 3 critérios de aceite
    ...

  techniques_applied:
    - Role Prompting
    - Few-Shot Learning
    - Chain of Thought
    - Structured Output
    - Constraint Definition
    - Edge Case Handling
    - Context Enrichment
```

---

## 📈 Métricas Esperadas

Após avaliação no LangSmith, esperamos:

| Métrica       | Valor Esperado |
|---------------|----------------|
| Clarity       | ≥ 0.95         |
| Precision     | ≥ 0.93         |
| F1-Score      | ≥ 0.94         |
| Helpfulness   | ≥ 0.95         |
| Correctness   | ≥ 0.96         |

---

## 🔍 Testando o Prompt

Para testar o prompt manualmente, você pode usar o arquivo `src/evaluate.py` (se implementado) ou testar diretamente no LangSmith Hub após o push.

Exemplo de entrada para teste:

```text
o app ta super lento quando eu tento abrir a lista de produtos, demora uns 10 segundos pra carregar
parece que trava tudo
```

Saída esperada: User Story formatada com Chain of Thought + User Story final.

---

## 📁 Estrutura de Arquivos Criados/Modificados

```
.env                                    # ✅ Criado - Configurações
prompts/
  └── bug_to_user_story_v2.yml         # ✅ Criado - Prompt otimizado
src/
  ├── pull_prompts.py                   # ✅ Implementado
  └── push_prompts.py                   # ✅ Implementado
tests/
  └── test_prompts.py                   # ✅ Implementado
```

---

## 🚨 Avisos de Segurança

⚠️ **IMPORTANTE**: O arquivo `.env` contém chaves de API sensíveis!

1. **NUNCA** faça commit do arquivo `.env` no Git
2. Verifique se `.env` está no `.gitignore`
3. Considere rotacionar as chaves após o projeto

---

## 🎓 Próximos Passos para o MBA

1. ✅ Execute `pytest` para validar todos os testes
2. ✅ Faça push do prompt v2 com `python src/push_prompts.py`
3. 📊 Acesse o LangSmith e compare prompts v1 vs v2
4. 📈 Execute avaliações usando `src/evaluate.py`
5. 📝 Documente os resultados das métricas
6. 🎯 Apresente as melhorias alcançadas

---

## 💡 Dicas

- Use o LangSmith Tracing para debugar prompts
- Teste com diferentes tipos de bug reports
- Compare as saídas v1 vs v2 lado a lado
- Documente casos onde o v2 superou o v1

---

## 📞 Suporte

Em caso de dúvidas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que as chaves de API estão corretas no `.env`
3. Execute os testes para validar a implementação

Boa sorte no seu projeto de MBA! 🚀
