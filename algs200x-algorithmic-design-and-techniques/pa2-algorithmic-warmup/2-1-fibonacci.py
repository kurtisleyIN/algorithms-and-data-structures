#! python3

def calc_fib(final):
    """ Calculate the Fibonacci sequence up to the input value"""
    
    # Initialize the Fibonacci array
    fibonacci = [0, 1]
    
    # If n <= 1, no calculation is required
    if final <= 1:
        return final

    # Calculate and append the Fibonacci array until the nth value is found
    for index in range(2, final+1):
        fibonacci.append(fibonacci[index-1] + fibonacci[index-2])

    return fibonacci[final]

if __name__ == '__main__':

    n = int(input())            # Integer to which the sequence should be calculated
    print(calc_fib(n))
