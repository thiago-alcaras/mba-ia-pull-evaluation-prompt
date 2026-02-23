"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        username = os.getenv('USERNAME_LANGSMITH_HUB')
        if not username:
            print("❌ USERNAME_LANGSMITH_HUB não configurado no .env")
            return False
        
        # Extrair system_prompt e user_prompt
        system_prompt = prompt_data.get('system_prompt', '').strip()
        user_prompt = prompt_data.get('user_prompt', '{bug_report}').strip()
        
        if not system_prompt:
            print("❌ system_prompt está vazio")
            return False
        
        # Criar ChatPromptTemplate usando from_messages
        messages = [
            ("system", system_prompt),
            ("human", user_prompt)
        ]
        
        chat_prompt = ChatPromptTemplate.from_messages(messages)
        
        # Fazer push para o LangSmith Hub
        full_prompt_name = f"{username}/{prompt_name}"
        print(f"📤 Fazendo push do prompt: {full_prompt_name}")
        print(f"   Descrição: {prompt_data.get('description', 'N/A')}")
        print(f"   Versão: {prompt_data.get('version', 'N/A')}")
        
        # Extrair metadados para exibir
        techniques = prompt_data.get('techniques_applied', [])
        if techniques:
            print(f"   Técnicas aplicadas ({len(techniques)}):")
            for tech in techniques:
                tech_name = tech.get('name', 'N/A') if isinstance(tech, dict) else tech
                print(f"      - {tech_name}")
        
        # Push do prompt
        hub.push(
            full_prompt_name,
            chat_prompt,
            new_repo_is_public=True
        )
        
        print(f"✅ Prompt publicado com sucesso!")
        print(f"   URL: https://smith.langchain.com/hub/{full_prompt_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao fazer push do prompt: {e}")
        print(f"   Tipo do erro: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []
    
    # Campos obrigatórios
    required_fields = ['description', 'system_prompt', 'version']
    for field in required_fields:
        if field not in prompt_data:
            errors.append(f"Campo obrigatório faltando: {field}")
    
    # Validar system_prompt não vazio
    system_prompt = prompt_data.get('system_prompt', '').strip()
    if not system_prompt:
        errors.append("system_prompt está vazio")
    
    # Verificar se ainda tem TODOs
    if 'TODO' in system_prompt or 'TODO' in str(prompt_data):
        errors.append("Prompt ainda contém TODOs - complete antes de fazer push")
    
    # Validar técnicas aplicadas
    techniques = prompt_data.get('techniques_applied', [])
    if len(techniques) < 2:
        errors.append(f"Mínimo de 2 técnicas requeridas nos metadados, encontradas: {len(techniques)}")
    
    # Validar tags
    tags = prompt_data.get('tags', [])
    if len(tags) < 3:
        errors.append(f"Recomendado pelo menos 3 tags, encontradas: {len(tags)}")
    
    return (len(errors) == 0, errors)


def main():
    """Função principal"""
    print_section_header("Push de Prompts Otimizados para LangSmith Hub")
    
    # Verificar variáveis de ambiente
    required_vars = ['LANGCHAIN_API_KEY', 'LANGCHAIN_ENDPOINT', 'USERNAME_LANGSMITH_HUB']
    if not check_env_vars(required_vars):
        return 1
    
    # Carregar prompt v2
    prompt_file = Path(__file__).parent.parent / 'prompts' / 'bug_to_user_story_v2.yml'
    print(f"📂 Carregando prompt de: {prompt_file}")
    
    prompt_data_full = load_yaml(str(prompt_file))
    if not prompt_data_full:
        print("❌ Erro ao carregar arquivo YAML")
        return 1
    
    # Extrair dados do prompt
    prompt_key = 'bug_to_user_story_v2'
    if prompt_key not in prompt_data_full:
        print(f"❌ Chave '{prompt_key}' não encontrada no arquivo YAML")
        return 1
    
    prompt_data = prompt_data_full[prompt_key]
    print(f"✅ Prompt carregado: {prompt_data.get('description', 'N/A')}")
    
    # Validar prompt
    print("\n🔍 Validando prompt...")
    is_valid, errors = validate_prompt(prompt_data)
    
    if not is_valid:
        print("❌ Validação falhou:")
        for error in errors:
            print(f"   - {error}")
        return 1
    
    print("✅ Validação passou!")
    
    # Fazer push
    print("\n📤 Iniciando push para LangSmith Hub...")
    success = push_prompt_to_langsmith('bug_to_user_story_v2', prompt_data)
    
    if success:
        print("\n🎉 Processo concluído com sucesso!")
        print("\nPróximos passos:")
        print("1. Acesse o LangSmith Hub para verificar o prompt publicado")
        print("2. Execute avaliações usando src/evaluate.py")
        print("3. Compare métricas entre v1 e v2")
        return 0
    else:
        print("\n❌ Falha ao fazer push do prompt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
