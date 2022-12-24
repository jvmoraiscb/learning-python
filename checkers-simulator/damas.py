class Damas:
    def __init__(self, pecas, jogador):
        self.jogador = jogador
        self.tabuleiro = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
        for i in range(8):
            for j in range(8):
                if i%2 == 0:
                    if j%2 == 0:
                        self.tabuleiro[i][j] = "-"
                    else:
                        self.tabuleiro[i][j] = "o"
                else:
                    if j%2 == 0:
                        self.tabuleiro[i][j] = "o"
                    else:
                        self.tabuleiro[i][j] = "-"
        k = 0
        for i in range(8):
            for j in range(8):
                if self.tabuleiro[i][j] == "o":
                    if pecas[k].lower() == "a" or pecas[k].lower() == "b":
                        self.tabuleiro[i][j] = pecas[k]
                    k += 1

    def imprimeTabuleiro(self):
        atualizaDamas(self.tabuleiro)
        print("\nTURNO DO JOGADOR " + self.jogador.upper() + ":\n")
        print("   a b c d e f g h\n")
        for i in range(8):
            print(i+1, end="  ")
            for j in range(8):
                print(self.tabuleiro[i][j], end=" ")
            print()

    def escolhePeca(self, peca):
        i, j = converteJogada(peca)

        capturasDisponiveis = retornaTodasCapturasDisponiveis(self.jogador, self.tabuleiro)
        
        if i != -1:
            if verificaPeca(i, j, self.tabuleiro, self.jogador):
                if pecaPodeSeMover(i, j, self.tabuleiro, self.jogador):
                    if (capturasDisponiveis != "" and capturasDisponiveis.find(peca) != -1) or (capturasDisponiveis == ""):
                        print("Jogadas disponíveis: " + retornaPosicoesDisponiveis(i, j, self.tabuleiro, self.jogador))
                        return True
                    else:
                        print("Peça escolhida não pode se mover pois há outra peça capaz de realizar uma captura!")
                else:
                    print("Peça escolhida não pode se mover!")
            else:
                print("Não há peça na posição escolhida!")
        else:
            print("Posição escolhida está fora do tabuleiro ou não existe!")
        return False
    
    def fazJogada(self, peca, jogada):
        i, j = converteJogada(peca)
        k, l = converteJogada(jogada)

        if k != -1:
            capturou = retornaPosicoesDisponiveis(i, j, self.tabuleiro, self.jogador).find("(captura)")
            if(verificaJogada(i, j, k, l, self.jogador, self.tabuleiro)):
                if retornaPosicoesDisponiveis(k, l, self.tabuleiro, self.jogador).find("(captura)") != -1 and capturou != -1:
                    self.imprimeTabuleiro()
                    print("\nPeça pode realizar outra captura (em série)!")
                    print("Jogadas disponíveis: " + retornaPosicoesDisponiveis(k, l, self.tabuleiro, self.jogador))
                    return -1, desconverteJogada(k, l)
                else:
                    self.jogador = retornaOutroJogador(self.jogador)
                    return 0, peca
            else:
                print("Jogada escolhida não está disponível!")
        else:
            print("Posição escolhida está fora do tabuleiro ou não existe!")
        return 1, peca
    
    def acabou(self):
        for i in range(8):
            for j in range(8):
                if self.tabuleiro[i][j].lower() == self.jogador:
                    if pecaPodeSeMover(i, j, self.tabuleiro, self.jogador):
                        return False
        return True

def atualizaDamas(tabuleiro):
    for i in range(8):
        for j in range(8):
        # faz damas
            if tabuleiro[i][j] == "a" and i == 7:
                tabuleiro[i][j] = "A"
            if tabuleiro[i][j] == "b" and i == 0:
                tabuleiro[i][j] = "B"

def converteJogada(jogada):     # converte string para posição do tabuleiro
    if len(jogada) == 2:
        if (ord(jogada[0]) >= ord("1") and ord(jogada[0]) <= ord("8")) and (ord(jogada[1].lower()) >= ord("a") and ord(jogada[1].lower()) <= ord("h")):
            return int(jogada[0]) - 1, ord(jogada[1].lower()) - 96 - 1  # posição válida, valor ascii "a" == 97
    return -1, -1                                                       # posição inválida

