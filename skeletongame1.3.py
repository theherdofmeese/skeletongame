# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:59:24 2024

@author: thehe
"""
import random
class Player:
    progress = 0
    itempool = ["sword","armor","key","map"]
    hits = 0
    maxhits = 3
    score = 0
    kills = 0
    gold = 0
    inventory = []
    player = True
    def __init__(self, hits, gold, score, inventory, maxhits, kills, progress):
        self.hits = hits
        self.gold = gold
        self.score = score
        self.inventory = inventory
        self.progress = progress
        self.maxhits = maxhits
        self.kills = kills
    def damage(pain):
        Player.hits += pain
        return Player.hits
    def addscore(points):
        Player.score += points
        return  Player.score
    def addgold(coins):
        Player.gold += coins
        return Player.gold
    def heal(hp):
        Player.hits -= hp
        if Player.hits < 0:
            Player.hits = 0
        return Player.hits
    def playerdeath():
        if Player.hits >= Player.maxhits:
            print("You died!")
            Player.player = False
            Player.hits = 0
            Player.maxhits = 0
            return
    def loot():
        return random.choice(Player.itempool)
class Skeleton:
    hits = 0
    skeleton = True
    maxhits = 3
    options = ["attack","heal","block"]
    def __init__(self,hits,maxhits):
        self.hits = hits
        self.maxhits = maxhits
    def skeledeath():
        if Skeleton.hits >= Skeleton.maxhits:
            Player.kills += 1
            Player.addscore(15)
            Player.addgold(random.randint(1, 4))
            print("You killed the skeleton!")
            Skeleton.hits = 0
            Skeleton.skeleton = False
            return
        else:
            pass
    def heal(hp):
        Skeleton.hits -= hp
        if Skeleton.hits< 0:
           Skeleton.hits = 0
        return Skeleton.hits
    def skeleaction():
        action = random.choice(Skeleton.options)
        return action
    def skeledamage(pain):
        Skeleton.hits += pain
        return Skeleton.hits
def Combat(playerchoice,compchoice):
    if playerchoice not in ["attack","block","heal"]:
        print("Fumble!")
        Player.damage(1)
        return
    print(f"You {playerchoice} while the skeleton {compchoice}s")
    def tie(playerchoice):
        combatresult = {
            "attack": "you both attack!\n\n",
            "block": "you lost the staring contest!\n\n",
            "heal": "you both recover some health\n\n"}
        result = combatresult.get(playerchoice)
        return print(result)
    def win(playerchoice):
        combatresult = {
            "attack": "you rattle the skeleton's bones while it tries to recover!\n\n",
            "block": "you block the skeleton's attack!\n\n",
            "heal": "you recover some health\n\n"}
        Player.addscore(5)
        result = combatresult.get(playerchoice)

        return print(result)
    def lose(playerchoice):
        combatresult = {
            "attack": "the skeleton blocks your attack!\n\n",
            "block": "the skeleton reassembles!\n\n",
            "heal": "you try to heal, but the skeleton attacks!\n\n"}
        result = combatresult.get(playerchoice)

        return print(result)
    if playerchoice == compchoice:
        if playerchoice == "attack":
            Skeleton.skeledamage(1)
            Player.damage(2)
        if playerchoice == "heal":
            Player.heal(1)
            Skeleton.heal(1)
        tie(playerchoice)
    elif playerchoice == "attack":
        if compchoice == "block":
            lose(playerchoice)
        else:
            Skeleton.skeledamage(2)
            win(playerchoice)
    elif playerchoice == "block":
        if compchoice == "heal":
            Skeleton.heal(3)
            lose(playerchoice)
        else:
            win(playerchoice)
    elif playerchoice == "heal":
        if compchoice == "attack":
            Player.damage(2)
            lose(playerchoice)
        else:
            win(playerchoice)
            Player.heal(2)
    return Player.player and Skeleton.skeleton
def encounter(chance):
    roll = random.randint(1,chance)
    if roll == chance:
        return True
    else:
        return False
def itemeffects():
     if "armor" in Player.inventory:
         Player.maxhits = 5
     if "sword" in Player.inventory:
         Skeleton.maxhits = 2
     if "map" in Player.inventory:
         Player.progress += 4
         Player.inventory.remove("map")
     if "gun" in Player.inventory:
         Skeleton.maxhits = 1
def Shop():
    thief = False
    if thief == True:
        print("GET OUT")
        print("The shopkeeper shoots you")
        Player.damage(3)
        Player.playerdeath()
        return
    def purchase(item):
        if item not in shopinventory and not "steal":
            print("get out")
            return
        elif item == "steal":
            print("Thief! Skeleton Jesus saw that")
            if encounter(2):
                stolengoods= Player.loot()
                Player.inventory.append(stolengoods)
                print("You got away with it")
                print("Shopkeeper: IF I EVER SEE YOU AGAIN I'LL SHOOT YOU")
                print(f"You ran away with the {stolengoods}...\n\n\n\n")
                Shop.thief = True
            else:
                print("You were caught!")
                Shop.thief = True
                print("Shopkeeper: NEVER COME BACK")
            return
        elif Player.gold >= shopinventory.get(item):
            Player.gold-=shopinventory.get(item)
            Player.inventory.append(item)
            print(f"You bought the {item}")
        else:
            print("Not enough gold!")
#        Player.inventory.append(newitem)
    print("Whaddya buyin?")
    shopinventory = {
        "key": 20,
        "sword": 50,
        "armor": 30,
        "map": 40,
        "gun": 100,
        }
    print(shopinventory)
    purchase(input("What would you like to buy?\n"
                   f"(You have {Player.gold} gold):"))
    itemeffects()
    
def Loot():
    if encounter(2) == True:
        itemdrop = Player.loot()
        print(f"You find an item! It's the {itemdrop}!")
        Player.inventory.append(itemdrop)
        itemeffects()
    else:
        golddrop = random.randint(4, 8)
        Player.gold += golddrop
        print(
            f"you find {golddrop} gold coins!"
            f"\nYou now have {Player.gold} coins!\n\n"
        )
def Explore():
    Player.progress += 1
    print("You walk further into the catacombs...\n\n")
    if encounter(3) == True:
        print("You found a chest!  But its locked...")
        if "key" in Player.inventory:
            ans = input(
                """Open the chest with your key?"
                (Key will be removed)
                (yes or no)"""
                ).lower()
            if ans == "yes":
                chestgold=random.randint(100,200)
                Player.gold += chestgold
                Player.inventory.remove("key")
                Loot()
                print(f"You open the chest and find {chestgold}\n\n\n")
        else:
            print("you walk away...\n\n\n")
            
    if Player.progress in [5,9]:
        Skeleton.maxhits +=1
        print("the skeletons get stronger...\n\n\n")
    if Player.progress in [3,5,7]:
        print("You find a shop\n")
        choice = input("Go in?\n(yes/no):")
        if choice == "y":
            Shop()
        else:
            print("You moved on with your journey")
def newroom(path):
    if path.lower() == "loot":
       Loot()
    elif path.lower() == "explore":
        Explore()
    elif path.lower() == "heal":
        Player.heal(3)
        print(f"""
              You have {Player.score} points
              You have {Player.gold} gold
              You've killed {Player.kills} skeletons
              You have {Player.inventory}
              \n\n\n""")
    else:
        print("You fumble around and do nothing...\n\n")
bonezone = True
while bonezone == True:
    Player.progress = 0
    Player.hits = 0
    Player.maxhits = 3
    Player.score = 0
    Player.kills = 0
    Player.gold = 0
    Player.inventory = []
    Skeleton.hits=0
    Skeleton.maxhits = 3
    
    Player.player = True
    Skeleton.skeleton = False
   
    input("Welcome to BONE ZONE\nPress enter to begin")
    while Player.player:

        print("A skeleton approaches, prepare to fight!")
        Skeleton.skeleton = True
        while Skeleton.skeleton and Player.player:
            Combat(input(
                "What do you do?"
                "\n[attack, block, heal]:\n"
                ).lower(),Skeleton.skeleaction())
            Player.playerdeath()
            Skeleton.skeledeath()
            if Skeleton.skeleton == True:
                print(f"Skeleton health: {Skeleton.maxhits-Skeleton.hits}")
            else:
                print("Skeleton health: Pile of bones")
            if Player.player == True:
                print(f"Player health: {Player.maxhits-Player.hits}\n\n")
            else:
                print("Player health: Promoted to Skeleton\n\n\n")

        if Player.player == False:
            break
        newroom(input(
            "What do you do next?"
            "\n[Loot, Heal, or Explore]:\n"
            ))
        
        if Player.progress <10:
            pass
        else:
            print ("you win!")
            Player.player = False
            break
        print("You move into the next room...\n\n\n")
    print(
          f"""You scored {Player.score} points
          You found {Player.gold} gold
          You killed {Player.kills} skeletons"""
          )

    tryagain = input("Do you want to try again? (yes/no):\n")
    if tryagain not in ["yes","no"]:
        print("get out")
        break
    elif tryagain.lower() == "no":
        print("Thanks for playing!")
        bonezone=False
        break
    if tryagain.lower() == "yes":
        Player.player = True
