#! python3

def calc_fib(final):
    """ Calculate the Fibonacci sequence up to the input value """
    
    # If final <= 1, no calculation required
    if final <= 1:
        return final

    # Calculate and append the Fibonacci array until the nth value is found
    fibonacci = [0, 1]
    for index in range(2, final+1):
        fibonacci.append(fibonacci[index-2] + fibonacci[index-1])

    return fibonacci[final]


if __name__ == '__main__':

    n = int(input())            # Integer to which the sequence should be calculated
    print(calc_fib(n))
