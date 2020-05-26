# python3
# Input: Two integers (n and b)
# Output: The remainder (modulo) of the nth Fibonacci number by b
import sys

def get_fibonacci_huge(n, b):
    if n <= 1:
        return n
   
    Fib = [0,1,1]
    Counter = 2

    while (Fib[Counter-1] % b != 0) or (Fib[Counter] % b != 1):
        Fib.append(Fib[Counter-1] + Fib[Counter])
        Counter = Counter + 1
        
    Counter = Counter - 1
        
    return Fib[n % Counter] % b

if __name__ == '__main__':
    input = sys.stdin.read();
    n, b = map(int, input.split())
    print(get_fibonacci_huge(n, b))
