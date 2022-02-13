#! python3
import sys


def gcd_naive(number1, number2):
    """ Calculate the greatest common denominator of two integers """
    
    # Exit statement for recursion
    if number2 == 0:
        return number1
    
    # Reassign number1 as the modulo of number1 and number2
    number1 = number1 % number2
    
    # Recall the function by switching a and b
    return gcd_naive(number2, number1)


if __name__ == '__main__':

    integers = sys.stdin.read()            # Two integers
    a, b = map(int, integers.split())
    print(gcd_naive(a, b))
