#SalesList

def main():

    num_days = int(input("Enter the number of days for sales data: "))
    sales = [0] * num_days

    print("Enter the sales for each day:")

    i = 0
    while i < len(sales):
        print("Enter day #", i + 1, "Sales:", end="")
        sales[i] = float(input())
        i += 1
    print(sales)

main()