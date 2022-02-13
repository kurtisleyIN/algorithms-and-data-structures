#! python3

def get_fibonacci_last_digit_naive(final):
    """ Calculate the last digit of the Fibonacci sequence up to the input value """
    
    # Initialize the Fibonacci sequence
    fibonacci = [0, 1]
    
    # If n <= 1, no calculation required
    if final <= 1:
        return final

    # Calculate and append the Fibonacci last digit sequence until the nth value is found
    for index in range(2, final+1):
        fibonacci.append((fibonacci[index-2] + fibonacci[index-1]) % 10)

    return fibonacci[final]


if __name__ == '__main__':

    n = int(input())                    # Integer to which the sequence should be calculated
    print(get_fibonacci_last_digit_naive(n))
