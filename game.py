# Alex Ruan
# 21 September 2018
# On my honor, I have neither recieved nor given unauthorized unauthorized
# This is a "Choose your own adventure" game, where your final objective is to defeat God himself
#Sources: Python documentation and an ASCII art generator

text = "It charges at you, and you have to make a split-second decision. Do you\n1) Fight\n2) Run\n\n" #Stores part of a monster fight sequence
text2 = "Now, you have a choice to\n1) Turn left\n2) Turn right\n\n" #Stores a part of a monster fight sequence

def no(): #Output for when an invalid command is entered
    print("Sorry, that is not an accepted command. Please enter '1' or '2.'")

def finalBattle(): #The final battle sequence with God
    choice = input("Onwards! As you near the end of your journey, you encounter God once again.\nYou prepare to fight him. Do you:\n1)Eat the cheese\n2)Forget the cheese! Fight God!\n\n")
    if choice == "1":
        print("You eat the cheese. Unexpectedly, you feel a rush of strength and adrenaline. The cheese was magical!\nYou gain godlike powers and are fit to fight God. After an intense battle, you emerge victorious!\nA door apeears in front of you, and you take your leave.")
        print("          _______                       _________ _        _ ")
        print("|\     /|(  ___  )|\     /|    |\     /|\__   __/( (    /|( )")
        print("( \   / )| (   ) || )   ( |    | )   ( |   ) (   |  \  ( || |")
        print(" \ (_) / | |   | || |   | |    | | _ | |   | |   |   \ | || |")
        print("  \   /  | |   | || |   | |    | |( )| |   | |   | (\ \) || |")
        print("   ) (   | |   | || |   | |    | || || |   | |   | | \   |(_)")
        print("   | |   | (___) || (___) |    | () () |___) (___| )  \  | _ ")
        print("   \_/   (_______)(_______)    (_______)\_______/|/    )_)(_)")
        print("")
    elif choice == "2":
        print("You really thought you could defeat God?! You lose!")
    else:
        no()

def monster3(): #The third monster battle
    choice = input("You've come across a monster! " + text)
    if choice == "1":
        choice = input("You easily defeat the monster. In it's lair, you find a cheese. But oh no! Your inventory is full.\nDo you:\n1) Pick up the cheese\n2) Leave the cheese\n\n")
        if choice == "1":
            choice = input("What would you like to drop?\n1)The shiny sword\n2)The glowing armor\n\n")
            if choice == "1":
                print("You drop the shiny sword, and you pick up the cheese.")
                finalBattle()
            elif choice == "2":
                print("You drop the glowing armor, and you pick up the cheese.")
                finalBattle()
            else:
                no()
        elif choice == "2":
            print("You really thought you could defeat God with just a shiny sword and glowing armor?! You lose!")
        else:
            no()
    elif choice == "2":
        choice = input("You run away like a coward. However, this monster is faster and catches up to you. It quickly finishes you off, and you die")
    else:
        no()

def monster2(): #The second monster battle
    choice = input("You've come across a monster! " + text)
    if choice == "1":
        choice = input("You fight the monster with your new sword, and you barely escape alive. Luckily, the monster drops glowing armor, so your efforts were not in vain. You pick it up, and continue your journey.\n" + text2)
        if choice == "1":
            monster3()
        elif choice == "2":
            monster3()
        else:
            no()
    elif choice == "2":
        print("You run away like a coward. However, this monster is faster and catches up to you. It quickly finishes you off, and you die")
    else:
        no()

def monster(): #The first monster battle
    choice = input("You've come across a monster! " + text)
    if choice == "1":
        print("You foolish idiot! You are no match for the monster. It quickly finishes you off and you die.")
    elif choice == "2":
        choice = input("You run away like a coward. However, the monster cannot catch up to you. As you run, you see a shining sword. You pick it up, and continue your journey.\n" + text2)
        if choice == "1":
            monster2()
        elif choice == "2":
            monster2()
        else:
            no()
    else:
        no()

def game(): #The game itself
    choice = input("You wake up to find yourself in a dark room. What do you do?\n\n1) Go towards the light\n2) Stay in the dark room\n\n")
    if choice == "1":
        choice = input("You walk towards to light, only to find yourself at an intersection. Do you\n1) Go left\n2) Go right\n\n")
        if choice == "1":
            monster()
        elif choice == "2":
            choice == input("You see God. Do you\n1) Fight\n2) Run\n\n")
            if choice == "1":
                print("You're trying to fight God?! You die, obviously!")
            elif choice == "2":
                print("You're trying to run away from God?! You die, obviously!")
            else:
                no()
        else:
            no()
    elif choice == "2":
        choice = input("You decide to stay. Do you:\n1)Go foward\n2)Go backwards\n\n")
        if choice == "1":
            print("You fall into a pit of spikes and you die!")
        elif choice == "2":
            print("You fall into a pit of snakes and you die!")
        else:
            no()
    else:
        no()

game()
