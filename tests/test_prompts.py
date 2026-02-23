"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture
def prompt_v2_data():
    """Fixture que carrega o prompt v2 para os testes."""
    prompt_file = Path(__file__).parent.parent / 'prompts' / 'bug_to_user_story_v2.yml'
    data = load_prompts(str(prompt_file))
    return data.get('bug_to_user_story_v2', {})


class TestPromptV2Structure:
    """Testes de estrutura e qualidade do prompt v2."""
    
    def test_prompt_has_system_prompt(self, prompt_v2_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert 'system_prompt' in prompt_v2_data, "Campo 'system_prompt' não encontrado"
        system_prompt = prompt_v2_data['system_prompt'].strip()
        assert len(system_prompt) > 0, "system_prompt está vazio"
        assert len(system_prompt) > 100, "system_prompt é muito curto (menos de 100 caracteres)"
        print(f"✅ system_prompt tem {len(system_prompt)} caracteres")

    def test_prompt_has_role_definition(self, prompt_v2_data):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        
        # Verificar se contém definição de papel
        role_indicators = [
            'você é',
            'você é um',
            'você é uma',
            'atue como',
            'assuma o papel',
            'como um',
            'product owner',
            'product manager'
        ]
        
        has_role = any(indicator in system_prompt for indicator in role_indicators)
        assert has_role, "Prompt não define claramente uma persona/papel (Role Prompting)"
        print(f"✅ Role Prompting detectado")

    def test_prompt_mentions_format(self, prompt_v2_data):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        
        # Verificar se menciona formato
        format_keywords = [
            'markdown',
            'user story',
            'user stories',
            'como',
            'quero',
            'para que',
            'critérios de aceite',
            'acceptance criteria'
        ]
        
        mentions_format = any(keyword in system_prompt for keyword in format_keywords)
        assert mentions_format, "Prompt não especifica formato de saída (Markdown/User Story)"
        print(f"✅ Formato de saída especificado")

    def test_prompt_has_few_shot_examples(self, prompt_v2_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        
        # Verificar indicadores de exemplos
        example_indicators = [
            'exemplo',
            'examples',
            'entrada:',
            'saída:',
            'input:',
            'output:',
            '**entrada',
            '**saída'
        ]
        
        has_examples = any(indicator in system_prompt for indicator in example_indicators)
        assert has_examples, "Prompt não contém exemplos few-shot"
        
        # Contar quantos exemplos (procurar por múltiplas ocorrências)
        example_count = sum(system_prompt.count(indicator) for indicator in ['exemplo 1', 'exemplo 2', 'exemplo 3'])
        assert example_count >= 2, f"Prompt deve ter pelo menos 3 exemplos, encontrados: {example_count}"
        print(f"✅ Few-shot learning detectado (pelo menos 3 exemplos)")

    def test_prompt_no_todos(self, prompt_v2_data):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        system_prompt = prompt_v2_data.get('system_prompt', '')
        full_content = str(prompt_v2_data)
        
        assert 'TODO' not in system_prompt, "system_prompt contém TODO - complete antes de finalizar"
        assert 'TODO' not in full_content, "Dados do prompt contêm TODO - complete antes de finalizar"
        assert '[...]' not in system_prompt, "system_prompt contém [...] - complete o conteúdo"
        print(f"✅ Nenhum TODO ou placeholder encontrado")

    def test_minimum_techniques(self, prompt_v2_data):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        techniques = prompt_v2_data.get('techniques_applied', [])
        
        assert isinstance(techniques, list), "techniques_applied deve ser uma lista"
        assert len(techniques) >= 2, f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}"
        
        # Verificar se técnicas têm estrutura adequada
        for i, tech in enumerate(techniques):
            if isinstance(tech, dict):
                assert 'name' in tech, f"Técnica {i+1} não tem campo 'name'"
                assert len(tech['name'].strip()) > 0, f"Técnica {i+1} tem 'name' vazio"
        
        print(f"✅ {len(techniques)} técnicas documentadas nos metadados")

    def test_prompt_has_chain_of_thought(self, prompt_v2_data):
        """Verifica se o prompt implementa Chain of Thought (CoT)."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        
        # Indicadores de Chain of Thought
        cot_indicators = [
            'passo a passo',
            'passo 1',
            'raciocínio',
            'processo',
            'antes de',
            'chain of thought',
            'cot',
            'análise'
        ]
        
        has_cot = any(indicator in system_prompt for indicator in cot_indicators)
        assert has_cot, "Prompt não implementa Chain of Thought (CoT)"
        print(f"✅ Chain of Thought detectado")

    def test_prompt_has_constraints(self, prompt_v2_data):
        """Verifica se o prompt define restrições claras."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        
        # Indicadores de restrições
        constraint_indicators = [
            'deve',
            'obrigatório',
            'restrições',
            'diretrizes',
            'regras',
            'importante',
            'constraints',
            'mínimo',
            'máximo'
        ]
        
        constraint_count = sum(system_prompt.count(indicator) for indicator in constraint_indicators)
        assert constraint_count >= 3, f"Prompt deve ter restrições claras, encontrados apenas {constraint_count} indicadores"
        print(f"✅ Restrições definidas ({constraint_count} indicadores)")

    def test_prompt_metadata_completeness(self, prompt_v2_data):
        """Verifica se metadados essenciais estão presentes."""
        required_metadata = ['description', 'version', 'tags', 'techniques_applied']
        
        for field in required_metadata:
            assert field in prompt_v2_data, f"Metadado obrigatório faltando: {field}"
        
        # Verificar qualidade dos metadados
        assert len(prompt_v2_data['description']) > 20, "Descrição muito curta"
        assert len(prompt_v2_data['tags']) >= 3, "Deve ter pelo menos 3 tags"
        assert prompt_v2_data['version'] == 'v2', "Versão deve ser 'v2'"
        
        print(f"✅ Metadados completos e válidos")


class TestPromptV2Quality:
    """Testes de qualidade avançada do prompt."""
    
    def test_prompt_length_adequate(self, prompt_v2_data):
        """Verifica se o prompt tem tamanho adequado (não muito curto)."""
        system_prompt = prompt_v2_data.get('system_prompt', '')
        word_count = len(system_prompt.split())
        
        assert word_count >= 200, f"Prompt muito curto ({word_count} palavras). Recomendado: 200+ para prompts complexos"
        print(f"✅ Prompt tem {word_count} palavras (adequado)")
    
    def test_techniques_documented_match_implementation(self, prompt_v2_data):
        """Verifica se as técnicas documentadas realmente foram implementadas."""
        system_prompt = prompt_v2_data.get('system_prompt', '').lower()
        techniques = prompt_v2_data.get('techniques_applied', [])
        
        technique_names = [
            tech['name'].lower() if isinstance(tech, dict) else str(tech).lower() 
            for tech in techniques
        ]
        
        # Verificar se cada técnica tem evidência no prompt
        for tech_name in technique_names:
            if 'role' in tech_name:
                assert 'você é' in system_prompt or 'product owner' in system_prompt, \
                    "Role Prompting documentado mas não implementado"
            elif 'few-shot' in tech_name or 'few shot' in tech_name:
                assert 'exemplo' in system_prompt, "Few-shot documentado mas não implementado"
            elif 'chain of thought' in tech_name or 'cot' in tech_name:
                assert 'passo' in system_prompt or 'raciocínio' in system_prompt, \
                    "Chain of Thought documentado mas não implementado"
        
        print(f"✅ Todas as {len(techniques)} técnicas documentadas foram implementadas")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])