preco = 99.98765

# Preco com 2 casas decimais
preco_2_decimais = f"R$ {preco:.2f}"

# Preco sem casas decimais
preco_sem_decimais = f"R$ {preco:.0f}"

# calculando descondo de 10 %
desconto = preco * 0.10
preco_final = preco - desconto
preco_final_formatado = f"R$ {preco_final:.2f}"

print(f"Preço com 2 decimais: {preco_2_decimais}")
print(f"Preço sem decimais: {preco_sem_decimais}")
print(f"Preço com 10% de desconto: {preco_final_formatado}")
