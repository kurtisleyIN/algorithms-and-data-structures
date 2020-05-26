# python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    a = a % b
    return gcd(b, a)

def lcm(a, b):
    gcdx = gcd(a, b)
    return (a*b)//gcdx

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
