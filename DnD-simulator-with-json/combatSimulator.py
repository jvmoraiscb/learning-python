class CombatSimulator:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        if self.player1.dexterity >= self.player2.dexterity:
            player1Turn = True
        else:
            player1Turn = False

        print(f"{self.player1.name} x {self.player2.name}\n")
        while self.player1.hp > 0 and self.player2.hp > 0:
            if player1Turn:
                print(f"Turno de {self.player1.name}:");
                self.player1.attack(self.player2)
                player1Turn = False
            else:
                print(f"Turno de {self.player2.name}:");
                self.player2.attack(self.player1)
                player1Turn = True

        if self.player1.hp > 0:
            print(f"{self.player1.name} venceu!")
        else:
            print(f"{self.player2.name} venceu!")
