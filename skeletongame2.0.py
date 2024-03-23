# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:36:30 2024

@author: thehe
"""
class Character:
    def __init__(self, maxhealth, hits, score):
        self.maxhealth = maxhealth
        self.hits= hits
        self.score = score
    @property
    def death(self):
        if self.hits >= self.maxhealth:
            print(f"{self} died!")
            self = False
    def damage(self, points):
        self.hits += points
        return self.hits
    def heal(self, hp):
        self.hits -= hp
        if self.hits <= 0:
            self.hits = 0
class Player(Character):
    def __init__(self, maxhealth, hits, score, gold, progress, kills, inventory = None):
        super().__init__(maxhealth,hits,score)
        self.kills = kills
        self.gold = gold
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    def itempickup(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
class Skeleton(Character):
    def __init__(self, maxhealth, hits, score):
        super().__init__(maxhealth,hits,score)
class Wizard(Character):
    def __init__(self, maxhealth, hits, score, spelllist = None):
        super().__init__(maxhealth,hits,score)
        if spelllist is None:
            self.spelllist = []
        else:
            self.spelllist = spelllist
    def cast(self, spell):
        if spell in self.spelllist:
            print(f"{self} casts {spell}!")
        else:
            print(f"{self} doesnt know that spell")
class Zombie(Character):
    def __init__(self, maxhealth, hits, score):
        super().__init__(maxhealth,hits,score)
    pass
class Combat():
    def __init__(self, player_act,npc_act,outcome):
        self.player_act = player_act
        self.npc_act = npc_act
        self.outcome = outcome

zomb1 = Zombie(2,0,30)
wiz1 = Wizard(5, 0, 50, ["fireball"])
bones1 = Skeleton(3, 0, 20)
print(zomb1)