def main():
    while True:
        print("What is your mood today?")
        print("Enter 1 for Happy")
        print("Enter 2 for OK")
        print("Enter 3 for Sad")
        mood = input("Enter your choice: ")
        
        if mood == "1":
            happy()
        elif mood == "2":
            ok()
        elif mood == "3":
            sad()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def happy():
    print("O O")
    print(" V ")

def ok():
    print("O O")
    print(" - ")

def sad():
    print("@ @")
    print("'~'")

main()