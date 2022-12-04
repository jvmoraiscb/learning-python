import sys
import character as cr

def main():
    try:
        player1 = cr.Character(sys.argv[1])
        player2 = cr.Character(sys.argv[2])
    except:
        print("ERRO: arquivos não informados ou inválidos!")
        return;

    if player1.dexterity >= player2.dexterity:
        player1Turn = True
    else:
        player1Turn = False

    print(f"{player1.name} x {player2.name}\n")
    while player1.hp > 0 and player2.hp > 0:
        if player1Turn:
            print(f"Turno de {player1.name}:");
            player1.attack(player2)
            player1Turn = False
        else:
            print(f"Turno de {player2.name}:");
            player2.attack(player1)
            player1Turn = True

    if player1.hp > 0:
        print(f"{player1.name} venceu!")
    else:
        print(f"{player2.name} venceu!")

main()
