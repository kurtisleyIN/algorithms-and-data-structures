# python3
import sys

def get_change(m):
    coins = [4,3,1]
    
    table = [0 for i in range(m+1)]
    table[0] = 0
    
    for i in range(1, m + 1): 
        table[i] = sys.maxsize 
    
    for i in range(1, m + 1): 
        for coin in coins: 
            if (coin <= i): 
                SubResult = table[i - coin] 
                if (SubResult != sys.maxsize and SubResult + 1 < table[i]): 
                    table[i] = SubResult + 1
    return table[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