def desconverteJogada(i, j):    # converte posição do tabuleiro para string
    return str(i+1) + chr(j+1+96)

def verificaPeca(i, j, tabuleiro, peca):
    if tabuleiro[i][j].lower() == peca:
        return True
    else:
        return False

def pecaPodeSeMover(i, j, tabuleiro, jogador):
    if jogador == "a":                                                                  # Jogador A #

        if tabuleiro[i][j] == "a":                                                      # peça normal #
            if (i+1 <= 7 and j+1 <= 7):                                                 # pode mover para frente/direita
                if (tabuleiro[i+1][j+1] == "o"):
                    return True
            if (i+1 <= 7 and j-1 >= 0):                                                 # pode mover para frente/esquerda
                if (tabuleiro[i+1][j-1] == "o"):
                    return True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i+1][j+1].lower() == "b" and tabuleiro[i+2][j+2] == "o"):
                    return True
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i+1][j-1].lower() == "b" and tabuleiro[i+2][j-2] == "o"):
                    return True
            return False                                                                # não pode mover

        if tabuleiro[i][j] == "A":                                                      # dama #
            if (i+1 <= 7 and j+1 <= 7):                                                 # pode mover para frente/direita
                if (tabuleiro[i+1][j+1] == "o"):
                    return True
            if (i-1 >= 0 and j+1 <= 7):                                                 # pode mover para tras/direita
                if (tabuleiro[i-1][j+1] == "o"):
                    return True
            if (i+1 <= 7 and j-1 >= 0):                                                 # pode mover para frente/esquerda
                if (tabuleiro[i+1][j-1] == "o"):
                    return True
            if (i-1 >= 0 and j-1 >= 0):                                                 # pode mover para tras/esquerda
                if (tabuleiro[i-1][j-1] == "o"):
                    return True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i+1][j+1].lower() == "b" and tabuleiro[i+2][j+2] == "o"):
                    return True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peca para tras/direita
                if (tabuleiro[i-1][j+1].lower() == "b" and tabuleiro[i-2][j+2] == "o"):
                    return True
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i+1][j-1].lower() == "b" and tabuleiro[i+2][j-2] == "o"):
                    return True
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peça para tras/esquerda
                if (tabuleiro[i-1][j-1].lower() == "b" and tabuleiro[i-2][j-2] == "o"):
                    return True
            return False                                                                # não pode mover

    if jogador == "b":                                                                  # Jogador B #

        if tabuleiro[i][j] == "b":                                                      # peça normal #
            if (i-1 >= 0 and j-1 >= 0):                                                 # pode mover para frente/direita
                if (tabuleiro[i-1][j-1] == "o"):
                    return True
            if (i-1 >= 0 and j+1 <= 7):                                                 # pode mover para frente/esquerda
                if (tabuleiro[i-1][j+1] == "o"):
                    return True
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i-1][j-1].lower() == "a" and tabuleiro[i-2][j-2] == "o"):
                    return True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i-1][j+1].lower() == "a" and tabuleiro[i-2][j+2] == "o"):
                    return True
            return False                                                                # não pode mover
    
        if tabuleiro[i][j] == "B":                                                      # dama #
            if (i-1 >= 0 and j-1 >= 0):                                                 # pode mover para frente/direita
                if (tabuleiro[i-1][j-1] == "o"):
                    return True
            if (i+1 <= 7 and j-1 >= 0):                                                 # pode mover para tras/direita
                if (tabuleiro[i+1][j-1] == "o"):
                    return True
            if (i-1 >= 0 and j+1 <= 7):                                                 # pode mover para frente/esquerda
                if (tabuleiro[i-1][j+1] == "o"):
                    return True
            if (i+1 <= 7 and j+1 <= 7):                                                 # pode mover para tras/esquerda
                if (tabuleiro[i+1][j+1] == "o"):
                    return True
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i-1][j-1].lower() == "a" and tabuleiro[i-2][j-2] == "o"):
                    return True
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peca para tras/direita
                if (tabuleiro[i+1][j-1].lower() == "a" and tabuleiro[i+2][j-2] == "o"):
                    return True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i-1][j+1].lower() == "a" and tabuleiro[i-2][j+2] == "o"):
                    return True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peça para tras/esquerda
                if (tabuleiro[i+1][j+1].lower() == "a" and tabuleiro[i+2][j+2] == "o"):
                    return True
            return False

