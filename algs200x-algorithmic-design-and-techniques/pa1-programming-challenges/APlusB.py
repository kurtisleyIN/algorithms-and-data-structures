#! python3
import sys


def main(numbers: list) -> None:
    """ Print the sum of the first two integers in a list """
    print(int(numbers[0]) + int(numbers[1]))


if __name__ == '__main__':

    tokens = sys.stdin.read().split()
    main(tokens)
