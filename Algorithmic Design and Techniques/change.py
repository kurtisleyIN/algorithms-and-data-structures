# python3
import sys

def get_change(m):
    Counter = 0
    
    while m >= 10:
        m = m-10
        Counter = Counter + 1
    while m >= 5:
        m = m-5
        Counter = Counter + 1
    while m >= 1:
        m = m-1
        Counter = Counter + 1
        
    return Counter

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
