media = 85.5
frequencia = 80
media_minima = 7.0
frequencia_minima = 75

# Verificação de aprovação

media_ok = media >= media_minima
frequencia_ok = frequencia >= frequencia_minima
aprovado = media_ok and frequencia_ok

print(f"Media: {media}")
print(f"Frequencia: {frequencia_minima}")
print(f"Aprovado: {aprovado}")