#! python3
import sys


def calculate_gcd(number1, number2):
    """ Calculate the greatest common denominator of two integers """
    
    # Exit statement for this recursive function
    if number2 == 0:
        return number1
    
    # Reassign number1 as the modulo of number1 and number2
    number1 = number1 % number2
    
    # Recall the function by switching number1 and number2
    return calculate_gcd(number2, number1)


def calculate_lcm(number1, number2):
    """ Calculate the least common multiple of two integers """
    
    # Calculate the greatest common denominator
    gcd = calculate_gcd(number1, number2)
    
    # The least common multiple is the product divided by the greatest common denominator
    return (number1*number2)//gcd


if __name__ == '__main__':
    integers = sys.stdin.read()            # Two integers
    a, b = map(int, integers.split())
    print(calculate_lcm(a, b))
