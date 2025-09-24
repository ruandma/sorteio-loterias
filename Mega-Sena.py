import random

def gerar_megasena():
    # Sorteia 6 números únicos entre 1 e 60
    numeros = random.sample(range(1, 61), 6)
    # Ordena para ficar mais organizado
    return sorted(numeros)

# Gerando um jogo
jogo = gerar_megasena()
print("Seu jogo da Mega-Sena:", jogo)
