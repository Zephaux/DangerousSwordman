import random, os, time

def rolar_dado(): # "dados" do jogo pode ser tanto pra dano, quanto pra ataque
    return random.randint(0, 10)

def d20():
    return random.randint(1,20)
def escolherOpcao():
    while True:  # validaçao da ação
        escolher_acao = input("O que gostaria de fazer \n[1] Atacar\n[2] Defender\n[3] Item\n[4]Status\n")

        match escolher_acao:
            case '1':
                break
            case '2':
                break
            case '3':
                break
            case '4':
                break
            case _:
                print("Por favor selecione uma opção válida!")
                continue

    return escolher_acao


def jogo():
    nome = input('Digite seu nome: ')
    player = {'Nome': nome, 'Vida': 100,'Ataque': 40, 'Defesa': 20}
    mob = {'Nome': 'kara di kwo', 'Vida': 100,'Ataque': 40, 'Defesa': 20}

    player1 = None # variável para ser linkada com o dicionário do player 1
    player2 = None # variável para ser linkada com o dicionário do player 2


    # for c in range(0,1): #for usado para definir quem vai começar atacando
    #     player_dice = rolar_dado()
    #     mob_dice = rolar_dado()
    #
    #     if player_dice > mob_dice:
    #         player1 = player
    #         player2 = mob
    #     else:
    #         player1 = mob
    #         player2 = player

    while not ((player['Vida'] <= 0) or (mob['Vida'] <= 0)):
        escolher_acao = escolherOpcao()

        if escolher_acao == '1':
            print("Você escolheu atacar!")
            ataque = player['Ataque'] + d20()
            defesa = mob['Defesa'] + d20()
            dano = ataque - defesa
            mob['Vida'] -= dano
            print(f"\nVocê Deu {dano} pontos de dano no mob\nHP Mob: {mob['Vida']}")



            ataque = mob['Ataque'] + d20()
            defesa = player['Defesa'] + d20()
            dano = ataque - defesa

            player['Vida'] -= dano

            print(f"\nO mob deu {dano} pontos de dano em você\nHP player: {player['Vida']}")

        # if (player['Vida'] == 0):
        #     break
        # if (mob['Vida'] == 0):
        #     break



    # sistema ataque defesa bibliografia: "https://forgotten-rpg.forumeiros.com/t11-calculo-de-dano"

    # Dano = Ataque - Defesa // Ataque = Força  + d20 // # quando
    # Defesa = Constituição + Resistência do Equipamento + d20

    # if escolher_acao not in '123':
    #     print("Por favor selecione uma opção válida!")
    #     continue
    # else:
    #     break
    # while True:
    #     damage = rolar_dado()
    #     if damage == 0:
    #         print("Você desviou!")
    #         continue
    #
    #     player['Vida'] -= damage
    #     print(f"Você levou {damage} de dano!\n Sua vida desceu pra {player['Vida']} de HP")
    #     time.sleep(1)
    #     if player['Vida'] <= 0:
    #         break
    #     os.system('cls') #limpa o terminal
    # print('Morreu')

jogo()
print("Cabou-setão")