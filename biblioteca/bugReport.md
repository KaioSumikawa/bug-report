## 3) Missão: A Biblioteca

- Arquivo: `biblioteca/biblioteca.py`
- Problemas encontrados:
	- Valores-limite estavam incorretos: idades exatamente 12 e 18 caíam no `else` e eram tratadas como inválidas.
	- Não havia validação para idades negativas.
- Ações realizadas:
	- Corrigi as comparações para incluir limites: `idade <= 12` -> Infantil; `13 <= idade <= 17` -> Jovem; `idade >= 18` -> Adulto.
	- Adicionei validação explícita para idades negativas (`idade < 0` -> erro).
- Testes rápidos realizados:
	- 11 -> INFANTIL
	- 12 -> INFANTIL
	- 13 -> JOVEM
	- 17 -> JOVEM
	- 18 -> ADULTA
	- -1 -> ERRO

Status: Corrigido.


