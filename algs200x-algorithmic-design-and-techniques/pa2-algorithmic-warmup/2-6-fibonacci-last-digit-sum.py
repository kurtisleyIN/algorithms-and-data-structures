#! python3
import sys


def fibonacci_sum(final):
    """ Calculate the last digit of the sum of the Fibonacci sequence """

    # If final <= 1, no calculation required
    if final <= 1:
        return final

    # Build the modulo pattern for the Fibonacci last digit sum
    fibonacci = [0, 1]
    for index in range(2, 61):
        fibonacci.append((fibonacci[index-2] + fibonacci[index-1]) % 10)

    return sum(fibonacci[:(final % 60)+1]) % 10


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum(n))