def retornaPosicoesDisponiveis(i, j, tabuleiro, jogador):
    str = ""
    captura = False
    if jogador == "a":                                                                  # Jogador A #

        if tabuleiro[i][j] == "a":                                                      # peça normal #
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i+1][j-1].lower() == "b" and tabuleiro[i+2][j-2] == "o"):
                    str += desconverteJogada(i+2, j-2) + "(captura) "
                    captura = True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i+1][j+1].lower() == "b" and tabuleiro[i+2][j+2] == "o"):
                    str += desconverteJogada(i+2, j+2) + "(captura) "
                    captura = True
            if (i+1 <= 7 and j-1 >= 0) and captura == False:                            # pode mover para frente/esquerda
                if (tabuleiro[i+1][j-1] == "o"):
                    str += desconverteJogada(i+1, j-1) + " "
            if (i+1 <= 7 and j+1 <= 7) and captura == False:                            # pode mover para frente/direita
                if (tabuleiro[i+1][j+1] == "o"):
                    str += desconverteJogada(i+1, j+1) + " "

        if tabuleiro[i][j] == "A":                                                                 # dama #
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peça para frente/esquerda
                if (tabuleiro[i+1][j-1].lower() == "b" and tabuleiro[i+2][j-2] == "o"):
                    str += desconverteJogada(i+2, j-2) + "(captura) "
                    captura = True
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peça para tras/esquerda
                if (tabuleiro[i-1][j-1].lower() == "b" and tabuleiro[i-2][j-2] == "o"):
                    str += desconverteJogada(i-2, j-2) + "(captura) "
                    captura = True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peca para frente/direita
                if (tabuleiro[i+1][j+1].lower() == "b" and tabuleiro[i+2][j+2] == "o"):
                    str += desconverteJogada(i+2, j+2) + "(captura) "
                    captura = True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peca para tras/direita
                if (tabuleiro[i-1][j+1].lower() == "b" and tabuleiro[i-2][j+2] == "o"):
                    str += desconverteJogada(i-2, j+2) + "(captura) "
                    captura = True
            if (i+1 <= 7 and j-1 >= 0) and captura == False:                            # pode mover para frente/esquerda
                if (tabuleiro[i+1][j-1] == "o"):
                    str += desconverteJogada(i+1, j-1) + " "
            if (i-1 >= 0 and j-1 >= 0) and captura == False:                            # pode mover para tras/esquerda
                if (tabuleiro[i-1][j-1] == "o"):
                    str += desconverteJogada(i-1, j-1) + " "
            if (i+1 <= 7 and j+1 <= 7) and captura == False:                            # pode mover para frente/direita
                if (tabuleiro[i+1][j+1] == "o"):
                    str += desconverteJogada(i+1, j+1) + " "
            if (i-1 >= 0 and j+1 <= 7) and captura == False:                            # pode mover para tras/direita
                if (tabuleiro[i-1][j+1] == "o"):
                    str += desconverteJogada(i-1, j+1) + " "

    if jogador == "b":                                                                  # Jogador B #

        if tabuleiro[i][j] == "b":                                                                 # peça normal #
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peca para frente/esquerda
                if (tabuleiro[i-1][j-1].lower() == "a" and tabuleiro[i-2][j-2] == "o"):
                    str += desconverteJogada(i-2, j-2) + "(captura) "
                    captura = True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peça para frente/direita
                if (tabuleiro[i-1][j+1].lower() == "a" and tabuleiro[i-2][j+2] == "o"):
                    str += desconverteJogada(i-2, j+2) + "(captura) "
                    captura = True
            if (i-1 >= 0 and j-1 >= 0) and captura == False:                            # pode mover para frente/esquerda
                if (tabuleiro[i-1][j-1] == "o"):
                    str += desconverteJogada(i-1, j-1) + " "
            if (i-1 >= 0 and j+1 <= 7) and captura == False:                            # pode mover para frente/direita
                if (tabuleiro[i-1][j+1] == "o"):
                    str += desconverteJogada(i-1, j+1) + " "
    
        if tabuleiro[i][j] == "B":                                                                 # dama #
            if (i-2 >= 0 and j-2 >= 0):                                                 # pode comer peca para frente/esquerda
                if (tabuleiro[i-1][j-1].lower() == "a" and tabuleiro[i-2][j-2] == "o"):
                    str += desconverteJogada(i-2, j-2) + "(captura) "
                    captura = True
            if (i+2 <= 7 and j-2 >= 0):                                                 # pode comer peca para tras/esquerda
                if (tabuleiro[i+1][j-1].lower() == "a" and tabuleiro[i+2][j-2] == "o"):
                    str += desconverteJogada(i+2, j-2) + "(captura) "
                    captura = True
            if (i-2 >= 0 and j+2 <= 7):                                                 # pode comer peça para frente/direita
                if (tabuleiro[i-1][j+1].lower() == "a" and tabuleiro[i-2][j+2] == "o"):
                    str += desconverteJogada(i-2, j+2) + "(captura) "
                    captura = True
            if (i+2 <= 7 and j+2 <= 7):                                                 # pode comer peça para tras/direita
                if (tabuleiro[i+1][j+1].lower() == "a" and tabuleiro[i+2][j+2] == "o"):
                    str += desconverteJogada(i+2, j+2) + "(captura) "
                    captura = True
            if (i-1 >= 0 and j-1 >= 0) and captura == False:                            # pode mover para frente/esquerda
                if (tabuleiro[i-1][j-1] == "o"):
                    str += desconverteJogada(i-1, j-1) + " "
            if (i+1 <= 7 and j-1 >= 0) and captura == False:                            # pode mover para tras/esquerda
                if (tabuleiro[i+1][j-1] == "o"):
                    str += desconverteJogada(i+1, j-1) + " "
            if (i-1 >= 0 and j+1 <= 7) and captura == False:                            # pode mover para frente/direita
                if (tabuleiro[i-1][j+1] == "o"):
                    str += desconverteJogada(i-1, j+1) + " "
            if (i+1 <= 7 and j+1 <= 7) and captura == False:                            # pode mover para tras/direita
                if (tabuleiro[i+1][j+1] == "o"):
                    str += desconverteJogada(i+1, j+1) + " "
    return str

