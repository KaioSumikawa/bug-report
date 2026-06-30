## 5) Missão: A academia 

- Arquivo: `academia/academia.py`
- Problemas encontrados:
    - Encontrado bug de valor-limite (boundary condition) no arquivo que impedia cadastro de alunos com exatamente 14 anos de idade, contradizendo a mensagem de erro que dizia "idade mínima é 14 anos".
    - O código utilizava comparação **estrita** (`>`) em vez de **inclusiva** (`>=`):
- Ações realizadas:
    - Trocar `if idade > 14:` por `if idade >= 14:`
- Testes rápidos realizados:
    - Idade 13: Cadastro negado ✅
    - Idade 14: Cadastro negado ❌ (BUG CORRIGIDO)
    - Idade 15: Cadastro aprovado ✅

Status: Corrigido.

