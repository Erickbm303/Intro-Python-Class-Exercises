def main():
    
    max_attempts = 3
    attempts_left = max_attempts

    users = {
        "dannita": 104,
        "erick": 1111}

    user = input("What is your username?")

    while user not in users:
        print("Wrong username, please try again")
        user = input("What is your username?")

    password = users[user]

    while attempts_left > 0:
        try:
            password_attempt = int(input("Please enter your password: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if password_attempt == password:
            print("Welcome", user, "!")
            return
        else:
            attempts_left -= 1
            print(f"Wrong password, try again. You have {attempts_left} attempts left.")

    print("Too many attempts, security alert.")

main()