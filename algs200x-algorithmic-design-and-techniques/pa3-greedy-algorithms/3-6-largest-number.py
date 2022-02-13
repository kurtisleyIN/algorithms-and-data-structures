#! python3
from functools import cmp_to_key
import sys


def compare_numbers(x, y):
    """ Decide which concatenation of numbers is largest, 1 if expect bigger than"""

    x_string = str(x)
    y_string = str(y)
    xy_string = x_string + y_string
    yx_string = y_string + x_string
    if xy_string > yx_string:
        return +1
    elif xy_string < yx_string:
        return -1
    return 0


def largest_number(numbers):
    """ Calculate the largest number that can created using the input list of numbers """

    # Do a quick sorting based on the first digit of the number
    numbers = sorted(numbers, key=cmp_to_key(compare_numbers), reverse=True)

    return int(''.join([str(number) for number in numbers]))


if __name__ == '__main__':
    data = sys.stdin.read().split()
    a = data[1:]
    print(largest_number(a))
