# python3
# Input: Two integers (a and b)
# Output: The greatest common denominator of a and b
import sys

def gcd_naive(a, b):
    if b ==0:
        return a
    a = a % b
    return gcd_naive(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
