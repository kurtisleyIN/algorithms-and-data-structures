# python3
# Input: An integer (money)
# Output: The minimum number of coins (denominations 1,3,4) that make change for m

import sys

def get_change(money):
    
    # Set coin denominations in decreasing order
    coins = [4,3,1]
    
    # Create the working array and initialize each element to sys.maxsize
    ChangeArray = [0 for i in range(money + 1)]    
    for i in range(0, money + 1): 
        ChangeArray[i] = sys.maxsize
    
    # Set first element to 0
    ChangeArray[0] = 0
    
    # Loop through all the integers <= money
    for i in range(1, money + 1):
        # Loop through all possible coin values
        for coin in coins:
            # Only look at coin values <= i
            if coin <= i:
                # Store the possible array element to build off of
                BuildElement = ChangeArray[i - coin]
                # If the build element isn't sys.maxsize and it's less than the current number of coins, use it
                if (BuildElement != sys.maxsize and BuildElement + 1 < ChangeArray[i]): 
                    ChangeArray[i] = BuildElement + 1
    return ChangeArray[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
