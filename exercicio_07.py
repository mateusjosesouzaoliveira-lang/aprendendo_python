frase = "Python é uma linguagem de programação"

# Verificando se comtem "Python"
contem_Python = "Python" in frase

# Verificando tamaho
tamanho = len(frase)

# Maiscula
texto_maiuscula = frase.upper()

# Substituição
frase_substituida = frase.replace("programação", "codigo")

print(f"contem 'Python': {contem_Python}" )
print(f"O tamanho é: {tamanho}")
print(f"Maicusla: {texto_maiuscula}")
print(f"Frase Substituida: {frase_substituida}")