print("--- GESTOR DE ESTACIONAMENTO ---")
print("Valor fixo: R$ 5,00 a hora")

entrada = int(input("Que horas o carro entrou? (apenas a hora ex: 14): "))
saida = int(input("Que horas o carro saiu? (ex: 16): "))

if saida < entrada:
    print("Erro: a hora de saída não pode ser anterior à hora de entrada.")
    print("Por favor, verifique os valores e tente novamente.")
else:
    horas_estacionadas = saida - entrada
    if horas_estacionadas == 0:
        horas_estacionadas = 1
        print("Cobrança mínima de 1 hora aplicada.")

    valor_pagar = horas_estacionadas * 5
    print(f"O carro ficou {horas_estacionadas} horas.")
    print(f"Total a pagar: R$ {valor_pagar:.2f}")
