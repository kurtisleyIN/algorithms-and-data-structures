# python3
# Input: An integer (money)
# Output: The minimum number of coins (denominations of 1,5,10) to make change for money

import sys

def get_change(money):
    
    # Initialize the counting variable
    Counter = 0
    
    # Take as many 10s, 5s, then 1s until money == 0
    while money >= 10:
        money -= 10
        Counter += 1
    while money >= 5:
        money -= 5
        Counter += 1
    while money >= 1:
        money -= 1
        Counter += 1
        
    return Counter

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
