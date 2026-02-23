"""
Script auxiliar para testar pull de prompts do LangSmith e descobrir username.
"""

import os
from dotenv import load_dotenv
from langchain import hub

load_dotenv()

print("=" * 60)
print("🔍 DESCOBRINDO SEU USERNAME NO LANGSMITH HUB")
print("=" * 60)

# Verificar API key
api_key = os.getenv('LANGCHAIN_API_KEY')
if not api_key:
    print("\n❌ LANGCHAIN_API_KEY não encontrado no .env")
    exit(1)

print(f"\n✅ API Key configurada: {api_key[:20]}...")

# Tentar diferentes formatos para descobrir o username
print("\n📝 Vamos tentar descobrir seu username...")
print("\nFormato 1: Tentando 'test' (nome do seu prompt)")

try:
    prompt = hub.pull("test:b35d154b")
    print("✅ Conseguiu fazer pull de: test:b35d154b")
    print("   Isso significa que 'test' pode ser o nome ou há alguma configuração especial")
except Exception as e:
    print(f"❌ Erro: {e}")

print("\n" + "=" * 60)
print("\n📋 INSTRUÇÕES PARA ENCONTRAR SEU USERNAME:")
print("\n1. Acesse: https://smith.langchain.com/prompts")
print("2. Localize o prompt 'test' que você criou")
print("3. Clique no prompt")
print("4. Procure por 'Owner' ou o caminho completo")
print("5. O formato será: USERNAME/test")
print("\nExemplo:")
print("   Se você vê: 'joaosilva/test'")
print("   Seu username é: joaosilva")
print("\n" + "=" * 60)

print("\n💡 ALTERNATIVA RÁPIDA:")
print("\n1. Acesse: https://smith.langchain.com/settings")
print("2. Na seção 'Profile', você verá seu username")
print("\n" + "=" * 60)
