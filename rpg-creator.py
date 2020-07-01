class Character:
    def __init__(self, name: str, strength: int = 10, dexterity: int = 10, durability: int = 10, intellect: int = 10,
                 discernment: int = 10, charisma: int = 10):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.durability = durability
        self.intellect = intellect
        self.discernment = discernment
        self.charisma = charisma
        self.lifePoints = 100
        print(f'statystyki postaci: {vars(self)}')

    def attack(self):
        print('Ciach!')

    def injuries(self, points):
        print(f"{self.name} traci {(points * self.durability)/100} pkt życia.")
        self.lifePoints -= points * self.durability/100
        print(f"Teraz ma {round(self.lifePoints)} pkt życia.")


class Elf(Character):
    def __init__ (self, name):
        super().__init__(name, dexterity=20, intellect=15, discernment=15, charisma=18)

    def attack(self):
        print(f"{self.name} zadaje {self.dexterity} pkt obrażeń")
        return self.dexterity


class Human(Character):
    def __init__(self, name):
        super().__init__(name, strength=18, dexterity=15, durability=16, charisma=15)

    def attack(self):
        print(f"{self.name} zadaje {((self.strength + self.durability)/2)} pkt obrażeń")
        return (self.strength + self.durability)/2


class Orc(Character):
    def __init__(self, name):
        super().__init__(name, strength=20, durability=20)

    def attack(self):
        print(f"{self.name} zadaje {((self.strength + self.durability) / 2)} pkt obrażeń")
        return (self.strength + self.durability) / 2


def fight(player1, player2):
        if player1.dexterity > player2.dexterity:
            while player2.lifePoints > 0 and player1.lifePoints >0:
                player2.injuries(player1.attack())
                player1.injuries(player2.attack())
        else:
            while player2.lifePoints > 0 and player1.lifePoints > 0:
                player1.injuries(player2.attack())
                player2.injuries(player1.attack())
        if player1.lifePoints < 0:
            print(f"{player2.name} wygrał!")
        else:
            print(f"{player1.name} wygrał!")


if __name__ == "__main__":
    pola = Elf('Pola')
    misiek = Human('Misiek')
    fight(pola, misiek)



