def main():

    myList = [10, 20, 30, 40]

    print(myList[0], myList[1], myList[2], myList[3])

    print(len(myList))

    i = 0
    while i < len(myList):
        print(myList[i])
        i += 1

    size = ["XS", "S", "M", "L", "XL"]
    print(size)

    size = ["XS", "S", "M", "L", "XL"] * 100
    print(size)

main()