Jogo de Damas

Neste trabalho iremos implementar um jogo de damas no terminal. O conjunto de regras implementadas será o conjunto de regras da versão americana do jogo, como descrito na Wikipedia e detalhado abaixo.

Regras

O jogo de damas é jogado sobre um tabuleiro quadriculado de 8x8 casas. Cada jogador controla 12 peças que iniciam nas casas pretas das três fileiras mais próximas ao jogador.

Os jogadores alternam jogadas.

A cada jogada um jogador escolhe uma peça e pode movimentá-la para uma das casas pretas desocupadas à frente da peça. (As peças só se movem para frente.)

Caso uma peça adversária esteja adjacente e à frente de uma peça do jogador, e a casa preta atrás da peça adversária (oposta à peça do jogador) esteja vazia, uma captura é possível.

Em uma captura, a peça "salta" a peça adversária e é colocada na casa posterior. A peça adversária capturada é removida do tabuleiro.

Uma peça pode fazer múltiplas capturas em sequência na mesma jogada caso sejam possíveis capturas adicionais.

Peças não podem realizar capturas movimentando-se para trás. (As peças só se movem para frente.)

Quando uma captura for possível, o jogador é obrigado a realizá-la. Quando múltiplas capturas forem possíveis, o jogador pode escolher uma delas para realizar.

Quando uma peça chega à última fileira do tabuleiro (do lado oposto ao do jogador), ela é promovida para uma dama. As damas funcionam como as peças normais, mas podem se movimentar e realizar capturas para trás. (Quando se movimentam, as damas andam apenas uma casa.)

Um jogador que não tenha peças restantes ou cujas peças não tenham jogadas possíveis perde a partida.

A cada à direita do tabuleiro na fileira mais próxima ao jogador é sempre branca.

Implementação

Seu jogo deve imprimir o tabuleiro no terminal. A impressão deve distinguir as casas pretas das casas brancas e diferenciar as peças dos dois jogadores. A impressão deve também diferenciar as peças normais das damas.
A cada rodada, seu programa deve indicar de quem é a vez de jogar e deve ler do teclado a jogada a ser realizada. Você deve definir como a jogada será informada ao programa. Por exemplo, seu programa precisa permitir ao jogador indicar qual peça quer mover e em qual direção.
Ao ler a jogada do teclado, seu programa deve verificar se ela é uma jogada válida. Caso a jogada seja inválida, seu programa deve imprimir uma mensagem de erro explicando por quê a jogada é inválida e deve pedir ao usuário para tentar novamente. Em particular, seu programa deve exigir que o jogador realize uma captura caso alguma captura seja possível.
Seu programa também deve detectar automaticamente o final do jogo, em particular o caso das peças de um jogador estarem bloqueadas e não terem jogadas possíveis.

Carregamento de Posição

Seu programa deve também permitir o carregamento de uma posição específica no tabuleiro através de um string que será recebida pela linha de comando (sys.argv, como no TP1). O string terá o seguinte formato {T}:{J}, onde:

{T} é um string com 32 letras onde cada letra indica o estado de uma casa preta do tabuleiro. Numerando as fileiras do tabuleiro de 1 a 8 e as colunas do tabuleiro de a a h, onde a fileira 1 é a de cima e a fileira 8 é a de baixo (na tela) e onde a coluna a é a da esquerda e a coluna h é a da direita (na tela), as letras em {T} estão ordenadas na sequência 1b, 1d, 1f, 1h, 2a, ..., 8g.

Cada letra em {T} pode ter um de quatro valores:

a: Uma peça normal do jogador A.

A: Uma dama do jogador A.

b: Uma peça normal do jogador B.

B: Uma dama do jogador B.

.: Uma casa preta vazia (sem peça ou dama)

{J} é um string com uma letra, a ou b, que indica de quem é a vez de jogar.

Exemplos

O string correspondente à posição inicial do jogo de damas é:
aaaaaaaaaaaa........bbbbbbbbbbbb:b
O string correspondente à posição onde todas as peças de cada jogador andaram uma casa para frente sem que nenhuma captura seja realizada é:
....aaaaaaaaaaaabbbbbbbbbbbb....:b
O string correspondente à posição onde cada jogador tem uma dama e elas estão em cantos opostos do tabuleiro na diagonal longa:
...B........................A...:a
