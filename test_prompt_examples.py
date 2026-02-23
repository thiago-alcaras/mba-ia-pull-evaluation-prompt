"""
Exemplos de uso do prompt otimizado bug_to_user_story_v2.

Este script demonstra como usar o prompt v2 com o Google Gemini
para converter diferentes tipos de bug reports em User Stories.
"""

import os
from dotenv import load_dotenv
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Configurar LLM (Google Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv('GOOGLE_API_KEY')
)

def test_prompt_with_example(bug_report: str, example_name: str):
    """
    Testa o prompt v2 com um exemplo de bug report.
    
    Args:
        bug_report: Texto do bug report
        example_name: Nome do exemplo para display
    """
    print("\n" + "=" * 70)
    print(f"🐛 EXEMPLO: {example_name}")
    print("=" * 70)
    print("\n📝 Bug Report de Entrada:")
    print("-" * 70)
    print(bug_report)
    print("-" * 70)
    
    try:
        # Pull do prompt v2 do LangSmith Hub
        # Nota: Se ainda não fez push, isso falhará. Use o prompt local.
        username = os.getenv('USERNAME_LANGSMITH_HUB', 'leonanluppi')
        prompt = hub.pull(f"{username}/bug_to_user_story_v2")
        
        # Invocar o prompt com o bug report
        chain = prompt | llm
        result = chain.invoke({"bug_report": bug_report})
        
        print("\n✅ User Story Gerada:")
        print("-" * 70)
        print(result.content)
        print("-" * 70)
        
    except Exception as e:
        print(f"\n❌ Erro ao processar: {e}")
        print("\nDica: Certifique-se de que:")
        print("1. Fez push do prompt v2 com: python src/push_prompts.py")
        print("2. LANGCHAIN_API_KEY está correto no .env")
        print("3. GOOGLE_API_KEY está correto no .env")


def main():
    """Executa exemplos de teste."""
    
    print("\n" + "=" * 70)
    print("🧪 TESTANDO PROMPT OTIMIZADO: bug_to_user_story_v2")
    print("=" * 70)
    
    # Exemplo 1: Bug de Performance
    test_prompt_with_example(
        bug_report="""
        o app ta super lento quando eu tento abrir a lista de produtos
        demora uns 10 segundos pra carregar e as vezes trava tudo
        uso no celular samsung galaxy s21
        """,
        example_name="Bug de Performance"
    )
    
    # Exemplo 2: Bug de UI
    test_prompt_with_example(
        bug_report="""
        quando clico no botão salvar no formulário nada acontece
        testei no chrome e firefox
        as vezes funciona as vezes não, muito aleatório
        """,
        example_name="Bug de Interface/UI"
    )
    
    # Exemplo 3: Bug de Lógica de Negócio
    test_prompt_with_example(
        bug_report="""
        coloquei cupom de desconto NATAL30 mas na hora de pagar veio valor cheio
        o site disse que ia dar 30% off mas não deu
        """,
        example_name="Bug de Lógica de Negócio"
    )
    
    # Exemplo 4: Bug Vago (testa robustez)
    test_prompt_with_example(
        bug_report="""
        tem um erro no sistema
        não funciona direito
        """,
        example_name="Bug Vago (Edge Case)"
    )
    
    print("\n" + "=" * 70)
    print("✅ Testes concluídos!")
    print("=" * 70)
    print("\n📊 Observe:")
    print("   - Chain of Thought sendo aplicado")
    print("   - Estrutura consistente (Como/Quero/Para que)")
    print("   - Critérios de aceite SMART")
    print("   - Tratamento de casos vagos")


if __name__ == "__main__":
    # Verificar configurações
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ ERRO: GOOGLE_API_KEY não configurado no .env")
        print("Configure antes de executar este script.")
        exit(1)
    
    if not os.getenv('LANGCHAIN_API_KEY'):
        print("⚠️  AVISO: LANGCHAIN_API_KEY não configurado")
        print("Necessário para pull do prompt do LangSmith Hub")
    
    main()
