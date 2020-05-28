# python3
# Input: An integer (n)
# Output: The nth Fibonacci number

def calc_fib(n):
    
    # Initialize the Fibonacci array
    Fib = [0,1]
    
    # If n <= 1, no calculation is required
    # Calculate and append the Fibonacci array until the nth value is found
    if n <= 1:
        return n
    for i in range(2,n+1):
        Fib.append(Fib[i-1] + Fib[i-2])

    return Fib[n]

n = int(input())
print(calc_fib(n))
