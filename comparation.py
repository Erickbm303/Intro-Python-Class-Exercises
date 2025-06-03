def main():

    weight1 = float(input("Enter the weight for package 1:"))
    price1 = float(input("Enter price for package 1: $"))
    Weight2 = float(input("Enter weight for package 2:")) 
    price2 = float(input("Enter price for package 2: $"))

    unit1 = price1/weight1
    unit2 = price2/Weight2

    if unit2 > unit1:
        print("Package 1 has a better price.")
    else:
        print("Package 2 has a better price")

main()