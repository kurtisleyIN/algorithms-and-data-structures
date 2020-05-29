# python3
# Input:
# Output:

import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1
    return tree

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
