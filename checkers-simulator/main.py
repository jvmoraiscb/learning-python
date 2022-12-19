import sys
from damas import Damas

stringTab = "aaaaaaaaaaaa........bbbbbbbbbbbb:a".split(":") # string padrão, caso não seja passada nenhuma string como parametro
if len(sys.argv) == 2:
    stringTab = sys.argv[1].split(":")

partida = Damas(stringTab[0], stringTab[1])

while not partida.acabou():                                 # enquanto a partida não acabar
    partida.imprimeTabuleiro()                              # imprime o tabuleiro e atualiza as damas

    peca = str(input("\nEscolha uma peça: "))
    while not partida.escolhePeca(peca):                    # enquanto a peça não for válida
        peca = str(input("\nDigite novamente: "))
    
    jogada = str(input("\nEscolha sua jogada: "))
    while True:                                             # enquanto a jogada não for válida
        status, peca = partida.fazJogada(peca, jogada)
        if status == 0:                                     # caso a jogada seja válida
            break
        if status == 1:                                     # caso a jogada seja inválida
            jogada = str(input("\nDigite novamente: "))
        if status == -1:                                    # caso a jogada seja válida e possa capturar em série
            jogada = str(input("\nEscolha sua jogada: "))

if partida.jogador == "a":                                  # o jogador atual quando a partida acaba é o perdedor, pois não tem peças disponíveis ou não pode move-las
    print("Jogador B venceu a partida!")
else:
    print("jogador A venceu a partida!")

