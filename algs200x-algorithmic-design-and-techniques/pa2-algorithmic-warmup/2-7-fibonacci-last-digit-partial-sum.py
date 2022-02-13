#! python3
import sys


def fibonacci_partial_sum(start, end):
    """ Calculate the last digit of the partial sum of the Fibonacci sequence """

    if end <= 1:
        return end

    # Build the modulo pattern for the Fibonacci last digit sum
    fibonacci = [0, 1]
    for index in range(2, 61):
        fibonacci.append((fibonacci[index-2] + fibonacci[index-1]) % 10)

    return sum(fibonacci[(start % 60):(end % 60)+1]) % 10


if __name__ == '__main__':
    integers = sys.stdin.read()
    a, b = map(int, integers.split())
    print(fibonacci_partial_sum(a, b))
