# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:36:11 2024

@author: thehe
"""
import time
import sys
import random

def gamestart():
    print("Welcome to BONE ZONE")
    initialize = input("type 'BONE' to begin\n")
    if initialize.upper() != "BONE":
        print("get out")
    else:
        print("your journey begins. you wake up in the catacombs...")
        print("the labrynth of dark catacombs stretch far")
        print("escape before its too late, with enough gold you can pimp your horse")
        time.sleep(3)
def combat():
    global score
    pchoice = input("What will you do?\n(attack, block, or recover):\n")
    skeleoption = ["attack", "block","recover"]
    skelechoice = random.choice(skeleoption)
    print(f"you {pchoice}, the skeleton {skelechoice}s!")
    if pchoice == skelechoice:
        if pchoice == "block":
            print("you lose the staring contest...\n but nothing else happens")
        elif pchoice == "attack":
            print("blocking is for nerds, both deal some damage")
            damage(1, skeleton)
            damage(1, player)
        else:
            print("the skeleton reassembles as you bandage your skeleton bites")
            heal(1, skeleton)
            heal(1, player)
    elif (pchoice == "attack" and skelechoice == "block") or (
            skelechoice == "attack" and pchoice == "block"):
        print("the attack is deflected and does nothing!")
        if pchoice == "block":
           score += 5
    elif pchoice == "recover":
        if skelechoice == "block":
            heal(2, player)
            print("you patch yourself up")
        else:
            print("the skeleton hits you with a bone!")
            damage(2, player)
    else:
        print("you deal some damage while the skeleton isn't looking!")
        damage(2, skeleton)
        score += 5
             
        
def loot():
    global gold
    diceroll = random.randint(1,8)
    if diceroll > 4:
        print("you find some gold in the skeleton's wallet")
        gold += diceroll
        print(f"you now have {gold} gold")
    else:
        itemdrop = random.choice(items)
        print(f"you find the {itemdrop} and add it to your inventory")
        items.remove(itemdrop)
        inventory.append(itemdrop)
        global floormap, maxhealth, key, skelemax

        if itemdrop == "sword":
            print("killing machine!")
            skelemax -= 1
        elif itemdrop == "armor":
            maxhealth += 2
            print("skeleton proof")
        elif itemdrop == "key":
            key +=1
            print("now to find what it opens...")
        elif itemdrop == "floormap":
            floormap += 1
            
        
        
def explore():
    global progress
    global gold
    global floormap
    global skelemax
    print("you make your way into the catacombs, searching for the exit")
    progress+=1
    if floormap >= 1:
        progress +=5
        print("the map has a shortcut on it!")
        print("but now you're lost again...")
        floormap -= 1
    eventchance = random.randint(1,5)
    if eventchance == 1 or 5:
        print("you find a locked chest...")
        if key == 1:
            keyreply = input("use the key? it might be booby trapped...\n(y/n)")
            if eventchance == 5 and keyreply != "n":
                print("its full of treasure!")
                print("you picked up 200 gold and a sword")
                gold += 200
                skelemax -=1
            elif keyreply == "n":
                print("you leave it alone, good choice")
            else:
                print("you open the chest and its full of bees!\nhow did they get here?")
                damage(4,player)
                
                
def damage(dmgpoints, victim):
    global hits
    global skeleton
    global player
    global skelehits
    if victim == player:
        print(f"you take {dmgpoints} points of damage!")
        hits =+ dmgpoints
        if hits >= maxhealth:
            player = 0
            print("you died!\nyou are one of the skeletons now")
        else:
            print(f"you have {(maxhealth - hits)} healthpoints left!")
    elif victim == skeleton:
        skelehits =+ dmgpoints
        print(f"the skeleton takes {dmgpoints} points of damage!")
        if skelehits >= skelemax:
            skeleton = 0
            skelehits = 0
            print("the skeleton crumbles to dust and bones\n(mostly bones)!")
def heal(hp,victim):
    global hits
    global skelehits
    if victim == player:
        hits-=hp
        print(f"you healed for {hp} points")
        if hits >= maxhealth:
            hits = maxhealth
            print("you feel as good as new!")
    else:
        skelehits-=hp
        if skelehits <= 0:
            print("the skeleton looks good as new (relatively speaking)")
            skelehits = 0
def gameover(answer):
    print(f"you scored {score} points and found {gold} gold!")
    if answer == "y":
        pass
    else:
        sys.exit()
    
while __name__ == "__main__":
    maxhealth = 5
    gold = 0
    progress = 0
    skelehits=0
    hits = 0
    skeleton = 0
    skelemax = 3
    player = 2
    items = ["sword", "key", "floormap", "armor"]
    inventory = []
    key = 0
    floormap = 0
    score = 0
    gamestart()
    print("you make your way into the central chamber")
    print("you fnd a club, a shield, and some bandages")
    print("skeletons start moving toward you...")
    time.sleep(3)
    while player != 0:
        
        skeleton = 1
        print("a skeleton attacks you! get ready to fight")
        while skeleton == 1:
            combat()
            if player == 0:
                break
            if skelehits >= 3:
                print("you killed the skeleton! it crumbles to bones")
                score += 50
                gold += random.randint(1,4)
                print(f"you pick up some gold, you now have {gold} gold")
                break
        time.sleep(1)
        print("you have a moment of peace, what next?")
        choice = input("explore, loot, heal, or check backpack?:")
        if choice == "explore":
            explore()
            print("you move into the next room")
        elif choice == "loot":
            loot()
        elif choice == "heal":
            heal(player, maxhealth)
        elif choice == "check backpack":
            print(f"you have {gold} gold coins and {score} points")
            if inventory == []:
                print("you haven't found any items yet!")
            else:
                print("you dump your backpack on the floor to find...")
                for item in inventory:
                    print(item)
                print("...you pick everything back up")
        else:
            print("you fumble around and do nothing")
            
                
        if player == 0:
            break
        if progress == 5:
            print("halfway there")
        if progress >9 :
            print("you've find the exit")
            print("but the door is locked...")
            if key == 1:
                 if input("use your key to unlock it? (y/n)") == "y":
                     break
                 else:
                     print("no time to stare at it, you hear something nearby...")
    
    if player != 0:
        print("you've escaped, the sunlight feels good")
        time.sleep(1)
        print("you walk to a nearby stream to quench your thirst")
        time.sleep(1)
        print("...you see your reflection, you were a skeleton the whole time")
        time.sleep(1)
        print(f"you scored {score} points and found {gold} gold!")
    else:
        print("you died!")
        print(f"you scored {score} points and found {gold} gold!")

gameover(input("would you like to play again?: "))
