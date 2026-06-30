## 6) Missão: O supermercado

- Arquivo: `supermercado/supermercado.py`
- Problemas encontrados:
    - O sistema permitia que o cliente pagasse um valor menor que o total da compra, calculando um troco negativo.
    - O código realizava o cálculo do troco sem validar se o pagamento recebido era suficiente para cobrir o valor total da compra
- Ações realizadas: 
    - Adicionada validação para impedir que o sistema calcule troco quando o pagamento for inferior ao total da compra.
- Testes rápidos realizados:
    - Pagamento igual ao total | Troco correto
    - Pagamento maior que o total | Troco correto 
    - Pagamento menor que o total | Troco incorreto


Status: Corrigido.


