def main():

    valuePennies = 0.01
    valueNickles = 0.05
    valueDimes = 0.10
    valueQuaters = 0.25

    print("Enter one dollar to win")

    numPennies = int(input("How many pennies do you have?"))
    numNickles = int(input("How many nickles do you have?"))
    numDimes = int(input("How many dimes do you have?"))
    numQuaters = int(input("How many quaters do you have?"))

    total = numPennies * valuePennies + numNickles * valueNickles + numDimes * valueDimes + numQuaters * valueQuaters

    if total < 1:
        print("sorry you have less than one dollar")
    elif total > 1:
        print("Sorry you have more than on dollar")
    else:
        print("Congratulations you have one dollar! You won!!")

main()