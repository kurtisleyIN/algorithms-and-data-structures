# python3
# Input: A string (text) with the '$' at the end
# Output: A list of starting positions of sorted suffixes separated by spaces

import sys

def build_suffix_array(text):
    result = []
    suffixes = []

    for i in range(len(text)):
        suffixes.append((i, text[i:]))

    suffixes = sorted(suffixes, key=lambda t: t[1])

    for i in range(len(suffixes)):
        result.append(suffixes[i][0])

    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))