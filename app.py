#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def escolha_do_computador():
    """Retorna a escolha do computador de forma aleatória."""
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def resultado(jogador, computador):
    """Determina o vencedor da rodada."""
    if jogador == computador:
        return "empate"
    if (jogador == "pedra" and computador == "tesoura") or \
       (jogador == "tesoura" and computador == "papel") or \
       (jogador == "papel" and computador == "pedra"):
        return "vitoria"
    return "derrota"


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def main():
    vitorias = 0
    rodadas = 0
    
    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()
        
        # Valida a escolha do jogador
        if escolha_jogador not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
            continue
        
        escolha_computador = escolha_do_computador()
        res = resultado(escolha_jogador, escolha_computador)
        
        if res == "vitoria":
            print(f"Você ganhou! {escolha_jogador} vence {escolha_computador}.")
            vitorias += 1
        elif res == "derrota":
            print(f"Você perdeu! {escolha_computador} vence {escolha_jogador}.")
        else:
            print(f"Empate! Ambos escolheram {escolha_jogador}.")
        
        rodadas += 1
        jogar_novamente = input("Quer jogar novamente? (sim/nao) ").lower().strip()
        
        if jogar_novamente != "sim":
            break
    
    print(f"\nVocê jogou {rodadas} rodadas e ganhou {vitorias} vezes.")

if __name__ == "__main__":
    main()