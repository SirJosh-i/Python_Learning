import random, time

# Hero
herohp = 100
Hero = 0
PhyA = 30
your_Name = (str(input("Choose the character's name: ")))

# Enemy or Monsters
Monster = ["Slime", "Hoarde of Goblins", "BloodFang"]
slimeHP = 100
goblinHP = 100
bloodhoundHP = 100

# Monsters Attack
slimedmg = [1,20,30]

goblindmg = [5,20,30,40]

bloodhounddmg = [10,20,30,40,50]

# Starting Display
print("Welcome to the Realm of Darkness\n")
time.sleep(1.7)

# Prologue
print(str(your_Name) + " is walking in a silent dungeon, when SUDDENLY! A mighty shadow appears from the hallow!")
print("The warrior is thrilled and intrigued. He slowly approaches the shadow; Slowly and slowly until disappointment overtakes him.\nOut of the mighty shadow appears, ", end=" ")

# Suprise!
print("A LIME COLORED - SQUISHY SLIME!\n")

# Take your time to read the lore.
# time.sleep(5)

# ---------------------------------------------------------

# First Monster or Enemy
print("You encountered a slime.")

# Spotted a limy slime
while True:

    print(your_Name + " = " + str(herohp), end="")
    print("\t\t", end="")
    print(Monster[0] + " = " + str(slimeHP))

    # Choice
    Hero = str(input("Choices: Attack | Abandon \n"))

    # Condition
    if Hero == "Attack" or Hero == "A" or Hero == "a":
        slimeHP = slimeHP - PhyA

        if slimeHP == 0 or slimeHP < 0:
            print("You have defeated the " + Monster[0])
            herohp = herohp + 50
            time.sleep(1)
            break

    else:
        print("Hero = " + str(herohp - 100))
        if Hero == "Abandon" or Hero == "G" or Hero == "ab":
            print("You died whilst trying to escape!")
        else:
            print("You couldn't decide on time!")
        exit()

    # ---------------------------------------------------------
    time.sleep(1)

    # Enemy retaliates
    print(Monster[0] + " retaliates!\n")
    time.sleep(0.75)
    print(Monster[0] + "'s ", end="")
    slimeA = random.choice(slimedmg)


    # Enemy's Attack Level
    if slimeA == 30:
        print("Heavy Attack!")
    elif slimeA == 20:
        print("Light Attack!")
    else:
        print("Touch!")

    # Hero's remanining health
    herohp = herohp - slimeA

    # Break if you die
    if herohp == 0 or herohp < 0:
        print("You died.")
        break
if herohp == 0 or herohp < 0:
    exit()

# Story after victory against Slime
print("With lust of glory, you move onward. Quenching the sword with your fist with the thrill transparent in your eyes. You move forward... \n")
time.sleep(5)
print("You finally reach a divergent, a forked path. When you try to walk towards it, You hear echoes of laughter and snickering.\nVILE CREATURES, SHOW THINE FACE, you roar!\n")
time.sleep(2)
print("A group of dwarf-like creatures?....oh no wait! Multiple goblins start to appear out of nowhere and within seconds, you are faced by a hoarde of goblins.\n")    
time.sleep(3)
# ----------------------A HOARDE OF GOBLINS------------------------------------

while True:

    print(your_Name + " = " + str(herohp), end="")
    print("\t\t", end="")
    print(Monster[1] + " = " + str(goblinHP))

    # Choice
    Hero = str(input("Choices: Attack | Abandon \n"))

    # Condition
    if Hero == "Attack" or Hero == "A" or Hero == "a":
        goblinHP = goblinHP - PhyA

        if goblinHP == 0 or goblinHP < 0:
            print("You have defeated the " + Monster[1])
            herohp = herohp + 100
            time.sleep(2)
            break

    else:
        print("Hero = " + str(herohp - 100))
        if Hero == "Abandon" or Hero == "G" or Hero == "ab":
            print("You died whilst trying to escape!")
        else:
            print("You couldn't decide on time!")
        exit()

    # ---------------------------------------------------------
    time.sleep(1)


    # Enemy retaliates
    print(Monster[1] + " retaliates!\n")
    time.sleep(0.75)
    print(Monster[1] + "'s ", end="")
    goblinA = random.choice(goblindmg)

    # Enemy's Attack Level
    if goblinA == 40:
        print("Heavy Attack!")
    elif goblinA >= 20:
        print("Light Attack!")
    else:
        print("Touch!")

    # Hero's remanining health
    herohp = herohp - goblinA

    # Break if you die
    if herohp == 0 or herohp < 0:
        print("You died.")
        break

if herohp == 0 or herohp < 0:
    exit()

# After the defeat of Goblins
print("Blood dripping slowly off your fist and your sword almost rusted from the black fluid. You get ready to move forward, carrying your sword and your hope - Hope of escaping the abyss.\n")
print("You continue onward...")
time.sleep(7)
print("Dreary from the walk, with not a sip of water left - your eyes glisten and your hope rekindles when you spot light at last!", end="")
print("You hasten your pace, stretch your arm out to as if catch the light.\n")
time.sleep(3)
print("As you get closer, and closer to the light, it starts to get chillier. Like the shadow that appears when a light is shone, you spot an abyss-like creature emerge from the light.\n")
print("As though it was waiting for your arrival, it leaps and lands right in front of you, shaking the very ground.")

# ---------------------BOSS MONSTER BLOODFANG APPEARS!------------------------

print("DUN! DUN! DUN!")
time.sleep(1.75)
print("BOSS BLOODHOUND MAKES ITS APPEARANCE!")

print("It's eyes were darker than blood, its body so black, that even the abyss would fall to shame. It roared while revealing its sharp fangs.")
time.sleep(1)

while True:
    
    print(your_Name + " = " + str(herohp), end="")
    print("\t\t", end="")
    print(Monster[2] + " = " + str(bloodhoundHP))

    # Choice
    Hero = str(input("Choices: Attack | Abandon \n"))

    # Condition
    if Hero == "Attack" or Hero == "A" or Hero == "a":
        bloodhoundHP = bloodhoundHP - PhyA

        if bloodhoundHP == 0 or bloodhoundHP < 0:
            print("You have defeated the " + Monster[2])
            break

    else:
        print("Hero = " + str(herohp - 100))
        if Hero == "Abandon" or Hero == "G" or Hero == "ab":
            print("You died whilst trying to escape!")
        else:
            print("You couldn't decide on time!")
        exit()

    # ---------------------------------------------------------
    time.sleep(1)


    # Enemy retaliates
    print(Monster[2] + " retaliates!\n")
    time.sleep(0.75)
    print(Monster[2] + "'s ", end="")
    bloodfangA = random.choice(bloodhounddmg)

    # Enemy's Attack Level
    if goblinA == 50:
        print("BLOOD FANG DISASTER!")
    elif goblinA >= 20:
        print("BLOOD BITE!")
    else:
        print("MISS!")

    # Hero's remanining health
    herohp = herohp - goblinA

    # Break if you die
    if herohp == 0 or herohp < 0:
        print("You died.")
        break
