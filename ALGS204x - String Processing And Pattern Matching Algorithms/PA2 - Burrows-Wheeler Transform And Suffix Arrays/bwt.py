# python3
# Input: A string (text) ending with the '$' symbol
# Output: The Burrows-Wheeler Transform of "text"

import sys

def rotations(text):
    n = len(text)
    new_text = text * 2
    return [new_text[i:i + n] for i in range(n)]

def bwm(text):
    return sorted(rotations(text))

def BWT(text):
    n = len(text)
    burrows_wheeler_matrix = bwm(text)
    return ''.join([burrows_wheeler_matrix[i][n - 1] for i in range(n)])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))