def retornaTodasCapturasDisponiveis(jogador, tabuleiro):
    str = ""
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j].lower() == jogador:
                string = retornaPosicoesDisponiveis(i, j, tabuleiro, jogador)
                if string.find("(captura)") != -1:
                    str += desconverteJogada(i,j) + " "
    return str

def verificaJogada(i, j, k, l, jogador, tabuleiro):
    string = retornaPosicoesDisponiveis(i, j, tabuleiro, jogador)
    jogada = desconverteJogada(k, l)
    if string.find(jogada) != -1:
        if tabuleiro[i][j] == "a":
            tabuleiro[i][j] = "o"
            tabuleiro[k][l] = "a"
            if k == i+2 and l == j+2:
                tabuleiro[i+1][j+1] = "o"
            if k == i+2 and l == j-2:
                tabuleiro[i+1][j-1] = "o"
        if tabuleiro[i][j] == "A":
            tabuleiro[i][j] = "o"
            tabuleiro[k][l] = "A"
            if k == i+2 and l == j+2:
                tabuleiro[i+1][j+1] = "o"
            if k == i-2 and l == j+2:
                tabuleiro[i-1][j+1] = "o"
            if k == i+2 and l == j-2:
                tabuleiro[i+1][j-1] = "o"
            if k == i-2 and l == j-2:
                tabuleiro[i-1][j-1] = "o"
        if tabuleiro[i][j] == "b":
            tabuleiro[i][j] = "o"
            tabuleiro[k][l] = "b"
            if k == i-2 and l == j-2:
                tabuleiro[i-1][j-1] = "o"
            if k == i-2 and l == j+2:
                tabuleiro[i-1][j+1] = "o"
        if tabuleiro[i][j] == "B":
            tabuleiro[i][j] = "o"
            tabuleiro[k][l] = "B"
            if k == i-2 and l == j-2:
                tabuleiro[i-1][j-1] = "o"
            if k == i+2 and l == j-2:
                tabuleiro[i+1][j-1] = "o"
            if k == i-2 and l == j+2:
                tabuleiro[i-1][j+1] = "o"
            if k == i+2 and l == j+2:
                tabuleiro[i+1][j+1] = "o"
        return True
    return False

def retornaOutroJogador(jogador):
    if jogador == "a":
        return "b"
    return "a"