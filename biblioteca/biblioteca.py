print("--- SISTEMA DE EMPRÉSTIMO DA BIBLIOTECA ---")
print("Regras: Infantil (0-12) | Jovem (13-17) | Adulto (18+)")

idade = int(input("Qual a sua idade?: "))

if idade < 0:
    print("ERRO: Idade inválida para empréstimo.")
elif idade <= 12:
    print("Você pode acessar a seção INFANTIL.")
elif 13 <= idade <= 17:
    print("Você pode acessar a seção JOVEM.")
else:
    print("Você pode acessar a seção ADULTA.")
