def calculator():

    print("Calculator")
    print("Operations: +, -, *, /. \n")

    while True:
        try:

            num1 = float(input("Select first number:"))
            op = input("Enter operation:")
            num2 = float(input("Select second number:"))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if op == 0:
                    print("You cannot divide by 0")
                else:
                    result = num1 / num2
            else:
                print("Invalid Operation")
            
            print(f"Result: {result} \n")

        except ValueError:
            print("Wrong input \n")

        again = input("Do you want to try again?(yes/no)")
        if again.lower() != 'yes':
            print("Good bye!")

calculator()
