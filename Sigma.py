def main(): 
    
    i = 1
    sum = 0
    limit = int(input("select a limit:"))
   
    while i <= limit:
        sum = sum + i
        i = i + 1

    if limit < 6:
        print("Please select a number greater than 5.")
    else:
        print("1 + 2 + 3 + 4 + 5 + ... +", limit, "=", sum)
        
main()