## 2) Missão: O Estacionamento

- Arquivo: `estacionamento/estacionamento.py`
- Problemas encontrados:
	- Se `saida == entrada` o cálculo produzia 0 horas (cobrança R$0,00) — deveria haver cobrança mínima de 1 hora.
	- Se `saida < entrada` (digitação incorreta ou travessia de meia-noite), o cálculo gerava horas/valor negativo.
- Ações realizadas:
	- Adicionei validação: se `saida < entrada` exibe mensagem de erro e solicita verificação (não calcula valor negativo).
	- Se `saida == entrada` aplica cobrança mínima de 1 hora e informa o usuário.
- Testes rápidos realizados (execução automatizada com entradas simuladas):
	- entrada=14, saida=14 -> Cobrança mínima aplicada, total R$5.00
	- entrada=16, saida=14 -> Mensagem de erro sobre saída anterior à entrada
	- entrada=14, saida=15 -> total R$5.00 (normal)

Status: Corrigido.