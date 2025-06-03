#Lottery number changer

import random
def main(): 
    lotteryList = generateNewList()
    guessCount = 1

    guess = int(input("Please guess a lottery number between 10-99:"))

    while guess not in lotteryList:
        print("Sorry, you lost.", guess, "is not in your list", lotteryList)
        print("Generating new list...")
        lotteryList = generateNewList()
        guess = int(input("Please guess a lottery number between 10-99:"))
        guessCount = guessCount + 1

    print("Congratulation:", guess, "is in your lottery list", lotteryList)
    print("It took you ", guessCount, "guesses.")

def generateNewList():
    newLotteryList = [0] * 3

    for i in range(3):
        newLotteryList[i] = random.randint(10,99)
    
    return newLotteryList
main()