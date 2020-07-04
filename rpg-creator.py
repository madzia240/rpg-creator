import time
import itertools
from abc import ABC, abstractmethod


class Character(ABC):
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

    def characterStats(self):
        print(f'Character stats: {vars(self)}')

    @abstractmethod
    def attack(self):
        pass

    def injuries(self, points):
        print(f"{self.name} lost {(points * self.durability) / 100} life points.")
        self.lifePoints -= points * self.durability / 100
        print(f"{self.name} have {round(self.lifePoints)} life points left.")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, dexterity=20, intellect=15, discernment=15, charisma=18, durability=15)

    def attack(self):
        print(f"{self.name} hits {self.dexterity} damage")
        return self.dexterity


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, strength=18, dexterity=15, durability=17, charisma=15)

    def attack(self):
        print(f"{self.name} hits {((self.strength + self.durability) / 2)} damage")
        return (self.strength + self.durability) / 2


class Tank(Character):
    def __init__(self, name):
        super().__init__(name, strength=20, durability=18)

    def attack(self):
        print(f"{self.name} hits {((self.strength + self.durability) / 2)} damage")
        return (self.strength + self.durability) / 2


class Warlock(Character):
    def __init__(self, name):
        super().__init__(name, intellect=23, durability=13)

    def attack(self):
        print(f"{self.name} hits {self.intellect} damage")
        return self.intellect


class Team:
    def __init__(self):
        self.teamMembers = []

    def memberAdd(self, member):
        self.teamMembers.append(member)

    def members(self, i):
        print('Team members: ')
        for char in self.teamMembers:
            print(vars(char)[i])

    def membersRases(self):
        if len(self.teamMembers) == 0:
            print(f'There is no members in that team')
        else:
            print('Team members: ')
            for key, group in itertools.groupby(self.teamMembers, lambda member: str(type(member))[17:-2]):
                print(key,":", len(list(group)))


def fight(player1, player2):
    if player1.dexterity > player2.dexterity:
        while player2.lifePoints > 0 and player1.lifePoints > 0:
            player2.injuries(player1.attack())
            player1.injuries(player2.attack())
            time.sleep(1)
    else:
        while player2.lifePoints > 0 and player1.lifePoints > 0:
            player1.injuries(player2.attack())
            player2.injuries(player1.attack())
            time.sleep(1)
    if player1.lifePoints <= 0:
        print('-' * 20)
        print(f"{player2.name} won!")
        print('-' * 20)
        time.sleep(5)
    elif player2.lifePoints <= 0:
        print('-' * 20)
        print(f"{player1.name} won!")
        print('-' * 20)
        time.sleep(5)
    # player1.lifePoints = 100
    # player2.lifePoints = 100


if __name__ == "__main__":
    pola = Archer('Pola')
    misiek = Warrior('Misiek')
    kaczorek = Tank('Kaczorek')
    kubus = Warlock('Kubuś')
    rybka = Warlock('Rybka')
    druzynaA = Team()
    druzynaB = Team()
    druzynaA.memberAdd(pola)
    druzynaA.memberAdd(misiek)
    druzynaA.memberAdd(kaczorek)
    druzynaA.memberAdd(kubus)
    druzynaA.memberAdd(rybka)
    druzynaA.members('strength')
    druzynaA.members('name')
    druzynaA.membersRases()
    druzynaB.membersRases()

