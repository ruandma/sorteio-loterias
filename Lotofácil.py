import random

def gerar_lotofacil():
    # Escolhe 15 números únicos de 1 a 25
    numeros = random.sample(range(1, 26), 15)
    # Ordena para ficar bonitinho
    return sorted(numeros)

# Gerando um jogo
jogo = gerar_lotofacil()
print("Seu jogo da Lotofácil:", jogo)