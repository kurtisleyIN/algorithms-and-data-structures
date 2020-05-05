# python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
   
    Fib = [0,1,1]
    Counter = 2

    while (Fib[Counter-1] % m != 0) or (Fib[Counter] % m != 1):
        Fib.append(Fib[Counter-1] + Fib[Counter])
        Counter = Counter + 1
        
    Counter = Counter - 1
        
    return Fib[n % Counter] % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
