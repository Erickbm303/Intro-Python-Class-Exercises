def main():
    sum = 0
    budget = float(input("enter amount budget for the week:"))
    while spent != 0:
        spent = float(input("Enter an amount spent(0 to quit):"))
        budget = budget - spent
    print("Budgeted: $", budget)
    print("Spent: $", sum)

    difference = budget - spent
    if budget > sum:
        print(f"You are ${difference}") 
main()