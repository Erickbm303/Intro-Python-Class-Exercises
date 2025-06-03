def main():

    i = 3

    user = input("What is your username?")

    if user == "dannita":
        password = 104
    elif user == "erick":
        password = 1111
    else:
        while user != "dannita" and user != "erick":
            print("Wrong username please try again")
            user = input("What is your username?")
        if user == "dannita":
            password = 104
        elif user == "erick":
            password = 1111
        else:
            print("wtf") 

    passwordAttempt = int(input("Please put your password:"))

    if passwordAttempt == password:
        print("Welcome", user, "!")
    else:
        while passwordAttempt != password and i >= 0:
            print("Wrong password, try again. You have", i, "attempts")
            passwordAttempt = int(input("Please put your password:"))
            i = i - 1
        if passwordAttempt != password:
            print("To many attempts, security alert.")
        else:
            print("Welcome", user,"!")
        
main()