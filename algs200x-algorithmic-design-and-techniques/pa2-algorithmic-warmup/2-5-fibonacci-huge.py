#! python3
import sys


def get_fibonacci_huge(final, divisor):
    """ Calculate the modulo of the final Fibonacci number by the divisor """

    # Initialize the Fibonacci sequence
    fibonacci = [0, 1]
    
    # If final <= 1, no calculation required
    if final <= 1:
        return final
    
    # The sequence of modulo follows a periodic sequence that always starts with 0 and 1
    # This loop calculates and appends the Fibonacci array until the starting sequence is found
    index = None
    for index in range(2, final+2+1):
        fibonacci.append((fibonacci[index-2] + fibonacci[index-1]) % divisor)
        if (fibonacci[index-1] == 0) and (fibonacci[index] == 1):
            break

    return fibonacci[final % (index-1)]


if __name__ == '__main__':

    integers = sys.stdin.read()              # Two integers (n and b)
    n, b = map(int, integers.split())
    print(get_fibonacci_huge(n, b))
