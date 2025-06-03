#LotteryMachine.py

import random
def main():
    lottery_list = [0,0,0,0,0,0,0,0,0]

    for i in range(9):
        lottery_list[i] = random.randint(0, 99)

    print(lottery_list)

main()
