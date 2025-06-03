#analyst

def main():
    
    num_days = int(input("Enter the days of this month: "))
    num_left = [0] * num_days

    print("Enter the sales of each day:")

    i = 0
    while i < len(num_left):
        print("Enter the number", i + 1, "of", num_days,":", end="")
        num_left[i] = float(input())
        i += 1
    
    print("Sales:", num_left)
    print("Total days:", len(num_left), "days")
    print("Total:", sum(num_left))
    print("Highest:", max(num_left))
    print("Lowest:", min(num_left))
    print("Average:", sum(num_left) / len(num_left))

main()