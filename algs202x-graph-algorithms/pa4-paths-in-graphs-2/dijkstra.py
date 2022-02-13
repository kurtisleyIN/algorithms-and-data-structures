# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected and the weight/cost of each edge
#        Last pair of vertices are the vertices in question (x and y)
# Output: Minimum weight to get from x to y, -1 if none

import sys
import heapq

def distance(AdjacentList, cost, sumCost, x, y):
    dist = [sumCost+1]*len(AdjacentList)
    dist[x] = 0
    prev = [-1]*len(AdjacentList)
    h = list(zip(dist,range(len(dist))))
    heapq.heapify(h)
    while len(h) > 0:
        u = heapq.heappop(h)
        for ind,i in enumerate(AdjacentList[u[1]]):
            if dist[i] > u[0] + cost[u[1]][ind]:
                dist[i] = u[0] + cost[u[1]][ind]
                prev[i] = u[1]
                heapq.heappush(h,(dist[i],i))
    if dist[y] == sumCost + 1:
        return -1
    else:
        return dist[y]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3*edge):3], data[1:(3*edge):3]), data[2:(3*edge):3]))
    data = data[3*edge:]
    AdjacentList = [[] for _ in range(vert)]
    cost = [[] for _ in range(vert)]
    sumCost = 0
    for ((a, b), w) in edges:
        AdjacentList[a - 1].append(b - 1)
        cost[a - 1].append(w)
        sumCost += w
    x, y = data[0] - 1, data[1] - 1
    print(distance(AdjacentList, cost, sumCost, x, y))
