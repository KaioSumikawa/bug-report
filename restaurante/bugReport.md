## 4) Missão: O restaurante

- Arquivo: `restaurante/restaurante.py`
- Problemas encontrados:
    - Bug de divisão por zero. Quando o usuário inferia 0 pessoas para dividir a conta, o programa lançava exceção `ZeroDivisionError`.
    - O código aceitava qualquer número inteiro válido para o campo "número de pessoas", incluindo 0, causando um crash ao tentar dividir por zero.
- Ações realizadas: 
    - Adicionar validação explícita para `pessoas > 0`
- Testes rápidos realizados:
    - Valor: 100
    - Taxa garçom: N
    - Pessoas: 0
    - Resultado: "Número de pessoas deve ser maior que zero."

Status: Corrigido.