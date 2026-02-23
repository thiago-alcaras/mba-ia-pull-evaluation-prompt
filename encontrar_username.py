"""
Script para descobrir o username correto no LangSmith Hub.
"""

import os
from dotenv import load_dotenv
from langchain import hub
from langsmith import Client

load_dotenv()

print("=" * 70)
print("🔍 DESCOBRINDO SEU USERNAME NO LANGSMITH HUB")
print("=" * 70)

try:
    # Criar cliente LangSmith
    client = Client()
    
    print("\n✅ Conectado ao LangSmith com sucesso!")
    
    # Tentar obter informações da conta
    print("\n📋 Buscando informações da sua conta...")
    
    # Listar seus prompts
    print("\n📝 Seus prompts no LangSmith Hub:")
    print("-" * 70)
    
    try:
        # Tentar listar prompts do usuário
        # Note: A API pode variar, vamos tentar diferentes abordagens
        
        # Tentativa 1: Pull do prompt que você criou
        print("\n🔍 Tentando fazer pull do seu prompt 'test'...")
        prompt = hub.pull("test:b35d154b")
        print("✅ Pull bem-sucedido!")
        
        # Tentar extrair informações
        if hasattr(prompt, 'metadata'):
            print(f"\nMetadados do prompt: {prompt.metadata}")
        
        print("\n" + "=" * 70)
        print("✅ SEU PROMPT FOI ENCONTRADO!")
        print("=" * 70)
        
        print("\n📝 Para descobrir seu username exato:")
        print("\n1. Acesse: https://smith.langchain.com/prompts")
        print("2. Você verá seu prompt 'test' listado")
        print("3. Clique nele")
        print("4. Na URL ou na página, você verá algo como:")
        print("   https://smith.langchain.com/hub/SEU_USERNAME/test")
        print("\n5. Copie o SEU_USERNAME")
        
        print("\n" + "=" * 70)
        print("💡 ALTERNATIVA MAIS RÁPIDA:")
        print("=" * 70)
        print("\n1. Acesse: https://smith.langchain.com/settings")
        print("2. Procure por 'LangChain Hub Handle' ou 'Username'")
        print("3. Esse é o seu username!")
        
        print("\n" + "=" * 70)
        print("⚙️  DEPOIS DE DESCOBRIR:")
        print("=" * 70)
        print("\n1. Abra o arquivo .env")
        print("2. Edite a linha:")
        print("   USERNAME_LANGSMITH_HUB=leonanluppi")
        print("\n3. Substitua 'leonanluppi' pelo SEU username")
        print("\n4. Execute novamente:")
        print("   python src/push_prompts.py")
        
    except Exception as e:
        print(f"\n❌ Erro ao listar prompts: {e}")
        print("\n💡 Mas não se preocupe! Siga as instruções acima.")
    
except Exception as e:
    print(f"\n❌ Erro ao conectar: {e}")
    print("\n🔧 Verifique se LANGCHAIN_API_KEY está correto no .env")

print("\n" + "=" * 70)
