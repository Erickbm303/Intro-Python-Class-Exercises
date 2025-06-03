def mode():
    item1 = float(input("Please enter the price for item1: $"))
    item2 = float(input("Please enter the price for item2: $"))
    item3 = float(input("Please enter the price for item3: $"))
    item4 = float(input("Please enter the price for item4: $"))

    totalPrice = item1 +item2 + item3 + item4
    tax = totalPrice * 0.0865
    totalAfterTax = totalPrice + tax

    print("Thank you for shopping with Walmart")
    print("Your total is: $", totalPrice)
    print("taxes: $", tax)
    print("Your total including tax is: $", totalAfterTax)

mode()
