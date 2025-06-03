def main():

    print("Enter 0 to end the sum")
 
    x = int(input("Enter the first number: "))
    y = 1

    while y != 0:
        y = int(input("Enter the next number: "))
        x = x + y
    
    print(x)

main()
