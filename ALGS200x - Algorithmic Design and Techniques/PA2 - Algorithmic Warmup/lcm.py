# python3
# Input: Two integers (a and b)
# Output: The least common multiple of a and b

import sys

def gcd(a, b):
    
    # Exit statement for this recursive function
    if b == 0:
        return a
    
    # Reassign a as the modulo of a and b
    a = a % b
    
    # Recall the function by switching a and b
    return gcd(b, a)

def lcm(a, b):
    
    # Calculate the greatest common denominator
    gcdx = gcd(a, b)
    
    # The least common multiple is the product divided by the greatest common denominator
    return (a*b)//gcdx

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
