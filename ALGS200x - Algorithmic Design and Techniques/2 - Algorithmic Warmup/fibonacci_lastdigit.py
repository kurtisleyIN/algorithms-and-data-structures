# python3
# Input: An integer (n)
# Output: The last digit of the nth Fibonacci number

def calc_fib_lastdigit(n):
    
    # Initialize the Fibonacci last digit array
    Fib = [0,1]
    
    # If n <= 1, no calculation required
    # Calculate and append the Fibonacci last digit array until the nth value is found
    if n <= 1:
        return n
    for i in range(2,n+1):
        Fib.append((Fib[i-1] + Fib[i-2]) % 10)

    return Fib[n]

n = int(input())
print(calc_fib_lastdigit(n))

