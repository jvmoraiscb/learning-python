import json
import random

class Player:

    # constructor
    def __init__(self, playerFile):
        with open("armor.json", "r", encoding="utf8") as fd:
            armor_dic = json.load(fd)
        with open("weapons.json", "r", encoding="utf8") as fd:
            weapons_dic = json.load(fd)
        with open("attributes.json", "r", encoding="utf8") as fd:
            attributes_dic = json.load(fd)
        with open(playerFile, "r", encoding="utf8") as fd:
            player_dic = json.load(fd)

        self.hp             = player_dic["HP"]
        self.name           = player_dic["name"]

        self.strength       = player_dic["strength"]
        self.strengthBonus  = attributes_dic[self.strength]

        self.dexterity      = player_dic["dexterity"]
        self.dexterityBonus = attributes_dic[self.dexterity]

        self.weapon         = weapons_dic[player_dic["weapon"]]
        self.weaponDamage   = int(self.weapon["damage"].lstrip("d")) # remove o d da string de dado (por exemplo "d8" vira "8") e converte para inteiro
        self.__getAttackBonusDamage()

        self.armor          = armor_dic[player_dic["armor"]]
        self.shield         = player_dic["shield"]
        self.defense        = self.armor["AC"]
        self.__getDefenseBonus()

    def attack(self, enemy):
        d20 = random.randint(1, 20)

        print(f"- {self.name} jogou o d20: {d20} ({self.attackBonus:{'+' if self.attackBonus>=0 else ''}} {self.attackBonusString}) totalizando {d20 + self.attackBonus} pontos de ataque")
        attack = d20 + self.attackBonus
        
        print(f"- {enemy.name} possui {enemy.defense + enemy.defenseBonus} pontos de defesa {enemy.defenseBonusString}")
        if attack > (enemy.defense + enemy.defenseBonus):
            print(f"- {self.name} acertou {enemy.name}")
            d = random.randint(1, self.weaponDamage)
            print(f"- {self.name} jogou o d{self.weaponDamage}: {d} ({self.attackBonus:{'+' if self.attackBonus>=0 else ''}} {self.attackBonusString}) totalizando {d + self.attackBonus} pontos de dano")

            enemy.hp -= d + self.attackBonus
            if enemy.hp < 0:
                enemy.hp = 0;
            print(f"- {enemy.name} possui {enemy.hp} pontos de vida restantes\n")
        else:
            print(f"- {self.name} não acertou {enemy.name}\n")

    # private method
    def __getDefenseBonus(self):
        if self.dexterityBonus >= 0:
            if self.armor["type"] == "light":
                self.defenseBonus = self.dexterityBonus
            elif self.armor["type"] == "medium":
                if self.dexterityBonus > 2:
                   self.defenseBonus = 2
                else:
                    self.defenseBonus = self.dexterityBonus
            elif self.armor["type"] == "heavy":
                self.defenseBonus = 0
        else:
            self.defenseBonus = self.dexterityBonus
        
        self.defenseBonusString = f"({self.defense} da classe da armadura, {self.defenseBonus:{'+' if self.defenseBonus>=0 else ''}} por usar armadura do tipo {self.armor['type']}"

        if self.shield and "2-hand" not in self.weapon["props"]:
            self.defenseBonus += 2;
            self.defenseBonusString += " e +2 por usar um escudo)"
        else:
            self.defenseBonusString += ")"

    # private method
    def __getAttackBonusDamage(self):
        if self.dexterityBonus > self.strengthBonus and "finesse" in self.weapon["props"]:
            self.attackBonus = self.dexterityBonus
            self.attackBonusString = "por modificador de destreza, devido a propriedade finesse de sua arma"
        else:
            self.attackBonus = self.strengthBonus
            self.attackBonusString = "por modificador de força"
