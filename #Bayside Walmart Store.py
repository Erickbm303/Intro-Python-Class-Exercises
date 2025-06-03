#Bayside Walmart Store
def main():
    print("Enter the Monthly Earnings for the Bayside Walmart store:")

    profit = [0]*12

    i = 0
    while i < len(profit):
        print("Enter month #", i + 1, "Sales:", end="")
        profit[i] = float(input())
        i += 1
    print(profit)

    q1 = profit[0] + profit [1] + profit [2]
    q2 = profit[3] + profit [4] + profit [5]
    q3 = profit[6] + profit [7] + profit [8]
    q4 = profit[9] + profit [10] + profit [11]

    print("Total earning of the Walmart Store in quarter 1, 2024 is:", q1)
    print("Total earning of the Walmart Store in quarter 2, 2024 is:", q2)
    print("Total earning of the Walmart Store in quarter 3, 2024 is:", q3)
    print("Total earning of the Walmart Store in quarter 4, 2024 is:", q4)
    
    inquire = int(input("Which month's earning you would like to inquire:"))
    inquire = inquire + 1
    print(f"The earning for {month(inquire)} is:{profit[inquire]}")
def month(inquire):
    if inquire == 2:
        return "January" 
    elif inquire == 3:
        return inquire 
    elif inquire == 4:
        return "March" 
    elif inquire == 5:
        return "April" 
    elif inquire == 6:
        return "May" 
    elif inquire == 7:
        return "June" 
    elif inquire == 8:
        return "July"
    elif inquire == 9:
        return "August" 
    elif inquire == 10:
        return "September" 
    elif inquire == 11:
        return "Octuber"
    elif inquire == 12:
        return "Novermber"
    elif inquire == 13:
        return "December"
    else:
        return ("Wrong input")
main()