import random

hits = 0
skhits = 0
score = 0
gold = 0
skeleton = 0
progress = 0
player = 1

print("welcome to the BONE ZONE\n")
initialize = input(print("\nsay BONE to go to bone town: "))
while score == 0:
    if initialize != "BONE":
        print("get out")
        break
    else:
        print("your journey begins, you wake up deep in a crypt\n")
        score = score + 5
while player == 1:
    sword = 0
    key = 0
    floormap = 0
    armor = 0
    print("a skeleton gets up and shambles towards you")
    print("prepare to fight\n")
    skeleton = 1
    while skeleton == 1 and player == 1:
        choice = input("attack, block or heal?:  \n")
        comb_act = ["attack","block","heal"]
        skele_act = random.choice(comb_act)
        print(f"the skeleton {skele_act}s!")
        if choice not in ["attack", "block", "heal"]:
            print("you fumbled!")
            hits += 1
        if choice == skele_act:
            print(f"you both {choice}\n")
            if choice == "heal":
              
                print("you both feel a little stronger\n")
                if hits > 0:
                    hits = hits - 1
                if skhits > 0 :
                    skhits = skhits - 1
            elif choice == "attack":
                hits += 2
                skhits += 1
                if hits >= 5 and armor == 0:
                    player -= 1
                    break
                elif hits >= 7 and armor == 1:
                    player -= 1
                    break
                elif skhits == 2 and sword == 1:
                    score += 15
                    skeleton -=1
                elif skhits == 3 and sword == 0:
                    score += 15
                    skeleton -= 1
                    break
                print("blocking is for cowards")
                print("you each take some damage\n")
            else:
                print("the staring contest is a draw")
                print("nothing happens\n")
        elif choice == "block":
            if skele_act == "attack":
                print("blocked! 0 damage")
                score += 2
            else:
                print("skeleton drinks milk.")
                if skhits > 0 :
                    skhits = 0
        elif choice == "heal":
            if skele_act == "attack":
                print("get boned!")
                hits += 2
                if hits >4 and armor == 0:
                    player =0
                    break
                elif hits >6 and armor == 1:
                    player = 0
                    break
            else:
                print("you regained some health!\n")
                if hits == 1:
                    hits = 0
                elif hits > 1:
                    hits = hits - 2
        elif choice == "attack":
            if skele_act == "block":
                print("blocked! you dealt 0 damage\n")
            else:
                print("you rattled their bones!\n")
                skhits += 1
                score += 3
                if skhits >= 2 and sword == 1:
                    score += 15
                    skeleton -=1
                elif skhits >= 3 and sword == 0:
                    score += 15
                    skeleton -= 1
    if skeleton != 1:
        print("you killed a skeleton!")
        print("you enter the next chamber\n")
        
    if player != 1:
        break
    else:
        option = input("loot, heal or explore?")
        if option == "loot":
            lucky = random.randint(1, 4)
            itemdrop = ["armor","a key","a map","a sword"]
            item = random.choice(itemdrop)
            if lucky ==4:
                lucky = item
                print("you search the room and find ",lucky)
                if lucky == "armor":
                    armor = 1
                elif lucky == "a key":
                    key = 1
                elif lucky == "a map":
                    floormap = 1
                elif lucky == "a sword":
                    sword = 1
                
            else:
                print(f"you rummage through the skeletons remains and find {lucky} gold pieces\n")
                gold += lucky
        elif option == "heal":
            print("you take a moment to rest\n")
            hits = 0
        elif option == "explore":
            print("you go deeper into the catacombs, looking for the exit\n")
            progress += 1
            if progress == 7:
                print("you find a locked chest")
                if  key == 1:
                    confirm = input(print("try opening the chest with the key? (y/n)"  ))
                    if confirm == "y":
                        print("you open the chest! you find a pile of treasure\n")
                        gold += 200
                    else:
                        print("it was probably booby trapped anyway\n")
            if progress == 10:
                print("you escaped! congratulations")
                score += 100
                print("you earned ",score, " points and collected ", gold," gold coins!\n")
                break
        else:
            if floormap == 0:
                print("you got lost!")
                progress -= 1
            elif floormap == 1:
                print("you found a shortcut on your map!")
                progress+=3
                floormap = 0
        skeleton = 1
print("you died!")
print("you found ",gold," gold and scored ", score, " points")