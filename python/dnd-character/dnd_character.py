from random import randint
import math

def roll_dice():
        dice = []
        somme = 0
        for i in range(4):
            dice.append(randint(1,6))
        dice.sort()
        for s in range(1,4):
            somme += dice[s]
        return somme

def modifier(value):
    value -= 10
    value /= 2
    return math.floor(value)


class Character:
    def ability(self):
         return roll_dice()

    def __init__(self):
        self.strength = int(self.ability())
        self.dexterity = int(self.ability())
        self.constitution = int(self.ability())
        self.intelligence = int(self.ability())
        self.wisdom = int(self.ability())
        self.charisma = int(self.ability())

        self.hitpoints = 10 + modifier(self.constitution)



