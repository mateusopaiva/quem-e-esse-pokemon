import os
import platform
import time
from utils.pokemon import buscar_pokemon_aleatorio, download_imagem_pokemon, imagem_para_ascii
from utils.traducao_tipos import traducao_tipos

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("\n=== Instruções do Jogo ===")
    print("Olá, Treinador Pokémon!")
    print("Prepare-se para um desafio emocionante: eu pensei em um Pokémon da 1ª geração, e você deve adivinhar qual é.")
    print("Você terá dicas valiosas, incluindo uma imagem ASCII do Pokémon para ajudar.")
    print("Vamos ver se você consegue adivinhar quem é esse Pokémon. Boa sorte!\n")

    
    print("=== Quem é esse Pokémon? ===")
    print("1. Iniciar o jogo")
    print("2. Sair")
    opcao = input("Escolha uma opção (1 ou 2): ")
    return opcao

def traduzir_tipo(tipo_ingles):
    return traducao_tipos.get(tipo_ingles, tipo_ingles.title())

def jogar():
    pokemon = buscar_pokemon_aleatorio()
    imagem_url = pokemon['sprites']['front_default']
    nome_pokemon = pokemon['name']

    download_imagem_pokemon(imagem_url, nome_pokemon)

    limpar_tela()

    print("🎉 Preparado para o desafio Pokémon? 🎉")
    print("Vamos lá! Quem é esse Pokémon? ")

    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        resposta = input("É o ... ").lower()
        tentativas += 1

        if resposta == nome_pokemon:
            print(f"\n🎉 Parabéns! Você acertou! É o {nome_pokemon.upper()}! 🎉")
            return
        elif tentativas == 1:
            print("\n🔍 Dica 1: ")
            tipo_pokemon = traduzir_tipo(pokemon['types'][0]['type']['name'])
            print(f"Esse Pokémon é do tipo {tipo_pokemon}.")
        elif tentativas == 2:
            print("\n🔍 Dica 2: ")
            print(f"O número da Pokedex deste é {pokemon['id']}.")
        elif tentativas == 3:
            imagem_para_ascii(nome_pokemon)
            print("\n🔍 Dica Final: ")
            print("Agora não tem como errar: ")
            resposta = input("Quem é esse Pokémon? ").lower()
            if resposta == nome_pokemon:
                print(f"\n🎉 Parabéns! Você acertou! É o {nome_pokemon.upper()}! 🎉")
            else:
                print(f"\n😞 Que pena! Você errou. O Pokémon era {nome_pokemon.upper()}.")
            return 

def menu_jogo():
    while True:
        opcao = mostrar_menu()
        if opcao == '1':
            while True:
                limpar_tela()
                jogar()
                opcao_final = input("\nQuer desafiar novamente? (s/n): ").lower()
                if opcao_final != 's':
                    print("Obrigado por jogar! Espero que você tenha se divertido!")
                    print("Voltaremos em breve com novos desafios Pokémon.")
                    time.sleep(5)
                    return
        elif opcao == '2':
            print("Até logo, Treinador! Que sua jornada Pokémon seja incrível!")
            time.sleep(5)
            break
        else:
            print("🚫 Opção inválida. Por favor, escolha 1 ou 2 para continuar.")

if __name__ == "__main__":
    menu_jogo()
