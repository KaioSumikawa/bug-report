print("--- BILHETERIA DO CINEMA ---")
qtd = int(input("Quantos ingressos deseja comprar? (R$ 20,00 cada): "))
estudante = input("Você é estudante? (s/n): ")
dinheiro = float(input("Qual valor em dinheiro você entregou?: "))

valor_total = qtd * 20

# BUG 1: A meia entrada dá 10% de desconto em vez de 50%
if estudante.lower() == 's':
    valor_total = valor_total * 0.5
    print(f"Meia entrada aplicada. Novo total: R$ {valor_total:.2f}")
else:
    print(f"Total: R$ {valor_total:.2f}")

# BUG 2: Cálculo do troco 
troco = dinheiro - valor_total
print(f"Seu troco é: R$ {troco:.2f}")
print("Bom filme!")
