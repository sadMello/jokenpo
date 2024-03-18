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
        
        # Escolha do computador
        computador = random.choice(opcoes)
        
        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {computador}")
                # Verificando o vencedor
        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        print("---------------------")

# Chamada da função para jogar
jogar()