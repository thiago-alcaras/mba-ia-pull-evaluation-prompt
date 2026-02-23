"""
Script principal para executar todo o pipeline do projeto MBA.

Este script executa automaticamente:
1. Pull do prompt v1 do LangSmith
2. Validação do prompt v2 com testes
3. Push do prompt v2 para o LangSmith

Uso:
    python run_pipeline.py [--skip-tests] [--skip-pull] [--skip-push]
"""

import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import argparse

load_dotenv()

def print_header(text):
    """Imprime cabeçalho formatado."""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60 + "\n")

def run_command(command, description):
    """Executa um comando e retorna o status."""
    print(f"▶️  {description}")
    print(f"   Comando: {command}")
    print()
    
    result = subprocess.run(command, shell=True, capture_output=False)
    
    if result.returncode != 0:
        print(f"\n❌ ERRO: {description} falhou com código {result.returncode}")
        return False
    
    print(f"\n✅ {description} concluído com sucesso!")
    return True

def main():
    parser = argparse.ArgumentParser(description="Pipeline completo do projeto MBA")
    parser.add_argument('--skip-tests', action='store_true', help='Pula execução dos testes')
    parser.add_argument('--skip-pull', action='store_true', help='Pula pull do prompt v1')
    parser.add_argument('--skip-push', action='store_true', help='Pula push do prompt v2')
    
    args = parser.parse_args()
    
    print_header("🚀 Pipeline de Otimização de Prompts - MBA IA")
    
    success = True
    
    # Passo 1: Pull do prompt v1
    if not args.skip_pull:
        print_header("📥 PASSO 1: Pull do Prompt V1 do LangSmith")
        success = run_command("python src/pull_prompts.py", "Pull do prompt v1")
        
        if not success:
            print("\n⚠️  Você pode continuar mesmo com erro no pull (se já tiver o arquivo v1)")
            response = input("Deseja continuar? (s/n): ").lower()
            if response != 's':
                return 1
    else:
        print("\n⏭️  Pulando pull do prompt v1 (--skip-pull)")
    
    # Passo 2: Testes do prompt v2
    if not args.skip_tests:
        print_header("🧪 PASSO 2: Executando Testes de Validação do Prompt V2")
        success = run_command("python -m pytest tests/test_prompts.py -v", "Testes do prompt v2")
        
        if not success:
            print("\n❌ Testes falharam! Verifique os erros acima.")
            print("Corrija o prompt v2 antes de fazer push.")
            return 1
    else:
        print("\n⏭️  Pulando testes (--skip-tests)")
    
    # Passo 3: Push do prompt v2
    if not args.skip_push:
        print_header("📤 PASSO 3: Push do Prompt V2 para o LangSmith")
        
        print("⚠️  ATENÇÃO: Você está prestes a fazer push PÚBLICO do prompt v2")
        print("   Isso criará ou atualizará: leonanluppi/bug_to_user_story_v2")
        print()
        response = input("Confirma o push? (s/n): ").lower()
        
        if response == 's':
            success = run_command("python src/push_prompts.py", "Push do prompt v2")
            
            if not success:
                print("\n❌ Push falhou! Verifique:")
                print("   1. LANGCHAIN_API_KEY está correto no .env")
                print("   2. USERNAME_LANGSMITH_HUB está correto no .env")
                return 1
        else:
            print("\n⏭️  Push cancelado pelo usuário")
    else:
        print("\n⏭️  Pulando push (--skip-push)")
    
    # Resumo final
    print_header("🎉 Pipeline Concluído!")
    
    print("📋 Resumo das ações:")
    print(f"   {'✅' if not args.skip_pull else '⏭️ '} Pull do prompt v1")
    print(f"   {'✅' if not args.skip_tests else '⏭️ '} Testes de validação")
    print(f"   {'✅' if not args.skip_push else '⏭️ '} Push do prompt v2")
    
    print("\n📚 Próximos passos sugeridos:")
    print("   1. Acesse o LangSmith Hub para ver seu prompt publicado")
    print("   2. Execute avaliações comparando v1 vs v2")
    print("   3. Documente as melhorias nas métricas")
    print("   4. Teste o prompt com diferentes bug reports")
    
    print("\n🔗 Links úteis:")
    print("   - LangSmith Hub: https://smith.langchain.com/hub")
    print("   - Seu prompt: https://smith.langchain.com/hub/leonanluppi/bug_to_user_story_v2")
    print("   - Guia completo: GUIA_EXECUCAO.md")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
