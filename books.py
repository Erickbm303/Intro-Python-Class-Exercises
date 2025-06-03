def main():
    print("B&N Booksellers has a book club awards points to its customers based on the number of books purchased each month. The points of awarded as follow:")
    print("Buy 1-3 books, and you will earn 1 point for that purchase.")
    print("Buy 4-6 books, and you will earn 2 points for that purchase.")
    print("Buy 7-9 books, and you will earn 3 points for that purchase.")
    print("Buy 10-12 books, and you will earn 4 points for that purchase.")
    print("Each point is an equivalent of 10% off for you next purchase (maximun of 6 points is allowed)")

    book = int(input("How many books would you like to buy?"))
    price = float(input("What is the total price? $"))

    if book >= 1 and book <= 3:
        print("You earn 1 point!")
    elif book >= 4 and book <= 6:
        print("You earn 2 points!")
    elif book >= 7 and book <= 9:
        print("You earn 3 points!")
    else: 
        print("You earn 4 points!")

    purchase2 = int(input("Do you want to purchase again?"))

    if purchase2 == "yes":
        book2 = int(input("How many books would you like to buy?"))
        price2 = float(input("What is the total price? $"))
        if book >= 1 and book <= 3:
            discount = price2 * 0.1
            total = price2 - discount
        elif book >=4 and book <= 6:
            discount = price2 * 0.1
            total = price2 - discount
        elif book >= 7 and book <= 9:
            discount = price2 * 0.3
            total = price2 - discount
        else:
            discount = price2 * 0.4
            total = price2 - discount
        print("Your total is, $", total)
    else:
        print("See you next time")
    print("Thank you for shopping at B&N Booksellers!")

main()