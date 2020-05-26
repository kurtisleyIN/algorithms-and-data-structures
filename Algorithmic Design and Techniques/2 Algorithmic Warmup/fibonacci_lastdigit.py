# python3
def calc_fib_lastdigit(n):
    Fib = [0,1]
    
    if n <= 1:
        return n
    for i in range(2,n+1):
        Fib.append((Fib[i-1] + Fib[i-2]) % 10)

    return Fib[n]

n = int(input())
print(calc_fib_lastdigit(n))

