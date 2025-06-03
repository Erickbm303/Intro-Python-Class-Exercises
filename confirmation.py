def mode():
    firstName = input("What is your first name?")
    lastName = input("What is your last name?")
    email = input("what is your email?")
    phoneNumber = input("What is your phone number?")

    print("Please verify the data you entered here is correct:")
    print("First Name:", firstName)
    print("Last Name:", lastName)
    print("Email:", email)
    print("Phone:", phoneNumber)
    
    verification = input("Is the information correct?")

    print("Thank you,", firstName, lastName)

mode()