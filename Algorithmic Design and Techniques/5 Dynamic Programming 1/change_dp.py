# python3
# Input: An integer (money)
# Output: The minimum number of coins (denominations 1,3,4) that make change for m
import sys

def get_change(money):
    coins = [4,3,1]
    
    table = [0 for i in range(money + 1)]
    table[0] = 0
    
    for i in range(1, money + 1): 
        table[i] = sys.maxsize 
    
    for i in range(1, money + 1): 
        for coin in coins: 
            if (coin <= i): 
                SubResult = table[i - coin] 
                if (SubResult != sys.maxsize and SubResult + 1 < table[i]): 
                    table[i] = SubResult + 1
    return table[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
