import random
import math


def play():
    userinput = input("Select r for rock, p for paper, s for scissors: ")
    userinput = userinput.lower()

    options = ("r", "p", "s")

    if userinput in options:
        print("Great choice!")

    else:
        print("Invalid Input")    

    computer = random.choice(["r", "p", "s"])

    if userinput == computer:
        print("You and the computer both chose {}. It's a tie!".format(computer))


    if is_win(userinput, computer):
        print("You chose {} and the computer chose {}. You win!".format(userinput, computer))

    else:
       print("You chose {} and the computer chose {}. Sorry, you lost.".format(userinput, computer))

def is_win(userinput, computer):
    if(userinput == "r" and computer == "s") or (userinput == "s" and computer == "p") or (userinput == "p" and computer == "r"):
        return True

if __name__ == '__main__':
    play()       


