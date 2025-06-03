def main():
    marketPrice = float(input("Enter the market value of the property: "))

    aV = assessedValue(marketPrice)
    pT = propertyTax(aV)

    print("The assessed value of the property is: ", aV)
    print("The property tax is: ", pT)
    total = aV + pT
    print("The total amount due is: ", total)

def assessedValue(marketPrice):

    aV = marketPrice * 0.60
    return aV

def propertyTax(aV):
    pT = aV * 2/100
    return pT
main()