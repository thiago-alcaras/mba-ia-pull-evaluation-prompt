"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """
    Faz pull do prompt do LangSmith Hub e salva localmente.
    
    Returns:
        0 se sucesso, 1 se erro
    """
    print_section_header("Pull de Prompts do LangSmith Hub")
    
    # Verificar variáveis de ambiente
    required_vars = ['LANGCHAIN_API_KEY', 'LANGCHAIN_ENDPOINT']
    if not check_env_vars(required_vars):
        return 1
    
    try:
        # Pull do prompt do LangSmith Hub
        prompt_name = "leonanluppi/bug_to_user_story_v1"
        print(f"📥 Fazendo pull do prompt: {prompt_name}")
        
        prompt = hub.pull(prompt_name)
        print(f"✅ Prompt puxado com sucesso!")
        
        # Extrair conteúdo do prompt
        # O prompt é um ChatPromptTemplate, precisamos extrair os componentes
        messages = prompt.messages if hasattr(prompt, 'messages') else []
        
        # Montar estrutura YAML
        prompt_data = {
            'bug_to_user_story_v1': {
                'description': 'Prompt para converter relatos de bugs em User Stories',
                'system_prompt': '',
                'user_prompt': '{bug_report}',
                'version': 'v1',
                'created_at': '2025-01-15',
                'tags': ['bug-analysis', 'user-story', 'product-management']
            }
        }
        
        # Extrair system_prompt das mensagens
        for message in messages:
            if hasattr(message, 'prompt'):
                template = message.prompt.template if hasattr(message.prompt, 'template') else str(message.prompt)
                if 'system' in str(type(message)).lower() or 'SystemMessage' in str(type(message)):
                    prompt_data['bug_to_user_story_v1']['system_prompt'] = template
                elif 'human' in str(type(message)).lower() or 'HumanMessage' in str(type(message)):
                    prompt_data['bug_to_user_story_v1']['user_prompt'] = template
        
        # Se não conseguiu extrair, usar o formato string direto
        if not prompt_data['bug_to_user_story_v1']['system_prompt']:
            prompt_str = str(prompt)
            prompt_data['bug_to_user_story_v1']['system_prompt'] = prompt_str
        
        # Salvar em arquivo YAML
        output_path = Path(__file__).parent.parent / 'prompts' / 'bug_to_user_story_v1.yml'
        print(f"💾 Salvando prompt em: {output_path}")
        
        if save_yaml(prompt_data, str(output_path)):
            print(f"✅ Prompt salvo com sucesso em: {output_path}")
            print(f"\n📄 Conteúdo extraído:")
            print(f"   - Description: {prompt_data['bug_to_user_story_v1']['description']}")
            print(f"   - Version: {prompt_data['bug_to_user_story_v1']['version']}")
            print(f"   - Tags: {', '.join(prompt_data['bug_to_user_story_v1']['tags'])}")
            return 0
        else:
            print("❌ Erro ao salvar arquivo YAML")
            return 1
            
    except Exception as e:
        print(f"❌ Erro ao fazer pull do prompt: {e}")
        print(f"   Tipo do erro: {type(e).__name__}")
        return 1


def main():
    """Função principal"""
    return pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())
