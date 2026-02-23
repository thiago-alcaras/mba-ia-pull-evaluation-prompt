"""
Script de verificação rápida do ambiente.
Testa se as dependências principais estão instaladas.
"""

import sys

print("=" * 60)
print("🔍 VERIFICAÇÃO DO AMBIENTE - PROJETO MBA")
print("=" * 60)

# Verificar versão Python
print(f"\n✅ Python {sys.version}")

# Testar imports essenciais
errors = []

try:
    import langchain
    print(f"✅ langchain {langchain.__version__}")
except ImportError as e:
    errors.append(f"❌ langchain não instalado: {e}")
    print(f"❌ langchain não instalado")

try:
    import langsmith
    print(f"✅ langsmith instalado")
except ImportError as e:
    errors.append(f"❌ langsmith não instalado: {e}")
    print(f"❌ langsmith não instalado")

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    print(f"✅ langchain-google-genai instalado")
except ImportError as e:
    errors.append(f"❌ langchain-google-genai não instalado: {e}")
    print(f"❌ langchain-google-genai não instalado")

try:
    import yaml
    print(f"✅ pyyaml instalado")
except ImportError as e:
    errors.append(f"❌ pyyaml não instalado: {e}")
    print(f"❌ pyyaml não instalado")

try:
    import pytest
    print(f"✅ pytest instalado")
except ImportError as e:
    errors.append(f"❌ pytest não instalado: {e}")
    print(f"❌ pytest não instalado")

try:
    from dotenv import load_dotenv
    print(f"✅ python-dotenv instalado")
except ImportError as e:
    errors.append(f"❌ python-dotenv não instalado: {e}")
    print(f"❌ python-dotenv não instalado")

print("\n" + "=" * 60)

if errors:
    print("⚠️  ATENÇÃO: Algumas dependências estão faltando!")
    print("\n📦 Execute para instalar:")
    print("   pip install -r requirements.txt")
    print("\n❌ Erros encontrados:")
    for error in errors:
        print(f"   {error}")
    sys.exit(1)
else:
    print("✅ TODAS AS DEPENDÊNCIAS INSTALADAS!")
    print("\n🚀 Próximos passos:")
    print("   1. Configure o .env com suas API keys")
    print("   2. Execute: python run_pipeline.py")
    print("   3. Ou execute os testes: pytest tests/test_prompts.py -v")
    sys.exit(0)
