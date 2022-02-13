#! python3
import sys

def fibonacci_sum(final):
    """ Calculate the last digit of the sum of the Fibonacci number """

    # Initialize the Fibonacci sequence
    fibonacci = [0, 1]

    if final <= 1:
        return final

    for index in range(2, 61):
        fibonacci.append((fibonacci[index-2] + fibonacci[index-1]) % 10)

    return sum(fibonacci[:(final % 60)+1]) % 10


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum(n))
