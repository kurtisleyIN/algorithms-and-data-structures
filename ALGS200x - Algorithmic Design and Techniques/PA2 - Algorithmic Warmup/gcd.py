# python3
# Input: Two integers (a and b)
# Output: The greatest common denominator of a and b

import sys

def gcd_naive(a, b):
    
    # Exit statement for this recursive function
    if b == 0:
        return a
    
    # Reassign a as the modulo of a and b
    a = a % b
    
    # Recall the function by switching a and b
    return gcd_naive(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
