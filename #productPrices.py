#productPrices

def main ():
    
    product = int(input("How many products would you like to enter their prices? "))
    productList = [0] * product

    print("Please enter the prices of the products:")

    i = 0
    while i < len(productList):
        print("Product #", i + 1, "of #", product, ":", end="$")
        productList[i] = float(input())
        i += 1
        
    print("The amount of the products are:", len(productList), "products")
    print("The prices are:", productList)
    print("Total:", sum(productList))
    print("The maximum price is:", max(productList))
    print("The minimum price is:", min(productList))
    print("The average price is:", sum(productList) / len(productList))
    

main()

    

