# python3
# Input: The number of nodes in the tree (n) and the parents of each node (parents)
# Output: The height of the tree

import sys
import threading

# Set recursion and stack size limit
sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 25)

def path_len(node_id, parents, cache):
    # Set current parent
    CP = parents[node_id]
    
    # -1 indicates root, so it is height 1
    if CP == -1:
        return 1

    # If the height has already been stored in the cache, return it
    if cache[node_id]:
        return cache[node_id]

    # Recursively store the path length
    cache[node_id] = 1 + path_len(parents[node_id], parents, cache)
    return cache[node_id]

def compute_height(n, parents):
    # Create empty cache
    cache = [0] * n
    
    # Calculate the path length for every node and select the max
    return max([path_len(i, parents, cache) for i in range(n)])

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

threading.Thread(target=main).start()