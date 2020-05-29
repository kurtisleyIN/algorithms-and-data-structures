# python3
# Input:
# Output:

import sys
import queue


def bipartite(adj):
    q = queue.Queue()    
    tag = len(adj) * [0]

    tag[0] = 1
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in adj[u]:
            if tag[i] == tag[u]:
                return 0
            elif tag[i] == 0:
                q.put(i)
                if tag[u] == 1:
                    tag[i] = 2
                else:
                    tag[i] = 1

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
