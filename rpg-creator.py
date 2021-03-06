import time
import itertools
from abc import ABC, abstractmethod
import json
import random


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
        self.experience = 0
        self.level = 1

    def characterStats(self):
        print(f'Character stats: {vars(self)}')

    @abstractmethod
    def attack(self):
        pass

    def injuries(self, points):
        print(f"{self.name} lost {(points * self.durability) / 100} life points.")
        self.lifePoints -= points * self.durability / 100
        print(f"{self.name} have {round(self.lifePoints)} life points left.")

    def lvl(self):
        if self.experience%20 == 0:
            self.level += 1
            self.strength += 2
            self.dexterity += 2
            self.durability += 2
            self.intellect += 2
            self.discernment += 2


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, dexterity=20, intellect=15, discernment=15, charisma=18, durability=15)

    def attack(self):
        critical = random.randint(0, 5)
        if critical == 5:
            print(f"CRITICAL HIT! {self.name} hits {self.dexterity *2} damage")
            return self.dexterity *2
        print(f"{self.name} hits {self.dexterity} damage")
        return self.dexterity


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, strength=18, dexterity=15, durability=17, charisma=15)

    def attack(self):
        critical = random.randint(0, 5)
        if critical == 5:
            print(f"CRITICAL HIT! {self.name} hits {(self.strength + self.durability)} damage")
            return self.strength + self.durability
        print(f"{self.name} hits {((self.strength + self.durability) / 2)} damage")
        return (self.strength + self.durability) / 2


class Tank(Character):
    def __init__(self, name):
        super().__init__(name, strength=20, durability=18)

    def attack(self):
        critical = random.randint(0, 5)
        if critical == 5:
            print(f"CRITICAL HIT! {self.name} hits {(self.strength + self.durability)} damage")
            return self.strength + self.durability
        print(f"{self.name} hits {((self.strength + self.durability) / 2)} damage")
        return (self.strength + self.durability) / 2


class Warlock(Character):
    def __init__(self, name):
        super().__init__(name, intellect=23, durability=13)

    def attack(self):
        critical = random.randint(0, 5)
        if critical == 5:
            print(f"CRITICAL HIT! {self.name} hits {self.intellect * 2} damage")
            return self.intellect * 2
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
                print(key, ":", len(list(group)))


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
        print(f"{player2.name} won!\n+10exp")
        print('-' * 20)
        player2.experience += 10
        player2.lvl()
        time.sleep(5)
    elif player2.lifePoints <= 0:
        print('-' * 20)
        print(f"{player1.name} won!\n+10exp")
        print('-' * 20)
        player1.experience += 10
        player1.lvl()
        time.sleep(5)
    player1.lifePoints = 100
    player2.lifePoints = 100


def teamFight(teamA, teamB):
    teamAPoints = 0
    teamBPoints = 0
    print("Team fight!")
    time.sleep(2)
    for memberA, memberB in zip(teamA.teamMembers, teamB.teamMembers):
        fight(memberA, memberB)
        if memberA.lifePoints <= 0:
            teamBPoints += 1
        elif memberB.lifePoints <= 0:
            teamAPoints += 1
    if teamAPoints > teamBPoints:
        print('Team A won!')
    elif teamAPoints < teamBPoints:
        print('Team B won!')
    elif teamAPoints == teamBPoints:
        print("Tie!")
    time.sleep(2)


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
    with open('team.json', 'r') as f:
        team = json.load(f)
    for member in team:
        name = (member['name']).lower()
        if member["rase"] == "Archer":
            name = Archer(member["name"])
        elif member["rase"] == "Warrior":
            name = Warrior(member["name"])
        elif member["rase"] == "Warlock":
            name = Warlock(member["name"])
        elif member["rase"] == "Tank":
            name = Tank(member["name"])
        druzynaB.memberAdd(name)
    # with open('team.json', 'w') as outfile:
    #     json.dump(team, outfile)
    print("-"*29)
    print("|", " "*8, "Arcadia", " "*8, "|")
    print("-"*29)
    print("\nWelcome in Arcadia World!\n\nYou woke up in small room. The dusk reigning here only intensifies your "
          "fatigue, you only think about "
          "one thing - to lie in a warm bed and sleep for several days. In the wall you see a small corner, "
          "where a fat man sits smoking a pipe. His aroma tobacco is so strong that you begin to choke and cough - "
          "pungent smoke squeezes tears from your eyes.")
    time.sleep(3)
    name = input('\nFinally, you woke up - he says - What it is your name?\n')
    rase = int(input("Looks like you can fight. What is your profession?\n1. Archer\n2. Warrior\n3. Warlock\n4. Tank\n"))
    if rase == 1:
        name = Archer(name)
    elif rase == 2:
        name = Warrior(name)
    elif rase == 3:
        name = Warlock(name)
    elif rase == 4:
        name = Tank(name)
    choose = 0
    while choose != 4:
        choose = int(
            input(f'{name.name}, what do you want to do?\n1.See your stats\n2.Fight!\n3.Team\n4.Quit game\n'))
        if choose == 1:
            name.characterStats()
            time.sleep(2)
        elif choose == 2:
            print("Choose your opponent:")
            for i, member in enumerate(druzynaB.teamMembers):
                print(f"{i}: {member.name}")
            opponent = int(input())
            print(f"Your opponent: {druzynaB.teamMembers[opponent].name}")
            time.sleep(2)
            print("FIGHT!")
            time.sleep(2)
            fight(name, druzynaB.teamMembers[opponent])
        elif choose == 3:
            if name not in druzynaA.teamMembers:
                print('You do not have your team.')
                time.sleep(1)
                ans = input('Do you want to join?\n[Y]es [N]o\n').lower()
                if ans == "y":
                    druzynaA.memberAdd(name)
                    print("\nYou joined to team!")
                    time.sleep(2)
            else:
                ans = int(input('Team options:\n1. Team Members\n2. Fight!\n3. Back\n'))
                if ans == 1:
                    druzynaA.members("name")
                    druzynaA.membersRases()
                elif ans == 2:
                    teamFight(druzynaA, druzynaB)




