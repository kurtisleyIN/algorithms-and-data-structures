# python3
# Input: Two integers (a and b)
# Output: The sum of a and b
import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)