# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: 1 if the graph is bipartite, 0 if not

import sys
import queue


def bipartite(AdjacentList):
    q = queue.Queue()    
    tag = len(AdjacentList) * [0]

    tag[0] = 1
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in AdjacentList[u]:
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
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*edge):2], data[1:(2*edge):2]))
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
        AdjacentList[b - 1].append(a - 1)
    print(bipartite(AdjacentList))
