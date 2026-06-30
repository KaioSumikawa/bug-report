## 1) Missão: O Sistema do Cinema

- Arquivo: `cinema.py`
- Problemas encontrados:
	- Meia-entrada aplicava 10% de desconto em vez de 50% (linha original: `valor_total = valor_total * 0.90`).
	- Cálculo do troco estava invertido (`troco = valor_total - dinheiro`) o que gerava trocos negativos.
- Ações realizadas:
	- Corrigi o desconto para 50%: `valor_total = valor_total * 0.5`.
	- Corrigi o cálculo do troco: `troco = dinheiro - valor_total`.
	- Formatei as saídas para duas casas decimais.
- Testes rápidos realizados (simulação):
	- Entrada: 2 ingressos, não estudante, R$50 -> total R$40.00, troco R$10.00
	- Entrada: 1 ingresso, estudante, R$10 -> total R$10.00, troco R$0.00

Status: Corrigido.