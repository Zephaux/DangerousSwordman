import random, os, time

def rolar_dado(): # "dados" do jogo pode ser tanto pra dano, quanto pra ataque
    return random.randint(0, 10)

def jogo():
    nome = input('Digite seu nome')
    player = {'Nome': nome, 'Vida': 30}
    mob = {'Nome': 'kara di kwo', 'Vida': 100 }


    player1 = None # variável para ser linkada com o dicionário do player 1
    player2 = None # variável para ser linkada com o dicionário do player 2


    for c in range(0,1): #for usado para definir quem vai começar atacando
        player_dice = rolar_dado()
        mob_dice = rolar_dado()

        if player_dice > mob_dice:
            player1 = player
            player2 = mob
        else:
            player1 = mob
            player2 = player

    escolher_acao = 0 # 1 - Ataca // 2 - Defende // 3 - Item

    while True: # validaçao da ação
        escolher_acao = input("O que gostaria de fazer \n[1] Atacar\n[2] Defender\n[4] Item\n")

        match escolher_acao:
            case '1':
                break
            case '2':
                break
            case '3':
                break
            case _:
                print("Por favor selecione uma opção válida!")
                continue
    #sistema ataque defesa bibliografia: "https://forgotten-rpg.forumeiros.com/t11-calculo-de-dano"

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