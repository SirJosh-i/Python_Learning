"""GAME RULES:
User input
User input compared to the outcome of computer determines the gameplay
"""
import random, sys

print("Welcome to the Game of ROCK, PAPER and SCISSORS!")
print()

while True:
    #Main Game Starts
    rps = ["Rock", "Paper", "Scissors"]
    print("Choose: ", rps)

    yourChoice = input()

    while yourChoice not in rps:
        print("Invalid Response")
        sys.exit()

    print("V/s")

    #Computer Random response
    computerChoice = random.choice(rps)   #random.choice --> Presents a random element from a given list
    print(computerChoice)

    #Comparision and comment
    if yourChoice == computerChoice:
        print("TIE!")
    elif yourChoice == rps[0] and computerChoice == rps[1] or yourChoice == rps[2] and computerChoice == rps[0] or yourChoice == rps[1] and computerChoice == rps[2]:
        print("You lose!")
    else:
        print("You win!")
        
        #Decision to play more or stop
        print("Do you want to continue?")
        print("Yes \t No")  
        toContinue = input()

        if toContinue == "Yes":
            print("...\n")
        else:
            sys.exit()









