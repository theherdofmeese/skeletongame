# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:44:19 2024

@author: thehe
"""
import random
score = 0
hits = 0
gold = 0

#the bone zone
print("welcome to the BONE ZONE\n")
initialize = input(print("say BONE to go to bone town: "))
while score == 0:
    if initialize != "BONE":
        print("get out")
        score = -1
    else:
        print("lets shred, bone daddy")
        score = 5


def damage(dmgpoints):
    print("you take ",dmgpoints," damage! you suck!")
    hits + dmgpoints
    if hits == 5:
        print("game over idiot, now YOU'RE the skeleton")
def heal(healpoints):
    print("you heal for ",healpoints," health! stop getting hit!")
    hits - healpoints
def skelehit(whackem):
    print("you hit the skeleton!")
    skealth - whackem
    if skealth == 0:
        print("the skeleton dies!")
        skeleton - 1
        score + 15
def skeleheal(reassemble):
    print("the skeleton puts itself back together")
    if skealth < 3:
        skealth + reassemble
def combat(choice):
    comb_act = ["attack","block","heal"]
    skele_act = random.choice(comb_act)
    print(f"the skeleton {skele_act}s!")
 #   if choice != "attack" and "block" and "heal":
  #      print("you fumbled!")
    if choice == skele_act:
        print(f"you both {choice}")
        if choice == "heal":
            heal(1)
            skeleheal(1)
            print("you both feel a little stronger")
            print("skeleton health: ", skealth)
            print("your health: ", (5 - hits))
        elif choice == "attack":
            damage(1)
            skelehit(1)
            print("blocking is for cowards")
            print("you each take 1 damage")
            print(skealth)
            print(hits)
        else:
            print("the staring contest is a draw")
            print("nothing happens")
    elif choice == "block":
        if skele_act == "attack":
            print("blocked! 0 damage")
        else:
            print("skeleton drinks milk.")
            skeleheal(1)
    elif choice == "heal":
        if skele_act == "attack":
            print("get boned!")
            damage(2)
        else:
            print("put some pep in your step!")
            heal(3)
    elif choice == "attack":
        if skele_act == "block":
            print("blocked! you dealt 0 damage")
        else:
            print("you rattled their bones!")
            skelehit(2)
while hits < 5:
    print("you encounter a skeleton!")
    print("prepare for combat")
    skeleton = 1
    skealth = 3
    while skeleton == 1 and hits < 5:
        combat(input("attack, block or heal?: "))
    print("make a decision: heal or loot?\n")
    decision = input("your decision:  ")
    if decision == "heal":
        print("you bandage yourself and continue on")
        hits = 0
    elif decision == "loot":
        print("you rummage through the pile of bones for shiny things")
        lucky = random.randint(1, 3)
        gold + lucky
        print("the sekelton was carrying ",lucky,"gold pieces")
        print("you now have ",gold)
print("game over")
print(gold)
print(score)