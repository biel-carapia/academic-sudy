# LIsta de notas dos estudantes 
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arrendondar a média para duas casas decimais
arrendondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arrendondada = arrendondar_media(media)

# Verificar se os estudantes foram aprovados
situacao = "Aprovado" if media_arrendondada >= 7 else "Reprovado"



