import json
import random

class Character:
    # constructor
    def __init__(self, characterFile):
        with open("armor.json", "r", encoding="utf8") as fd:
            armor_dic = json.load(fd)
        with open("weapons.json", "r", encoding="utf8") as fd:
            weapons_dic = json.load(fd)
        with open("attributes.json", "r", encoding="utf8") as fd:
            attributes_dic = json.load(fd)
        with open(characterFile, "r", encoding="utf8") as fd:
            character_dic = json.load(fd)

        self.hp             = character_dic["HP"]
        self.name           = character_dic["name"]
        self.strength       = character_dic["strength"]
        self.strengthBonus  = attributes_dic[self.strength]
        self.dexterity      = character_dic["dexterity"]
        self.dexterityBonus = attributes_dic[self.dexterity]
        self.armor          = armor_dic[character_dic["armor"]]
        self.weapon         = weapons_dic[character_dic["weapon"]]
        self.shield         = character_dic["shield"]
        self.armorClass     = self.__getAC()
        self.weaponDamage   = int(self.weapon["damage"].lstrip("d")) # remove o d dos valores de dados (por exemplo d8 vira 8)

    # to string
    def __str__(self):
        return f'name: {self.name}\nhp: {self.hp}\nstrength: {self.strength} ({self.strengthBonus})\ndexterity: {self.dexterity} ({self.dexterityBonus})\narmorClass: {self.armorClass} ({self.armor["type"]}, {self.armor["AC"]})\nweapon: {self.weaponDamage} ({self.weapon["props"]})\nshield: {self.shield}\n'

    def attack(self, enemy):
        d20 = random.randint(1, 20)
        
        if self.dexterityBonus >= self.strengthBonus and "finesse" in self.weapon["props"]:
            attackBonus = self.dexterityBonus
            bonusStatus = "por bonus de destreza"
        else:
            attackBonus = self.strengthBonus
            bonusStatus = "por bonus de força"

        print(f"- {self.name} jogou o d20: {d20} ({attackBonus:{'+' if attackBonus else ''}} {bonusStatus})")
        attack = d20 + attackBonus
        
        print(f"- {enemy.name} possui {enemy.armorClass} pontos de armadura")
        if attack > enemy.armorClass:
            print(f"- {self.name} acertou {enemy.name}")
            d = random.randint(1, self.weaponDamage)
            print(f"- {self.name} jogou o d{self.weaponDamage}: {d} ({attackBonus:{'+' if attackBonus else ''}} {bonusStatus})")

            enemy.hp -= d + attackBonus
            if enemy.hp < 0:
                enemy.hp = 0;
            print(f"- {enemy.name} recebeu {d + attackBonus} de dano e possui {enemy.hp} pontos de vida restantes\n")
        else:
            print(f"- {self.name} não acertou {enemy.name}\n")

    def __getAC(self):
        valueArmorClass = self.armor["AC"] 
        if self.dexterityBonus >= 0:
            if self.armor["type"] == "light":
                valueArmorClass += self.dexterityBonus
            elif self.armor["type"] == "medium":
                if self.dexterityBonus > 2:
                   valueArmorClass += 2
                else:
                    valueArmorClass += self.dexterityBonus
            elif self.armor["type"] == "heavy":
                valueArmorClass += 0
        else:
            valueArmorClass -= self.dexterityBonus
        if self.shield and "2-hand" not in self.weapon["props"]:
            valueArmorClass += 2;
        return valueArmorClass;
