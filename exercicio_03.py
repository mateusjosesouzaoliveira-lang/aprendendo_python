preco_original = 89.90
desconto_percentual = 15 

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto
compra_total= preco_final * 3

print(f" O valor do desconto é de; {valor_desconto:.2f}")
print(f"O valor filnal é de: {preco_final:.2f}")
print(f"O valotal total da compra é de : {compra_total}")