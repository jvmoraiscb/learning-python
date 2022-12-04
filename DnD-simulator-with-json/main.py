import sys
from combatSimulator import CombatSimulator
from player import Player

try:
    player1File = sys.argv[1]
    player2File = sys.argv[2]
    try:
        player1 = Player(player1File)
        player2 = Player(player2File)
        duel = CombatSimulator(player1, player2)
        duel.start()
    except:
        print("ERRO: um ou mais arquivos inválidos!")
except:
    print("ERRO: arquivos não informados!")
