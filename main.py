import random

def game():
    name = input("\nYour name: ").capitalize()
    
    print(f"Welcome to Adventure Glory {name}!")

    completed = False
    
    visited = []
    
    items = []

    player_hp = 100

    boss_hp = max(0, 150)

    normal_attack = ["[1]Clutch", "[2]Sword hit", "[3]Dynamic shots", "[4]Clone attack"]

    treasure = random.choice(["100 Gold, 3 Ruby, 1 Diamond!!!", "1000 Silver, 1 Ruby, 5 Diamond!!!", "100 Gold, 10 Emerald, 1 Diamond!!!", "3000 Silver, 6 Ruby, 20 Diamond!!!"])

    sword = random.choice(["Ice Magic Sword...", "Mystic Fire Magic Sword...", "Nature Blad...", "Hurican bow and arrow...", "legendary Sword...!"])

    sword_collect = sword

    sword_collected = False

    Ice_attacks = ["[1]Ice Slash", "[2]Freezing burst", "[3]Ice Golem", "[4]Ice clones"]

    Fire_attacks = ["[1]Fire Slash", "[2]Burning Sword", "[3]Fire Beast", "[4]Fire clash"]
    
    Nature_attacks = ["[1]Nature Cut", "[2]Divine crust", "[3]Earth Golem", "[4]Divine Tree"]
    
    Bow_attacks = ["[1]Eye Shot", "[2]Epic arrow shot", "[3]20 Arrows", "[4]Shadow Arrow Hurican"]

    Legendary_attacks = ["[1]Legendary Slash", "[2]Legendary Ray", "[3]Hero shot", "[4]Sage shot"]

    Appeared = True

    while True:
        print("\nGame start!")
        print("[A]Right", "[B]Left")
        print("[C]Up", "[D]Down")
        print("[E]Exit.")
        
        option = str(input("Choose direction to move your player: ")).capitalize()
        if option not in visited:
            if option == "E":
                print("Thanks for Playing!")
                break
            elif option == "A":
                visited.append("A")
                print("Player moved Right!", "You meet a old man!")
                talk = input("Do you want to talk : (Yes/No) :").lower()
                if talk == "yes":
                    print(f"Finally! I found you.Pure hearted man.This Magic Weapon is for you: {sword_collect}")
                    print(f"{name} became Magic Weapon master!")
                    sword_collected = True
                    items.append(sword_collect)
                    continue
                elif talk == "no":
                    print("Player come back at his position!")
            
            elif option == "B":
                visited.append("B")
                print("Player moved Left!", "Magical Flower found!")
                print("")
                pick = input("Do you want to carry Magical Flower: (Yes/No): ").lower()
                if pick == "yes":
                    flower = "Magical Flower"
                    print(f"{flower} collected sucessfully!")
                    items.append(flower)
                elif pick == "no":
                    print("Player come back at his position!")
            
            elif option == "C":
                visited.append("C")
                print("Player moved Up!", "Treasure found!")
                print(treasure)
            
            elif option == "D":
                print("Player moved Down!", "\n Floor Bose! Giant Goblin Appeared")
                print("[1] Fight.")
                print("[2] Run.")
                figth = input("Choose option for continue story: ")
                if figth == "1":
                    while Appeared:
                        boss_attack = random.choice(["Slam", "Slug hammer", "Body slam", "Critical punch"])

                        if boss_hp <= 0 and player_hp <= 0:
                            print(f"{name} : Its a draw")
                            completed = True
                            break

                        if boss_hp <= 0:
                            print(f"{name} : Won the battle!")
                            completed = True
                            break

                        elif player_hp <= 0:
                            print(f"{name} : Defeated!, Boss won battle!")
                            completed = True
                            break

                        if boss_hp > 0 and player_hp > 0:
                            print(f"\n{name} Hp: {player_hp}")
                            print(f"Boss Hp: {boss_hp}")
                            if sword_collected == True:
                                print(f"Magical weapon: {sword_collect}")
                                if sword_collect == "Ice Magic Sword...":
                                    print(Ice_attacks)

                                    attack = input("\nChoose Attack: ")
                                    if attack == "1":
                                        boss_hp = max(0, boss_hp - 30)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "2":
                                        boss_hp = max(0, boss_hp - 45)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "3":
                                        boss_hp = max(0, boss_hp - 90)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "4":
                                        boss_hp = max(0, boss_hp - 50)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    else:
                                        print("Option not found!")

                                elif sword_collect == "Mystic Fire Magic Sword...":
                                    print(Fire_attacks)

                                    attack = input("\nChoose Attack: ")
                                    if attack == "1":
                                        boss_hp = max(0, boss_hp - 30)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "2":
                                        boss_hp = max(0, boss_hp - 45)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "3":
                                        boss_hp = max(0, boss_hp - 90)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "4":
                                        boss_hp = max(0, boss_hp - 50)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    else:
                                        print("Option not found!")
                                
                                elif sword_collect == "Nature Blad...":
                                    print(Nature_attacks)
                                    
                                    attack = input("\nChoose Attack: ")
                                    if attack == "1":
                                        boss_hp = max(0, boss_hp - 30)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "2":
                                        boss_hp = max(0, boss_hp - 45)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "3":
                                        boss_hp = max(0, boss_hp - 90)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "4":
                                        boss_hp = max(0, boss_hp - 50)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    else:
                                        print("Option not found!")
                                
                                elif sword_collect == "Hurican bow and arrow...":
                                    print(Bow_attacks)

                                    attack = input("\nChoose Attack: ")
                                    if attack == "1":
                                        boss_hp = max(0, boss_hp - 30)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "2":
                                        boss_hp = max(0, boss_hp - 45)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "3":
                                        boss_hp = max(0, boss_hp - 90)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "4":
                                        boss_hp = max(0, boss_hp - 50)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    else:
                                        print("Option not found!")
                                
                                elif sword_collect == "legendary Sword...!":
                                    print(Legendary_attacks)

                                    attack = input("\nChoose Attack: ")
                                    if attack == "1":
                                        boss_hp = max(0, boss_hp - 30)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "2":
                                        boss_hp = max(0, boss_hp - 45)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "3":
                                        boss_hp = max(0, boss_hp - 90)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    elif attack == "4":
                                        boss_hp = max(0, boss_hp - 50)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                    else:
                                        print("Option not found!")
                                        
                            elif sword_collected == False:
                                print(normal_attack)

                                print("\n No Sword Collected!")
                                attack = input("\nChoose Attack: ")

                                if attack == "1":
                                        boss_hp = max(0, boss_hp - 15)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                elif attack == "2":
                                        boss_hp = max(0, boss_hp - 25)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                elif attack == "3":
                                        boss_hp = max(0, boss_hp - 60)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                elif attack == "4":
                                        boss_hp = max(0, boss_hp - 35)
                                        print(f"\nPlayer attacked with {attack}, Boss Hp: {boss_hp}")

                                else:
                                    print("Option not found!")

                            if boss_attack == "Slam":
                                player_hp -= 20
                                print(f"Boss used: {boss_attack}, Player hp is :{player_hp}")

                            elif boss_attack == "Slug hammer":
                                player_hp -= 50
                                print(f"Boss used: {boss_attack}, Player hp is :{player_hp}")

                            elif boss_attack == "Body slam":
                                player_hp -= 35
                                print(f"Boss used: {boss_attack}, Player hp is :{player_hp}")

                            elif boss_attack == "Critical punch":
                                player_hp -= 80
                                print(f"Boss used: {boss_attack}, Player hp is :{player_hp}")

                        else:
                            print("Game Completed..., Thanks for playing.")
                            break

                elif figth == "2":
                    print(f"{name} escaped dungeon...")
                    break

                else:
                    print("Choose right optons!")

            else:
                print("Option not found!")

        else:
            print("Nothing Found!")

        if completed == True:
            print("Game ended...")
            break
        
def tryagain():
    game()

    while True:
        try_again = input("\nWant to play more? (Yes/No): ").lower()

        if try_again == "yes":
            game()

        elif try_again == "no":
            print("Thanks for coming!!!")
            break

        else:
            print("Choose correct option!")

tryagain()

# Dungeon game completed