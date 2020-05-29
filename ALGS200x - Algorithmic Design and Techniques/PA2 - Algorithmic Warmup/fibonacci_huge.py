# python3
# Input: Two integers (n and b)
# Output: The remainder (modulo) of the nth Fibonacci number by b

import sys

def get_fibonacci_huge(n, b):
    
    # If n <= 1, no calculation required
    if n <= 1:
        return n
    
    # Initialize the Fibonacci array and the last index position
    Fib = [0,1,1]
    Index = 2
    
    # The sequence of modulo follows a periodic sequence that always starts with 0 and 1
    # This loop calculates and appends the Fibonacci array until the starting sequence is found
    while (Fib[Index-1] % b != 0) or (Fib[Index] % b != 1):
        Fib.append(Fib[Index-1] + Fib[Index])
        Index += 1
    
    # Back up the index position by 1    
    Index -= 1
        
    return Fib[n % Index] % b

if __name__ == '__main__':
    input = sys.stdin.read();
    n, b = map(int, input.split())
    print(get_fibonacci_huge(n, b))
