# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
#        Last pair of vertices are the vertices in question (x and y)
# Output: The minimum number of edges to get from x to y (-1 if none)

import sys
import queue 

def distance(AdjacentList, x, y):
    distance = [-1] * len(AdjacentList)
    distance[x] = 0

    q = queue.Queue()
    q.put(x)
    while not q.empty():
        u = q.get()
        for i in AdjacentList[u]:
            if distance[i] == -1:
                distance[i] = distance[u] + 1
                q.put(i)
    return distance[y]

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
    x, y = data[2 *edge] - 1, data[2*edge + 1] - 1
    print(distance(AdjacentList, x, y))