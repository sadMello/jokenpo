import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    while True:
        # Escolha do jogador
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ").lower()

        if jogador == 'sair':
            print("Até logo!")
            break

        if jogador not in opcoes:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue